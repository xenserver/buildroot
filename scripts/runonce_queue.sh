#!/bin/bash
set -eu

# Ensures only one process can call 'command' at any time
# Implements a FIFO queue so process starvation does not occur
#
# Use case is to run a command which processes everything
# in the queue at once, so when a job runs it clears out the
# queue to prevent multiple-processing
# 
# Syntax:
# $0 <lock_name> <timeout> <unique_token> <command> [<arg> ...]
#
# NOTE: the script may wait for 2 x timeout as the first timeout
# is waiting to become the head of the queue and the second
# timeout is waiting for <lock_name> to be available

# Consume args as we go so we can use $* to run later
lockfile=.${1//\//_}
shift
timeout=$1
shift
token=${1//\//_}
shift

PID=$$
queue_lockfile=${lockfile}.queue

flock -w 1 $queue_lockfile -c "echo $PID:$token >> $queue_lockfile"

# Wait for either us to be the head of the queue, or the queue to be empty
# (which can happen if someone else has run for us while we were waiting)
timeout $timeout bash << EOT
set -eux
head=\$(flock -w 1 $queue_lockfile -c "head -n1 $queue_lockfile") # PID:token
head_pid=\${head%%:*}
head_token=\${head#*:}
in_queue=\$(grep -c $token $queue_lockfile)
while [ \$in_queue -gt 0 -a "\$head_token" != "$token" ]; do
        sleep 1;
        head=\$(flock -w 1 $queue_lockfile -c "head -n1 $queue_lockfile")
        in_queue=\$(grep -c $token $queue_lockfile)

        head_pid=\${head%%:*}
        head_token=\${head#*:}

        # Remove the head if it's not running
        kill -0 \$head_pid >/dev/null 2>&1 || flock -w 1 $queue_lockfile -c "sed -i '/^\$head\\\$/d' $queue_lockfile"
done
EOT

# We only need to run this command once for all in the queue
# Use the actual lock now, so it doesn't matter if we change the queue, no one else
# will get in here.
(
# Use flock to protect this whole block of code; fd 9 is redirected to $lockfile at the end of the block
# Use a custom exit code so it's clear where the failure occured
flock -w $timeout 9 || exit 76

# Make sure we're still at the head of the queue; a previous run_once lock might have run for us
head=$(head -n1 $queue_lockfile)
head_token=\${head#:*}
if [ "$head_token" == "$token" ]; then

        # We're running for the whole queue here, so remove the queue
	(
	# Use flock to protect this whole block of code; fd 8 is redirected to $queue_lockfile at the end of the block
	flock -w 1 8 || exit 74
	mv -f $queue_lockfile ${queue_lockfile}.running
	touch $queue_lockfile
	) 8>$queue_lockfile

	# Log (if we're logging) who we are running the jobs for, then actually run it
	echo "Running jobs for:"
	cat ${queue_lockfile}.running
        $*
fi
) 9>$lockfile


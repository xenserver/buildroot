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

PID=$$
echo "[$PID] $(date): $0 $*"

# Consume args as we go so we can use $* to run later
lockfile=.${1//\//_}
shift
timeout=$1
shift
token=${1//\//_}
shift

queue_lockfile=${lockfile}.queue

lock_entry="$PID:$token"
flock -w 1 $queue_lockfile -c "echo $lock_entry >> $queue_lockfile"

# Wait for either us to be the head of the queue, or the queue to be empty
# (which can happen if someone else has run for us while we were waiting)
timeout $timeout bash << EOT
set -eu
while \$(flock -w 1 $queue_lockfile -c "grep -q $token $queue_lockfile") ; do
	head=\$(flock -w 1 $queue_lockfile -c "head -n1 $queue_lockfile") # PID:token
	head_pid=\${head%%:*}
	head_token=\${head#*:}
	if [ "\$head_token" == "$token" ] ; then
		echo "[$PID] $token is now head"
		exit 0
	fi
	echo "[$PID] Not head yet (\$head_token) is head.  Waiting for \$head_pid to complete"
	set +e
	wait \$head_pid
	set -e

        # Remove the head now it's not running
        flock -w 1 $queue_lockfile -c "sed -i '/^\$head\\\$/d' $queue_lockfile"
done
echo "[$PID] $token not in the queue any more"
EOT

if $(flock -w 1 $queue_lockfile -c "grep -q $token ${queue_lockfile}.completed"); then
	echo "[$PID] Now present in completed file thanks"
	exit 0
fi
echo "[$PID] Not run by anyone else yet"

# We only need to run this command once for all in the queue
# Use the actual lock now, so it doesn't matter if we change the queue, no one else
# will get in here.
echo "[$PID] $(date) wants lock $lockfile"
(
# Use flock to protect this whole block of code; fd 9 is redirected to $lockfile at the end of the block
# Use a custom exit code so it's clear where the failure occured
flock -w $timeout 9 || exit 76
echo "[$PID] $(date) got lock $lockfile"

# Make sure we're still at the head of the queue; a previous run_once lock might have run for us
head=$(head -n1 $queue_lockfile)
if [ "$head" == "$lock_entry" ]; then

	# Use flock to protect this whole block of code; fd 8 is redirected to $queue_lockfile at the end of the block
	(
	flock -w 1 8 || exit 74
	cat $queue_lockfile > ${queue_lockfile}.running
	) 8>>$queue_lockfile

	# Log (if we're logging) who we are running the jobs for, then actually run it
	echo "[$PID] Running jobs for:"
	cat ${queue_lockfile}.running
        $*

	# Use flock to protect this whole block of code; fd 8 is redirected to $queue_lockfile at the end of the block
	(
	flock -w 1 8 || exit 75
	set +e
	# Grep will 'fail' if there are no lines left after removing those running
	grep -v -f ${queue_lockfile}.running ${queue_lockfile} > ${queue_lockfile}.new
	set -e
	mv ${queue_lockfile}.new ${queue_lockfile}
	cat ${queue_lockfile}.running >> ${queue_lockfile}.completed
	) 8>>$queue_lockfile
fi
) 9>>$lockfile
echo "[$PID] $(date) released lock $lockfile"

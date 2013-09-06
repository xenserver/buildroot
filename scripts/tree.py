import os

class Tree(object):
    def __init__(self):
        self.t = {}

    def append(self, filename, contents=None, permissions=None):
        node = self.t.get( filename, {} )
        if contents:
	    node['contents'] = node.get( 'contents', '' ) + contents
        if permissions:
            if node.has_key('permissions') and node['permissions'] != permissions:
                raise Exception("Trying to change permissions for " % filename)
	    
            if permissions:
                node['permissions'] = permissions
            else:
                node['permissions'] = 0o644
        self.t[filename] = node

    def apply(self, path):
        for k, v in self.t.items():
            permissions = v.get("permissions", 0o644)
            contents = v.get("contents", "")
            fullpath = os.path.dirname( os.path.join(path, k))
            if not os.path.isdir(fullpath):
                print "makedirs(%s)" % fullpath 
                os.makedirs(fullpath)
            f = os.open( os.path.join(path, k), os.O_WRONLY | os.O_CREAT, permissions)
            os.write(f, contents)
            os.close(f)

    def __repr__(self):
        res = ""
        for k, v in self.t.items():
            permissions = v.get("permissions", 0o644)
            contents = v.get("contents", "")
            res += "%s (0o%o):\n" % (k, permissions)
            res += contents
            res += "\n\n"
        return res


import os

class Tree(object):
    def __init__(self):
        self.tree = {}

    def append(self, filename, contents=None, permissions=None):
        node = self.tree.get(filename, {})
        if contents:
            node['contents'] = node.get('contents', '') + contents
        if permissions:
            if node.has_key('permissions') and \
                node['permissions'] != permissions:
                raise Exception("Trying to change permissions for " % filename)
	    
            if permissions:
                node['permissions'] = permissions
            else:
                node['permissions'] = 0o644
        self.tree[filename] = node

    def apply(self, basepath):
        for subpath, node in self.tree.items():
            permissions = node.get("permissions", 0o644)
            contents = node.get("contents", "")
            fullpath = os.path.join(basepath, subpath)

            if not os.path.isdir(os.path.dirname(fullpath)):
                os.makedirs(os.path.dirname(fullpath))

            out = os.open(os.path.join(basepath, subpath), 
                          os.O_WRONLY | os.O_CREAT, permissions)
            os.write(out, contents)
            os.close(out)

    def __repr__(self):
        res = ""
        for subpath, node in self.tree.items():
            permissions = node.get("permissions", 0o644)
            contents = node.get("contents", "")
            res += "%s (0o%o):\n" % (subpath, permissions)
            res += contents
            res += "\n\n"
        return res


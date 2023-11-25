
nodes = []
class Node:
    def __init__(self, par):
        self.p = par #parent
        self.s = set() #set of children
        self.lab = '' #label
        self.sonlabs = set()
        nodes.append(self)

    def __repr__(self):
        return '%s(s=%s)' % (self.lab or 'Node', self.s)

def buildtree(tree):#Parses a string representation of a tree.Recursively builds the tree 
    class cur:
        pos = 0
    dd = {}
    def getnode(par):
        cc = Node(par)
        if tree[cur.pos] == '(':
            while tree[cur.pos] in '(,':
                cur.pos += 1
                cc.s.add(getnode(cc))
            cur.pos += 1
        ff = cur.pos
        while tree[cur.pos] not in '), ;':
            cur.pos += 1
        nam = tree[ff:cur.pos]
        cc.lab = nam
        if nam != '':
            dd[nam] = cc
        return cc
    return (getnode(None), dd)

def count(cur):
    trt = set()
    for son in cur.s:
        trt.update(count(son))
    if cur.lab:
        trt.add(cur.lab)
    cur.sonlabs = trt
    return trt

with open('rosalind_ctbl.txt') as f:
    (root, d) = buildtree(f.readline().strip())
    alllabs = sorted(count(root))
    nn = len(alllabs)
    for j in nodes:
        if len(j.sonlabs) not in (0, 1, nn - 1, nn):
            print(''.join(map(str, map(int, map(j.sonlabs.__contains__, alllabs)))))
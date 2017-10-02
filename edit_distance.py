from zss import simple_distance, Node
import json
import sys

def json_open(fl):
    with open(fl) as f:
        d = json.load(f)
    return d

def mktree(node, child):
    def mktree(node,child):
    if isinstance(child,list):
        for c in child:
            return mktree(node,c)
    elif isinstance(child,dict):
        for k,v in child.items():
    if isinstance(v, dict):
        node.addkid(Node(k))
        return mktree(node,v)
    else:
        node.addkid(Node(k))


def handle_dict(dictionary):
    for k in dictionary:
        if (isinstance(k,dict)):
            handle_dict(k)
        else :
            return k


if __name__ == '__main__':
    node = Node('A')
    fl = sys.argv[1]    
    obj = json_open(fl)

    print (handle_dict(obj[0]))

    #res = mktree(node,obj)
    #print(res)
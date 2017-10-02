from zss import simple_distance, Node
import json
import sys

def json_open(fl):
    with open(fl) as f:
        d = json.load(f)
    return d

def mktree(node, child):

    if not isinstance(child, dict ) and not isinstance(child, list):
        return node.addkid(Node(child))


    if isinstance(child, dict):
        print ("test")
        for k,v in child.items():
            print ("tttt",k,v)
            node.addkid(Node(v))
    else:
        for c in child:
            print (c)
            return mktree(node,c)

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
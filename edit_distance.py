from zss import simple_distance, Node
import json
import sys

def json_open(fl):
    with open(fl) as f:
        d = json.load(f)
    return d

def mktree(node, child,count=0):
    print (count)
    if isinstance(child,list):
        for c in child:
            count+=1
            return mktree(node,c,count)

    elif isinstance(child,dict):
        for k,v in child.items():
            if isinstance(child[k], dict):
                node.addkid(Node(k))
                return mktree(node,v, count)
            else :
                node.addkid(Node(k))
    return node
#(Node("f").addkid(Node("a").addkid(Node("h")).addkid(Node("c").addkid(Node("l")))).addkid(Node("e"))

def loop_tree(dictionary, node):
    print node
    print "----"
    for k,v in dictionary.iteritems():
        if isinstance(dictionary[k], dict):
            loop_tree(dictionary[k], node.addkid(Node(k)))
        else:
            node.addkid(Node(v))
            # print k,v

if __name__ == '__main__':
    node = Node('A')
    # fl = sys.argv[1]
    fl = "test.json"
    json_obj = json_open(fl)

    loop_tree(json_obj[0], node)
    print node
    # res = mktree(node,obj)
    # print(res)

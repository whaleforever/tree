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
                node.addkid(Node(v))                          
#(Node("f").addkid(Node("a").addkid(Node("h")).addkid(Node("c").addkid(Node("l")))).addkid(Node("e"))



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
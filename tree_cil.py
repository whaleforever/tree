from zss import simple_distance, Node
import json
import sys

def json_open(fl):
    with open(fl) as f:
        d = json.load(f)
    return d

def main(node,child):
    if isinstance(child, list) and len(child) == 0:
        return node.addkid(Node(''))
    if not isinstance(child, list) and not isinstance(child, dict):
        return node.addkid(Node(child))
    if isinstance(child, dict):
        for k, v in child.items():
            node.addkid(main(Node(k), v))
    if isinstance(child, list):
        for n, i in enumerate(child):
            node.addkid(main(Node(n), i))



if __name__ == '__main__':
    node = Node('A')
    fl = sys.argv[1]    
    obj = json_open(fl)    
    main(node,obj)
    


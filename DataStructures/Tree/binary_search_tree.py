from DataStructures.Tree import bst_node as bst

def new_map():
    my_bst={"root": None}
    return my_bst

def default_cmp(key,element):
    if key ==bst.get_key(element):
        return 0
    elif key > bst.get_key(element):
        return 1
    else:
        return -1

def size_tree(root):
    if root is None:
        return 0
    else:
        return root["size"]

def insert_node(root,key,value):
    if root is None:
        return bst.new_node(key,value)
    cmp = default_cmp(key,root)
    if cmp < 0:
        root["left"] = insert_node(root["left"],key,value) 
    elif cmp > 0:
        root["right"] = insert_node(root["right"],key,value)
    else:
        root["value"] = value
    root["size"]= 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root

def put (my_bst,key,value):
    my_bst["root"] = insert_node(my_bst["root"],key,value)
    return my_bst

def get_node(root,key):
    if root is None:
        return None
    cmp = default_cmp(key,root)
    if cmp < 0:
        return get_node(root["left"],key)
    elif cmp > 0:
        return get_node(root["right"],key)
    else:
        return root

def get(my_bst,key):
    node= get_node(my_bst["root"],key)
    return bst.get_value(node)

def size(my_bst):
    return size_tree(my_bst["root"])
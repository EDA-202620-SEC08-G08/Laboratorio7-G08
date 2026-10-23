from DataStructures.Tree import bst_node as bst
from DataStructures.List import single_linked_list as sl

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

def contains(my_bst,key):
    node= get_node(my_bst["root"],key)
    return node is not None

def is_empty(my_bst):
    return size(my_bst) == 0

def key_set_tree(root,key_set):
    if root is None:
        return
    key_set_tree(root["left"],key_set)
    sl.add_last(key_set,bst.get_key(root))
    key_set_tree(root["right"],key_set)

def key_set(my_bst):
    key_set=sl.new_list()
    key_set_tree(my_bst["root"],key_set)
    return key_set

def value_set_tree(root,value_set):
    if root is None:
        return
    value_set_tree(root["left"],value_set)
    sl.add_last(value_set,bst.get_value(root))
    value_set_tree(root["right"],value_set)

def value_set(my_bst):
    value_set=sl.new_list()
    value_set_tree(my_bst["root"],value_set)
    return value_set

def get_min_node(root):
    if root is None:
        return None
    elif root["left"] is None:
        return root
    else:
        return get_min_node(root["left"])
def get_min(my_bst):
    node= get_min_node(my_bst["root"])
    return bst.get_key(node)
def get_max_node(root):
    if root is None:
        return None
    elif root["right"] is None:
        return root
    else:
        return get_max_node(root["right"])
def get_max(my_bst):
    node= get_max_node(my_bst["root"])
    return bst.get_key(node)

def delete_min_tree(root):
    if root is None:
        return None
    elif root["left"] is None:
        return root["right"]
    else:
        root["left"] = delete_min_tree(root["left"])
        root["size"]= 1 + size_tree(root["left"]) + size_tree(root["right"])
        return root

def delete_min(my_bst):
    my_bst["root"] = delete_min_tree(my_bst["root"])
    return my_bst
def delete_max_tree(root):
    if root is None:
        return None
    elif root["right"] is None:
        return root["left"]
    else:
        root["right"] = delete_max_tree(root["right"])
        root["size"]= 1 + size_tree(root["left"]) + size_tree(root["right"])
        return root

def delete_max(my_bst):
    my_bst["root"] = delete_max_tree(my_bst["root"])
    return my_bst

def height_tree(root):
    if root is None:
        return 0
    else:
        return 1 + max(height_tree(root["left"]),height_tree(root["right"]))

def height(my_bst):
    return height_tree(my_bst["root"])

def keys_range(root, key_initial, key_final, list_key):
    if root is None:
        return
    key = bst.get_key(root)
    if key_initial < key:
        keys_range(root["left"], key_initial, key_final, list_key)
    if key_initial <= key <= key_final:
        sl.add_last(list_key, key)
    if key < key_final:
        keys_range(root["right"], key_initial, key_final, list_key)

def keys(my_bst, key_initial, key_final):
    list_key = sl.new_list()
    keys_range(my_bst["root"], key_initial, key_final, list_key)
    return list_key

def values_range(root, key_initial, key_final, list_value):
    if root is None:
        return
    key = bst.get_key(root)
    if key_initial < key:
        values_range(root["left"], key_initial, key_final, list_value)
    if key_initial <= key <= key_final:
        sl.add_last(list_value, bst.get_value(root))
    if key < key_final:
        values_range(root["right"], key_initial, key_final, list_value)

def values(my_bst, key_initial, key_final):
    list_value = sl.new_list()
    values_range(my_bst["root"], key_initial, key_final, list_value)
    return list_value

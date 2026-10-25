from DataStructures.Tree import bst_node as bst
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl

def new_map():
    my_bst={"root": None}
    return my_bst

def default_compare(key,element):
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
    cmp = default_compare(key,root)
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
    cmp = default_compare(key,root)
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
    if get(my_bst, key) is None:
        return False
    return True

def is_empty(my_bst):
    if my_bst["root"] is None:
        return True
    return False

def key_set_tree(root,key_list):
    if root is None:
        return key_list
    key_set_tree(root["left"], key_list)
    sl.add_last(key_list, root["key"])
    key_set_tree(root["right"], key_list)
    return key_list

def key_set(my_bst):
    key_list = sl.new_list()
    key_set_tree(my_bst["root"], key_list)
    return key_list

def value_set_tree(root,value_list):
    if root is None:
        return value_list
    value_set_tree(root["left"], value_list)
    sl.add_last(value_list, root["value"])
    value_set_tree(root["right"], value_list)
    return value_list

def value_set(my_bst):
    value_list = sl.new_list()
    value_set_tree(my_bst["root"], value_list)
    return value_list
    
def get_min_node(root):
    if root is None:
        return None
    if root["left"] is None:
        return root["key"]    
    return get_min_node(root["left"])
        
def get_min(my_bst):
    return get_min_node(my_bst["root"])

def get_max_node(root):
    if root is None:
        return None
    if root["right"] is None:
        return root["key"]
    return get_max_node(root["right"])

def get_max(my_bst):
    return get_max_node(my_bst["root"])
    
def delete_min_tree(root):
    if root is None:
        return None
    if root["left"] is None:
        return root["right"]
    root["left"] = delete_min_tree(root["left"])
    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root

def delete_min (my_bst):
    my_bst["root"]= delete_min_tree(my_bst["root"])
    return my_bst

def delete_max_tree(root):
    if root is None:
        return None
    if root["right"] is None:
        return root["left"]
    root["right"] = delete_max_tree(root["right"])
    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root

def delete_max(my_bst):
    my_bst["root"] = delete_max_tree(my_bst["root"])
    return my_bst

def height_tree(root):
    if root is None:
        return 0
    return 1 + max(height_tree(root["left"]), height_tree(root["right"]))

def height(my_bst):
    return height_tree(my_bst["root"])

def keys_range(root, key_initial, key_final, list_key):
    if root is None:
        return list_key
    cmp_ini = default_compare(key_initial, root)
    cmp_fin = default_compare(key_final, root)
    if cmp_ini < 0:
        keys_range(root["left"], key_initial, key_final, list_key)
    if cmp_ini <= 0 and cmp_fin >= 0:
        sl.add_last(list_key, root["key"])
    if cmp_fin > 0:
        keys_range(root["right"], key_initial, key_final, list_key)
    return list_key

def keys(my_bst, key_initial, key_final):
    list_key = sl.new_list()
    keys_range(my_bst["root"], key_initial, key_final, list_key)
    return list_key

def values_range(root, key_initial, key_final, list_value):
    if root is None:
        return list_value
    cmp_ini = default_compare(key_initial, root)
    cmp_fin = default_compare(key_final, root)
    if cmp_ini < 0:
        values_range(root["left"], key_initial, key_final, list_value)
    if cmp_ini <= 0 and cmp_fin >= 0:
        sl.add_last(list_value, root["value"])
    if cmp_fin > 0:
        values_range(root["right"], key_initial, key_final, list_value)
    return list_value

def values(my_bst, key_initial, key_final):
    list_value = sl.new_list()
    values_range(my_bst["root"], key_initial, key_final, list_value)
    return list_value
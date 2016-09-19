from node import Node


def one_iteration(node, polish_list):
    if(type(node) == str):
        polish_list.append((node, 0))
        return node

    if((type(node) != str) and (node.type == '(')):
        return one_iteration(node.parts[0], polish_list)

    for part in node.parts:
        one_iteration(part, polish_list)

    polish_list.append((node.type, len(node.parts)))

def node2list(node):
    polishList = []
    one_iteration(node, polishList)
    return polishList
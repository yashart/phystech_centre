from node import Node


def optimize_bracket_step(node):
    if(type(node) == str):
        return node

    if(node.type == '/'):
        if(type(node.parts[0]) != str) and (node.parts[0].type == '('):
            return Node(node.type, [node.parts[0].parts[0], node.parts[1]])
        if(type(node.parts[1]) != str) and (node.parts[1].type == '('):
            return Node(node.type, [node.parts[0], node.parts[1].parts[0]])

    if (node.type == 'sqrt'):
        if (type(node.parts[0]) != str) and (node.parts[0].type == '('):
            return Node(node.type, [node.parts[0].parts[0]])

    return Node(node.type, [optimize_bracket_step(n) for n in node.parts])

def optimize_bracket(node):
    old_node = Node('', [[]])
    new_node = node
    if(type(new_node) == str):
        return node
    while(new_node.is_equal(old_node) == False):
        old_node = new_node
        new_node = optimize_bracket_step(new_node)

    return new_node

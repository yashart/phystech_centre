#----------------------
#
#tex_converter.py - convert node to tex
#
#----------------------
from node import Node


def tex_dump(node):
    if (type(node) == str):
        return node
    if (node.type == '+'):
        return tex_dump(node.parts[0]) + ' + ' + tex_dump(node.parts[1])
    if (node.type == '-'):
        if(len(node.parts) == 2):
            return tex_dump(node.parts[0]) + ' - ' + tex_dump(node.parts[1])
        if(len(node.parts) == 1):
            return '-' + tex_dump(node.parts[0])
    if (node.type == '*'):
        return tex_dump(node.parts[0]) + ' \cdot ' + tex_dump(node.parts[1])
    if (node.type == '/'):
        return '\\frac{' + tex_dump(node.parts[0]) + '}{' + tex_dump(node.parts[1]) + '}'
    if (node.type == '^'):
        return tex_dump(node.parts[0]) + '^{' + tex_dump(node.parts[1]) + '}'
    if (node.type == '('):
        return '(' + tex_dump(node.parts[0]) + ')'
    if (node.type == 'sqrt'):
        return '\\sqrt{' + tex_dump(node.parts[0]) + '}'
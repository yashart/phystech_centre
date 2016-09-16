#-----------------------------------
#node.py
#
#tree structure
#
#-----------------------------------

class Node:
    def parts_str(self):
        st = []
        for part in self.parts:
            st.append( str( part ) )
        return "\n".join(st)

    def __repr__(self):
        return self.type + ":\n\t" + self.parts_str().replace("\n", "\n\t")

    def add_parts(self, parts):
        self.parts += parts
        return self

    def __init__(self, type, parts):
        self.type = type
        self.parts = parts

    def is_equal(self, node):
        self_str = self.__repr__()
        node_str = node.__repr__()
        if (self_str == node_str):
            return True
        return False
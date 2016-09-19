import unittest
import node2polish_list
import node


class Test(unittest.TestCase):
    def test_polish_list(self):
        testNode = node.Node('+', [node.Node('5', []), node.Node('4', [])])
        polishList = node2polish_list.node2list(testNode)
        self.assertEqual(polishList, [('5', 0), ('4', 0), ('+', 2)])
        testNode2 = node.Node('(', [testNode])
        polishList = node2polish_list.node2list(testNode2)
        self.assertEqual(polishList, [('5', 0), ('4', 0), ('+', 2)])
        testNode3 = node.Node('*', [testNode2, testNode])
        polishList = node2polish_list.node2list(testNode3)
        self.assertEqual(polishList, [('5', 0), ('4', 0), ('+', 2), ('5', 0), ('4', 0), ('+', 2), ('*', 2)])


if __name__ == "__main__":
    unittest.main()

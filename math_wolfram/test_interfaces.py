import unittest
import interfaces
import json

class Test(unittest.TestCase):
    def test_check_equations(self):
        rightList = [{'x':'2','y':'0','res':'1'},
                     {'x':'1', 'y':'2', 'res':'1'},
                     {'x':'2', 'y':'2', 'res':'4'}]
        self.assertTrue(interfaces.check_equation('x^y', rightList))

        rightList2 = [{'x':'2','y':'2','res':'1'},
                     {'x':'1', 'y':'2', 'res':'0.5'},
                     {'x':'5', 'y':'2', 'res':'2.5'}]

        print json.dumps(rightList)

        self.assertTrue(interfaces.check_equation('x/y', rightList2))

if __name__ == "__main__":
    unittest.main()

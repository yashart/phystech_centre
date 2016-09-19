import unittest
import calc_polish_list


class Test(unittest.TestCase):
    def test_calc(self):
        polishList = [('5', 0), ('4', 0), ('+', 2), ('-1', 0), ('4', 0), ('+', 2), ('/', 2)]
        self.assertEqual(calc_polish_list.calc_polish_list(polishList), 3)

    def test_var_to_num(self):
        polishList = [('x', 0), ('y', 0), ('+', 2), ('-1', 0), ('4', 0), ('+', 2), ('/', 2)]
        d = {'x': '5', 'y': '4'}
        calc_polish_list.vars_to_nums(polishList, d)
        self.assertEqual(polishList, [('5', 0), ('4', 0), ('+', 2), ('-1', 0), ('4', 0), ('+', 2), ('/', 2)])


if __name__ == "__main__":
    unittest.main()

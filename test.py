import unittest
from my_sum import sum
from fractions import Fraction

class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)
        
    def test_list_fraction(self):
        data = [1/4, 1/4, 2/5]
        result = sum(data)
        self.assertEqual(result, 1)
    
    def test_bad_type(self):
        data = 1
        with self.assertRaises(TypeError):
            result = sum(data)

if __name__ == "__main__":
    unittest.main()

import unittest 
from RevString import reverse_string

class TestRevString(unittest.TestCase):

    def test_with_boat_text(self):
        self.assertEqual(reverse_string("boat"), "taob")
    
    def test_with_Capitals(self):
        self.assertEqual(reverse_string("cAB"), "BAc")
    
    def test_with_integer(self):
        with self.assertRaises(TypeError):
            reverse_string(1)

    def test_with_list(self):
        with self.assertRaises(TypeError):
            reverse_string([])
    
    def test_with_palindrome(self):
        self.assertEqual(reverse_string("racecar"), "racecar")



if __name__ == "__main__":
    unittest.main()
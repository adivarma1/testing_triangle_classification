"""
Testcases for classify_triangle
@uthor: Adithya Varma Created on: 02/03/20
"""

import unittest

from classify_triangle import classify_triangle

class TestList(unittest.TestCase):
    """ Test cases for classify_Triangle """
    
    def test_invalidInput_A(self):
        self.assertEqual(classify_triangle(5, -6, 7),'It is an Invalid Triangle')

    def test_invalidInput_B(self):
        self.assertEqual(classify_triangle(1, 23, 39),'It is an Invalid Triangle')
    
    def test_invalidInput_C(self):
        self.assertEqual(classify_triangle('a', 1, 10),'It is an Invalid Triangle')
    
    def test_invalidInput_D(self):
        self.assertEqual(classify_triangle('', '', ''),'It is an Invalid Triangle')

    def test_rightTriangle_A(self): 
        self.assertNotEqual(classify_triangle(-3,4,5),'It is a Right Triangle')

    def test_rightTriangle_B(self): 
        self.assertEqual(classify_triangle(4,3,5),'It is a Right Triangle')

    def test_rightTriangle_C(self): 
        self.assertEqual(classify_triangle(12, 5, 13), 'It is a Right Triangle')
    
    def test_equilateralTriangle_A(self): 
        self.assertEqual(classify_triangle(4,4,4),'It is an Equilateral Triangle')

    def test_equilateralTriangle_B(self): 
        self.assertEqual(classify_triangle(7,7,7),'It is an Equilateral Triangle')
    
    def test_isocelesTriangle_A(self): 
        self.assertEqual(classify_triangle(2, 3, 2),'It is an Isoceles Triangle')
    
    def test_isocelesTriangle_B(self):     
        self.assertEqual(classify_triangle(4, 5, 5),'It is an Isoceles Triangle')
    
    def test_isocelesTriangle_C(self):     
        self.assertNotEqual(classify_triangle(1, 5, 1),'It is an Isoceles Triangle')

    def test_scaleneTriangle_A(self): 
        self.assertEqual(classify_triangle(20, 15, 17),'It is a Scalene Triangle')

    def test_scaleneTriangle_B(self): 
        self.assertNotEqual(classify_triangle(3, 4, 4),'It is a Scalene Triangle')

if __name__ == "__main__":
    unittest.main()
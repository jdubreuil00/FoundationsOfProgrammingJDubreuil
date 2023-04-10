"""
@Author Jordan Dubreuil 04/09/2023
Unit testing for Rectangle and Parallelepiped classes and methods.
"""
from shapes import *
import unittest

class TestShapes(unittest.TestCase):
    # Unit test for Perimeter.
    def test_Perimeter(self):
        my_instance = Rectangle(10,20)
        result = my_instance.Perimeter()
        self.assertEqual(result,60)

    # Unit test for Area.
    def test_Area(self):
        my_instance = Rectangle(10,10)
        result = my_instance.Area()
        self.assertEqual(result,100)

    # Unit test for Volume.
    def test_Volume(self):
        my_instance = Parallelepiped(10,20,30)
        result = my_instance.Volume()
        self.assertEqual(result,6000)

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestShapes))
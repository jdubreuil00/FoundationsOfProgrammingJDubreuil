"""
@Author Jordan Dubreuil 04/11/2023
Unit testing for Rectangle and Parallelepiped classes and methods.
"""
from shapes import *
import unittest
import io
from unittest.mock import patch

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

    #Unit test for Display Rectangle Class
    def test_DisplayRect(self):
        my_instance_rect = Rectangle(10,10)

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            my_instance_rect.Display()
            result = "The length of the rectangle is 10.\nThe width of the rectangle is 10.\nThe perimeter of the rectangle is 40.\nThe area of the rectangle is 100."
            self.assertEqual(fake_out.getvalue().strip(), result)
    
    # Unit test for Display Parallelepiped
    def test_DisplayPara(self):
        my_instance_para = Parallelepiped(10,20,30)
        
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            my_instance_para.Display()
            result = "The volume of the parallelepiped is 6000."
            self.assertEqual(fake_out.getvalue().strip(), result)
    


if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestShapes))
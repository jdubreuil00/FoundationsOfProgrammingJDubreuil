"""
@Author Jordan Dubreuil 04/23/2023
Unit testing for Dequeque Abstract Data Type.
"""
from dequeue import *
import unittest
import io
import sys
from unittest.mock import patch

class TestDequeque(unittest.TestCase):
    # Tests Display of Dequeque
    def test_display(self):
        my_instance = Dequeque()
        my_instance.addStart("pizza")
        my_instance.addEnd("taco")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        my_instance.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "['pizza', 'taco']")
        
    # Tests the IsEmpty Method of Dequeque
    def test_IsEmpty(self):
        my_instance = Dequeque()
        self.assertTrue(my_instance.IsEmpty())
        my_instance.addEnd('pizza')
        self.assertFalse(my_instance.IsEmpty())

    # Tests addStart Method of Dequeque
    def test_addStart(self):
        my_instance = Dequeque()
        my_instance.addStart("cheese")
        my_instance.addStart("ramen")
        my_instance.addStart("cookie")
        self.assertEqual(my_instance.food, ['cookie','ramen','cheese'])
        
    # Tests the addEnd Method of Dequeque
    def test_addEnd(self):
        my_instance = Dequeque()
        my_instance.addEnd("cheese")
        my_instance.addEnd("ramen")
        my_instance.addEnd("cookie")
        self.assertEqual(my_instance.food, ['cheese','ramen','cookie'])
    

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestDequeque))
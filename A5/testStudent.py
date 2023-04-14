from student import *
import unittest
import io
from unittest.mock import patch


class TestStudents(unittest.TestCase):
    def test_display(self):
        my_instance = Student("Jordan", "43")
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            my_instance.display()
            result = "Name: Jordan\nAge: 43"
            self.assertEqual(fake_out.getvalue().strip(), result)

    def test_displayEngineer(self):
        my_instance_eng = Engineer("Jordan", "43", "Calculus1")
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            my_instance_eng.displayEngineer()
            result = "Name: Jordan\nAge: 43\nCourses: Calculus1"
            self.assertEqual(fake_out.getvalue().strip(), result)

    def test_displayDoctor(self):
        my_instance_doc = Doctor("Jordan", "43", "Charlton")
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            my_instance_doc.displayDoctor()
            result = "Name: Jordan\nAge: 43\nHospital: Charlton"
            self.assertEqual(fake_out.getvalue().strip(), result)
        pass


if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestStudents))

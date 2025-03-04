import unittest
from employee import Employee


# Create a class that inherits from unittest.TestCase
class TestEmployee(unittest.TestCase):

    # setUp and tearDown method should be in camelCase
    # Testing methods should always start with "test_"

    # setUp method will run its code before every single test
    def setUp(self):
        self.emp1 = Employee("Edward", "Elric", 50000)
        self.emp2 = Employee("Itadori", "Yuji", 35000)

    # tearDown method will run its code after every single test
    def tearDown(self):
        pass

    def test_email(self):

        self.assertEqual(self.emp1.email, "edward.elric@email.com")
        self.assertEqual(self.emp2.email, "itadori.yuji@email.com")

        self.emp1.first = "Alphonse"
        self.emp2.first = "Choso"

        self.assertEqual(self.emp1.email, "alphonse.elric@email.com")
        self.assertEqual(self.emp2.email, "choso.yuji@email.com")

    def test_fullname(self):

        self.assertEqual(self.emp1.fullname, "Edward Elric")
        self.assertEqual(self.emp2.fullname, "Itadori Yuji")

        self.emp1.first = "Alphonse"
        self.emp2.first = "Choso"

        self.assertEqual(self.emp1.fullname, "Alphonse Elric")
        self.assertEqual(self.emp2.fullname, "Choso Yuji")

    def test_apply_raise(self):

        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay, 52500)
        self.assertEqual(self.emp2.pay, 36750)


if __name__ == "__main__":
    unittest.main()

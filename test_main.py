from unittest import TestCase

from main import fizz_buzz_generator


class Test(TestCase):
    def test_fizz_buzz_generator(self):
        # Get all generated items
        fizz_buzz_list = list(fizz_buzz_generator())

        # Assert a list with 100 items is generated
        self.assertEqual(100, len(fizz_buzz_list))

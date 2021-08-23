from unittest import TestCase

from main import fizz_buzz_generator


class Test(TestCase):
    def test_fizz_buzz_generator(self):
        # Get all generated items
        fizz_buzz_list = list(fizz_buzz_generator())

        # Assert a list with 100 items is generated
        self.assertEqual(100, len(fizz_buzz_list))

        # Assert first ten multiples of 3 are "Fizz"
        self.assertEqual("Fizz", fizz_buzz_list[2])
        self.assertEqual("Fizz", fizz_buzz_list[5])
        self.assertEqual("Fizz", fizz_buzz_list[8])
        self.assertEqual("Fizz", fizz_buzz_list[11])
        self.assertEqual("Fizz", fizz_buzz_list[14])
        self.assertEqual("Fizz", fizz_buzz_list[17])
        self.assertEqual("Fizz", fizz_buzz_list[20])
        self.assertEqual("Fizz", fizz_buzz_list[23])
        self.assertEqual("Fizz", fizz_buzz_list[26])
        self.assertEqual("Fizz", fizz_buzz_list[29])

        # Assert there are exactly 33 "Fizz"es
        fizzes = [item for item in fizz_buzz_list if item == "Fizz"]
        self.assertEqual(33, len(fizzes))


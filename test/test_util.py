from unittest import TestCase

from src.util import fizz_buzz_generator


class Test(TestCase):
    def setUp(self) -> None:
        # Get all generated items
        self.fizz_buzz_list = list(fizz_buzz_generator())

    def test_exactly_100_elements_are_generated(self):
        # Assert a list with 100 items is generated
        self.assertEqual(100, len(self.fizz_buzz_list))

    def test_first_five_multiples_of_3_and_5_are_fizzbuzzes(self):
        # Assert first five multiples of 3 and 5 are "FizzBuzz"
        self.assertEqual("FizzBuzz", self.fizz_buzz_list[14])
        self.assertEqual("FizzBuzz", self.fizz_buzz_list[29])
        self.assertEqual("FizzBuzz", self.fizz_buzz_list[44])
        self.assertEqual("FizzBuzz", self.fizz_buzz_list[59])
        self.assertEqual("FizzBuzz", self.fizz_buzz_list[74])

    def test_exactly_6_fizzbuzzes_are_generated(self):
        # Assert there are exactly 6 "FizzBuzz"es
        fizzbuzzes = [item for item in self.fizz_buzz_list if item == "FizzBuzz"]
        self.assertEqual(6, len(fizzbuzzes))

    def test_first_ten_multiples_of_3_but_not_5_are_fizzes(self):
        # Assert first ten multiples of 3 (not 5) are "Fizz"
        self.assertEqual("Fizz", self.fizz_buzz_list[2])
        self.assertEqual("Fizz", self.fizz_buzz_list[5])
        self.assertEqual("Fizz", self.fizz_buzz_list[8])
        self.assertEqual("Fizz", self.fizz_buzz_list[11])
        self.assertEqual("Fizz", self.fizz_buzz_list[17])
        self.assertEqual("Fizz", self.fizz_buzz_list[20])
        self.assertEqual("Fizz", self.fizz_buzz_list[23])
        self.assertEqual("Fizz", self.fizz_buzz_list[26])
        self.assertEqual("Fizz", self.fizz_buzz_list[32])
        self.assertEqual("Fizz", self.fizz_buzz_list[35])

    def test_exactly_33_fizzes_are_generated(self):
        # Assert there are exactly 33 "Fizz"es
        fizzes = [item for item in self.fizz_buzz_list if item == "Fizz"]
        self.assertEqual(27, len(fizzes))

    def test_first_ten_multiples_of_5_but_not_3_are_buzzes(self):
        # Assert first ten multiples of 5 (not 3) are "Buzz"
        self.assertEqual("Buzz", self.fizz_buzz_list[4])
        self.assertEqual("Buzz", self.fizz_buzz_list[9])
        self.assertEqual("Buzz", self.fizz_buzz_list[19])
        self.assertEqual("Buzz", self.fizz_buzz_list[24])
        self.assertEqual("Buzz", self.fizz_buzz_list[34])
        self.assertEqual("Buzz", self.fizz_buzz_list[39])
        self.assertEqual("Buzz", self.fizz_buzz_list[49])
        self.assertEqual("Buzz", self.fizz_buzz_list[54])
        self.assertEqual("Buzz", self.fizz_buzz_list[64])
        self.assertEqual("Buzz", self.fizz_buzz_list[69])

    def test_exactly_14_buzzes_are_generated(self):
        # Assert there are exactly 14 "Buzz"es
        buzzes = [item for item in self.fizz_buzz_list if item == "Buzz"]
        self.assertEqual(14, len(buzzes))

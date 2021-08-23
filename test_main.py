from unittest import TestCase

from main import fizz_buzz_generator


class Test(TestCase):
    def test_fizz_buzz_generator(self):
        # Get all generated items
        fizz_buzz_list = list(fizz_buzz_generator())

        # Assert a list with 100 items is generated
        self.assertEqual(100, len(fizz_buzz_list))

        # Assert first five multiples of 3 and 5 are "FizzBuzz"
        self.assertEqual("FizzBuzz", fizz_buzz_list[14])
        self.assertEqual("FizzBuzz", fizz_buzz_list[29])
        self.assertEqual("FizzBuzz", fizz_buzz_list[44])
        self.assertEqual("FizzBuzz", fizz_buzz_list[59])
        self.assertEqual("FizzBuzz", fizz_buzz_list[74])

        # Assert there are exactly 6 "FizzBuzz"es
        fizzbuzzes = [item for item in fizz_buzz_list if item == "FizzBuzz"]
        self.assertEqual(6, len(fizzbuzzes))

        # Assert first ten multiples of 3 (not 5) are "Fizz"
        self.assertEqual("Fizz", fizz_buzz_list[2])
        self.assertEqual("Fizz", fizz_buzz_list[5])
        self.assertEqual("Fizz", fizz_buzz_list[8])
        self.assertEqual("Fizz", fizz_buzz_list[11])
        self.assertEqual("Fizz", fizz_buzz_list[17])
        self.assertEqual("Fizz", fizz_buzz_list[20])
        self.assertEqual("Fizz", fizz_buzz_list[23])
        self.assertEqual("Fizz", fizz_buzz_list[26])
        self.assertEqual("Fizz", fizz_buzz_list[32])
        self.assertEqual("Fizz", fizz_buzz_list[35])

        # Assert there are exactly 33 "Fizz"es
        fizzes = [item for item in fizz_buzz_list if item == "Fizz"]
        self.assertEqual(27, len(fizzes))

        # Assert first ten multiples of 5 (not 3) are "Buzz"
        self.assertEqual("Buzz", fizz_buzz_list[4])
        self.assertEqual("Buzz", fizz_buzz_list[9])
        self.assertEqual("Buzz", fizz_buzz_list[19])
        self.assertEqual("Buzz", fizz_buzz_list[24])
        self.assertEqual("Buzz", fizz_buzz_list[34])
        self.assertEqual("Buzz", fizz_buzz_list[39])
        self.assertEqual("Buzz", fizz_buzz_list[49])
        self.assertEqual("Buzz", fizz_buzz_list[54])
        self.assertEqual("Buzz", fizz_buzz_list[64])
        self.assertEqual("Buzz", fizz_buzz_list[69])

        # Assert there are exactly 14 "Buzz"es
        buzzes = [item for item in fizz_buzz_list if item == "Buzz"]
        self.assertEqual(14, len(buzzes))

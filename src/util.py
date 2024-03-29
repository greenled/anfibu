from typing import Iterator


def fizz_buzz_generator() -> Iterator[str]:
    """
    Generates a sequence of strings with numbers from 1 to 100
    """
    num = 1
    while num <= 100:
        if num % 3 == 0 and num % 5 == 0:
            yield "FizzBuzz"
        elif num % 3 == 0:
            yield "Fizz"
        elif num % 5 == 0:
            yield "Buzz"
        else:
            yield str(num)
        num += 1

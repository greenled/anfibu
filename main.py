from typing import Iterator


def fizz_buzz_generator() -> Iterator[str]:
    """
    Generates a sequence of strings with numbers from 1 to 100
    """
    num = 1
    while num <= 100:
        if num % 3 == 0:
            yield "Fizz"
        else:
            yield str(num)
        num += 1


if __name__ == '__main__':
    for fizz_buzz_item in fizz_buzz_generator():
        print(fizz_buzz_item)

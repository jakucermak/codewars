import math


def reverse_fizz_buzz(array):
    fizzer = 0
    buzzer = 0

    for i in range(len(array)):

        if not isinstance(array[i],int):
            if "Fizz" in array[i] and fizzer == 0:
                fizzer = i+1
            if "Buzz" in array[i] and buzzer == 0:
                buzzer = i+1
    return (fizzer,buzzer)

def test_reverse_fizz_buzz():
    assert reverse_fizz_buzz([1, 2, "Fizz", 4, "Buzz"]) == (3, 5)
    assert reverse_fizz_buzz([1, "Fizz", "Buzz", "Fizz", 5, "FizzBuzz"]) == (2, 3)
    assert reverse_fizz_buzz([1, "FizzBuzz", 3, "FizzBuzz", 5, "FizzBuzz"]) == (2, 2)
    assert reverse_fizz_buzz(["Fizz", "Fizz", "Fizz", "Fizz", "Fizz", "FizzBuzz"]) ==(1, 6)
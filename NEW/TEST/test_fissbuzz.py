from fizzbuzz import fizzbuzz

def test_returns_fizzbuzz_if_divisible_3():
    assert fizzbuzz([3]) == ["Fizz"]

def test_returns_fizzbuzz_if_divisible_5():
    assert fizzbuzz([5]) == "Buzz"

def test_returns_fizzbuzz_if_divisible_3_and_5():
    assert fizzbuzz([15,5]) == "Fizzbuzz"

def test_other_case():
    assert fizzbuzz([8]) == 8
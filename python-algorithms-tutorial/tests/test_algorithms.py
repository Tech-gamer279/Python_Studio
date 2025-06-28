import pytest
from src.algorithms import fibonacci, factorial, gcd, is_prime, sieve_of_eratosthenes, binary_search, merge_sort

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-1)

def test_gcd():
    assert gcd(48, 18) == 6
    assert gcd(54, 24) == 6
    assert gcd(101, 10) == 1

def test_is_prime():
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(29) == True

def test_sieve_of_eratosthenes():
    assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]
    assert sieve_of_eratosthenes(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert sieve_of_eratosthenes(1) == []

def test_binary_search():
    arr = [1, 2, 3, 4, 5]
    assert binary_search(arr, 3) == 2
    assert binary_search(arr, 6) == -1

def test_merge_sort():
    assert merge_sort([3, 2, 1]) == [1, 2, 3]
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]
    assert merge_sort([5, 3, 8, 6, 2]) == [2, 3, 5, 6, 8]
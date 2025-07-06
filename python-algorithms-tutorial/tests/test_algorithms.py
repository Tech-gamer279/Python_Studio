import pytest
from src.algorithms import (
    fibonacci, factorial, gcd, is_prime, sieve_of_eratosthenes,
    binary_search, merge_sort
)

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55
    assert fibonacci(15) == 610

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(7) == 5040
    with pytest.raises(ValueError):
        factorial(-1)

def test_gcd():
    assert gcd(48, 18) == 6
    assert gcd(54, 24) == 6
    assert gcd(101, 10) == 1
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
    assert gcd(0, 0) == 0

def test_is_prime():
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(29) == True
    assert is_prime(97) == True
    assert is_prime(100) == False

def test_sieve_of_eratosthenes():
    assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]
    assert sieve_of_eratosthenes(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert sieve_of_eratosthenes(1) == []
    assert sieve_of_eratosthenes(2) == [2]
    assert sieve_of_eratosthenes(0) == []

def test_binary_search():
    arr = [1, 2, 3, 4, 5]
    assert binary_search(arr, 3) == 2
    assert binary_search(arr, 6) == -1
    assert binary_search([], 1) == -1
    assert binary_search([1], 1) == 0
    assert binary_search([1, 3, 5, 7, 9], 7) == 3

def test_merge_sort():
    assert merge_sort([3, 2, 1]) == [1, 2, 3]
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]
    assert merge_sort([5, 3, 8, 6, 2]) == [2, 3, 5, 6, 8]
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

# --- Lessons (docstrings for tutorial use) ---

def lesson_fibonacci():
    """
    Lesson: Fibonacci Sequence
    The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.
    Example: 0, 1, 1, 2, 3, 5, 8, 13, ...
    """

def lesson_factorial():
    """
    Lesson: Factorial
    The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
    Example: 5! = 5 * 4 * 3 * 2 * 1 = 120
    """

def lesson_gcd():
    """
    Lesson: Greatest Common Divisor (GCD)
    The GCD of two numbers is the largest number that divides both of them without leaving a remainder.
    Example: GCD of 48 and 18 is 6.
    """

def lesson_is_prime():
    """
    Lesson: Prime Numbers
    A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
    Example: 2, 3, 5, 7, 11, ...
    """

def lesson_sieve_of_eratosthenes():
    """
    Lesson: Sieve of Eratosthenes
    An efficient algorithm to find all primes up to a given limit.
    """

def lesson_binary_search():
    """
    Lesson: Binary Search
    Binary search is an efficient algorithm for finding an item from a sorted list of items.
    """

def lesson_merge_sort():
    """
    Lesson: Merge Sort
    Merge sort is a divide-and-conquer algorithm that splits a list into halves, sorts each half, and merges them.
    """
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

# ...existing code...

def lesson_recursion():
    """
    Lesson: Recursion
    Recursion is a method of solving problems where a function calls itself as a subroutine.
    Example: Calculating factorial or Fibonacci numbers recursively.
    """

def lesson_sorting_algorithms():
    """
    Lesson: Sorting Algorithms
    Sorting algorithms arrange the elements of a list in a certain order (ascending or descending).
    Examples: Bubble Sort, Merge Sort, Quick Sort.
    """

def lesson_searching_algorithms():
    """
    Lesson: Searching Algorithms
    Searching algorithms are used to find an element in a data structure.
    Examples: Linear Search, Binary Search.
    """

def lesson_time_complexity():
    """
    Lesson: Time Complexity
    Time complexity describes how the runtime of an algorithm increases as the size of the input increases.
    Example: O(n), O(log n), O(n^2)
    """

def lesson_space_complexity():
    """
    Lesson: Space Complexity
    Space complexity describes how much memory an algorithm uses as the size of the input increases.
    """

def lesson_hash_tables():
    """
    Lesson: Hash Tables
    Hash tables store key-value pairs and allow fast lookup, insertion, and deletion.
    Example: Python's built-in dict type.
    """

def lesson_recursion_vs_iteration():
    """
    Lesson: Recursion vs Iteration
    Some problems can be solved both recursively and iteratively. Each approach has its pros and cons.
    """
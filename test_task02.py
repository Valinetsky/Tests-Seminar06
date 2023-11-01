import pytest
import unittest
from hypothesis import given
import hypothesis.strategies as st

from Calc import Calculator

# Testing with pytest


@pytest.fixture
def calculator():
    return Calculator()


def test_add(calculator):
    res = calculator.sum(5, 3)
    assert res == 8


def test_subtract(calculator):
    res = calculator.sub(10, 4)
    assert res == 6

# Testting with - nose


def test_multiply():
    calculator = Calculator()
    res = calculator.mul(2, 3)
    assert res == 6


def test_divide(calculator):
    res = calculator.div(8, 4)
    assert res == 2


# def test_div_by_zero(calculator):
#     with calculator.assertRaises(ValueError):
#         calculator.div(5, 0)

# Testing with doctest
class TestCalculator(unittest.TestCase):
    '''
    Simple test for sum, subtract...


    >>> calculator = Calculator()
    >>> calculator.sum(5, 3)
    8
    >>> calculator.sub(10, 4)
    6
    '''

    def test_divide(self):
        calculator = Calculator()
        res = calculator.div(8, 4)
        self.assertEqual(res, 2)

# Testing with hipothesis


@given(st.integers(), st.integers())
def test_hipothesis_sum(x, y):
    calculator = Calculator()
    res = calculator.sum(x, y)
    assert res == x + y

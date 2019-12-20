# copy of the calc.py file
# remove all the stuff inside the functions
# with this we dont need type hinting in the calc.py file anymore
# this way calc.py will still be compatiable with older versions of python
# since only python 3.5+ has type hinting
from numbers import Real


def add(num1: complex, num2: complex) -> complex

def subtract(num1: Real, num2: Real) -> Real

def multiply(num1: int, num2: int) -> int

def divide(num1: int, num2: int) -> float
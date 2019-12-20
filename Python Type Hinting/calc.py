
# import real numbers type
from numbers import Real

# type hinting
# code will stil run but if using an ide it might tell you it is thw wrong type
# complex is complex numbers type
def add(num1: complex, num2: complex) -> complex:
		return num1 + num2

def subtract(num1: Real, num2: Real) -> Real:
	return num1 - num2

def multiply(num1: int, num2: int) -> int:
	return num1 * num2

def divide(num1: int, num2: int) -> float:
	return num1 / num2

print(add(5,8.2))
print(multiply('hello', 5))
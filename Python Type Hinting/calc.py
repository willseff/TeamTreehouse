# type hinting
# code will stil run but 
def add(num1: int, num2: int) -> int:
		return num1 + num2

def subtract(num1: int, num2: int) -> int:
	return num1 - num2

def multiply(num1: int, num2: int) -> int:
	return num1 * num2

def divide(num1: int, num2: int) -> float:
	return num1 / num2

print(add(5,8.2))
print(multiply('hello', 5))
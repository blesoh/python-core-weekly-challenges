#Import the calculator module into a separate Python script main.py 
#and use its functions to perform arithmetic operations on numbers like 5 and 3.

import calculator
result = calculator.add(5, 3)
print(f"Addition: 5 + 3 = {result}")

result = calculator.subtract(5, 3)
print(f"Subtraction: 5 - 3 = {result}")

result = calculator.multiply(5, 3)
print(f"Multiplication: 5 * 3 = {result}")

result = calculator.divide(5, 3)
print(f"Division: 5 / 3 = {result}")

result = calculator.divide(5, 0)
print(f"Division: 5 / 0 = {result}")

# --- IGNORE ---


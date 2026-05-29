# Demonstrating various functions using lambda expressions in Python

# 1. Addition
add = lambda a, b: a + b
print("Addition:", add(10, 5))

# 2. Subtraction
subtract = lambda a, b: a - b
print("Subtraction:", subtract(10, 5))

# 3. Multiplication
multiply = lambda a, b: a * b
print("Multiplication:", multiply(10, 5))

# 4. Division
divide = lambda a, b: a / b
print("Division:", divide(10, 5))

# 5. Square of a number
square = lambda x: x ** 2
print("Square:", square(6))

# 6. Check even or odd
even_or_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print("Even or Odd:", even_or_odd(7))

# 7. Find maximum of two numbers
maximum = lambda a, b: a if a > b else b
print("Maximum:", maximum(12, 20))

# 8. Convert string to uppercase
uppercase = lambda text: text.upper()
print("Uppercase:", uppercase("python"))

# 9. Using lambda with map()
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print("Squares using map():", squares)

# 10. Using lambda with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter():", even_numbers)

# 11. Using lambda with sorted()
students = [("Teja", 85), ("Ravi", 92), ("Anu", 78)]

sorted_students = sorted(students, key=lambda x: x[1])

print("Students sorted by marks:")
print(sorted_students)

# 12. Lambda with reduce()
from functools import reduce

product = reduce(lambda x, y: x * y, numbers)
print("Product using reduce():", product)
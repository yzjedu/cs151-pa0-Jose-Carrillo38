# Programmers: Jose Carrillo
# Course: CS151, Dr. Olsen
# Due Date: 9/18/2024
# Programming Assignment: PA00 Final
# Problem Statement: The program calculates the hypotenuse of a right triangle using the Pythagorean theorem.
# Data In: The program prompts the user for the lengths of two sides of a right triangle (a and b).
# Data Out: The program outputs the length of the hypotenuse calculated from the given side lengths.
# Credits: Based on the design for Pythagorean theorem implementation for Mateo Carrillo's math studies.

# Importing math module for square root function
import math

# Input: Prompt the user to enter the lengths of two sides of a right triangle
a = int(input("Enter the length of side a: "))
b = int(input("Enter the length of side b: "))

# Pythagorean theorem: c = sqrt(a^2 + b^2)
c = math.sqrt(a**2 + b**2)

# Output: Calculated hypotenuse length to the user
print(f"The length of the hypotenuse for the triangle with sides {a} and {b} is: {c:.2f}")

# Specific Message
print(f"This solution is for Mateo Carrillo's math problem.")

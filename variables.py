# Assigning values to variables
PI = 3.14
age = 30
name = "Alice"

# Type annotations
PI: float
age: int
name: str

# Using the variables
print(f"PI: {PI}, Type: {type(PI)}")
print(f"Age: {age}, Type: {type(age)}")
print(f"Name: {name}, Type: {type(name)}")

# Dynamic typing
age = "thirty"  # No error, age is now a string
print(f"Age: {age}, Type: {type(age)}")

#input

name = input("Your name: ")

print("Name: ", name)
#1
x, y, z = 10, 3.14, "Hello World"

#2
a = 2 + 3j
print("The value of a is:", a) 


b = 10
print("The value of b is:", b)  

# swap the values of a and b
a, b = b, a


print("The new value of a is:", a)  
print("The new value of b is:", b)

#3 with variable
a = 5
b = 10
print("Before swapping: a =", a, "and b =", b)

temp = a
a = b
b = temp

print("After swapping: a =", a, "and b =", b)

#without variable
a = 5
b = 10
print("Before swapping: a =", a, "and b =", b)

a = a + b
b = a - b
a = a - b

print("After swapping: a =", a, "and b =", b)

#4
#  2.x version
name = raw_input("Enter your name: ")
print ("Hello, " + name + "!")

#  3.x version
name = input("Enter your name: ")
print("Hello, " + name + "!")

#5
num1 = int(input("Enter the first number (between 1-10): "))
num2 = int(input("Enter the second number (between 1-10): "))


z = num1 + num2

result = z + 30

# final result
print("The result is:", result)

#6
value = input("Enter a value: ")
data_type = type(value)

print("The data type of the input value is:", data_type.__name__)

#7
# Upper CamelCase
MyVariable = "Hello World"

# Lower CamelCase
myVariable = 42

# SnakeCase
my_variable = 3.14

# UPPERCASE
MY_CONSTANT = "This is a constant value"

#8
Yes, assigning a variable to a different data type value will change the value of the variable.
In Python, variables do not have a fixed data type, and their data type can change dynamically based on the value assigned to them.


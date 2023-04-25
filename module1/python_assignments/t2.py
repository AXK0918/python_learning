#task two 
#1
num = int(input("Enter a number: "))


if num % 3 == 0 and num % 5 == 0:
    print("Consultadd - Python Training")
elif num % 3 == 0:
    print("Consultadd")
elif num % 5 == 0:
    print("Python Training")
else:
    print("The number is not divisible by 3 or 5")

#2
option = int(input("Enter an option (1-5):\n1. Addition\n2. Subtraction\n3. Division\n4. Multiplication\n5. Average\n"))

if option == 1:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
elif option == 2:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 - num2
elif option == 3:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        result = num1 / num2
elif option == 4:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 * num2
elif option == 5:
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    result = (first + second) / 2
else:
    print("Invalid option")

if result < 0:
    print("NEGATIVE")
else:
    print("Result:", result)

#4 
while True:
    num = int(input("Enter a number: "))
    
    if num < 0:
        print("It's Over")
        break
        
    print("Good Going")
    continue

#5
result = []
for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        result.append(num)

print(result)

#6
#output for the first code
1
2
3
#output for the second code
0 
1
2 
Error

#output for third code 
infinite loop that will print the values of count starting from 0 and 
incrementing by 1 in each iteration until it reaches a value of 5 or greater. 
Once the value of count becomes greater than or equal to 5, the loop will break and the program will terminate.

#7
for i in range(7):
    if i == 3 or i == 6:
        continue
    print(i, end=' ')

#8
string = input("Enter a string: ")
letters = digits = 0

for char in string:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

print("Letters:", letters)
print("Digits:", digits)

#9
import random

lucky_number = random.randint(1, 10)

while True:
    guess = int(input("Guess the lucky number (between 1 and 10): "))
    if guess == lucky_number:
        print("Congratulations! You guessed the lucky number!")
        break
    else:
        answer = input("Do you want to guess again? (yes/no): ")
        if answer == "no":
            break
#10
lucky_number = 7
counter = 1

while counter <= 5:
    guess = int(input("Guess the lucky number between 1 and 10: "))
    if guess == lucky_number:
        print("Good guess!")
        break
    else:
        print("Try again!")
        counter += 1

if counter > 5:
    print("Game over!")
#11
import random

lucky_num = random.randint(1, 10)

counter = 1
while counter <= 5:
    guess = int(input(f"Guess the lucky number (Attempt {counter}/5): "))
    if guess == lucky_num:
        print("Good guess!")
        break
    else:
        print("Try again!")
    counter += 1

if counter == 6:
    print("Sorry but that was not very successful.")
else:
    print("Congratulations! You found the lucky number!")

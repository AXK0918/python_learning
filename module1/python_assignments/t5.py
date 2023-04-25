#1
try:
    
    x = 2 +
    
except SyntaxError as error:
   
    print("SyntaxError occurred:", error)
#2
import sys

while True:
    try:
       
        filename = sys.argv[1]
        
        with open(filename, 'r') as f:
            print(f.read())
        break
    except (IndexError, FileNotFoundError):
        print("Please enter a valid filename:")
        filename = input()
#3
while True:
    try:
        
        number = input("Enter a 4-digit number: ")
        
        if len(number) != 4:
            raise ValueError("The length is too short/long!!! Please provide only four digits.")
        
        else:
            print("The number you entered is:", number)
            break
    except ValueError as error:
        
        print(error)

#4
MAX_TRIES = 3

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    for i in range(MAX_TRIES):
        retype_password = input("Re-type your password: ")
        if retype_password == password:
            print("Welcome, {}!".format(username))
            return
        else:
            print("Incorrect password. Please try again.")
            
    print("Too many attempts. Please try again later.")

login()

#5
with open('doc.txt', 'r') as file:
    
    contents = file.read()

    words = contents.split()

    
    even_length_words = [word for word in words if len(word) % 2 == 0]

    print("Even length words:", even_length_words)



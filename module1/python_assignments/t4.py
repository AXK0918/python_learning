#1
def reverse_string(s):
    
    lst = list(s)

    reversed_lst = lst[::-1]


    reversed_s = ''.join(reversed_lst)

    return reversed_s

s = "1234abcd"
reversed_s = reverse_string(s)
print(reversed_s)  # Output: "dcba4321"


#2
def count_upper_lower(s):
   
    uppercase_count = 0
    lowercase_count = 0

  
    for c in s:
        
        if c.isupper():
            uppercase_count += 1
        
        elif c.islower():
            lowercase_count += 1

    print("No. of Uppercase characters:", uppercase_count)
    print("No. of Lowercase characters:", lowercase_count)

#3
def unique_list(lst):
    
    unique_lst = []

    for element in lst:
        
        if element not in unique_lst:
            unique_lst.append(element)

    return unique_lst

#4
words = input("Enter a hyphen-separated sequence of words: ")
word_list = words.split("-")
word_list.sort()
sorted_words = "-".join(word_list)
print(sorted_words)

#5
lines = input("Enter a sequence of lines: ")
lines_upper = lines.upper()
print(lines_upper)


#6
def add_numbers(a, b):
    
    result = int(a) + int(b)
    print(result)

#7
def print_longest_string(str1, str2):

    len1 = len(str1)
    len2 = len(str2)

    if len1 > len2:
        print(str1)
    elif len2 > len1: 
        print(str2)
    else:
       
        print(str1)
        print(str2)

#8
def generate_tuple():
    squares = ()
    
    for i in range(1, 21):
        squares += (i*i,)
        
    return squares

#9
def showNumbers(limit):
    for num in range(limit+1):
        if num % 2 == 0:
            print(num, "EVEN")
        else:
            print(num, "ODD")
#10
even_numbers = list(filter(lambda x: x % 2 == 0, range(1, 21)))
print(even_numbers)

#11
numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

squares = list(map(lambda x: x ** 2, even_numbers))

print(squares)

#12
def divide_by_zero():
    try:
        result = 5/0
    except ZeroDivisionError:
        print("Error: division by zero!")
    else:
        print("Result: ", result)

divide_by_zero()
#13
from functools import reduce

lst = [1,2,3,4,5,6,7]

result = reduce(lambda x, y: 10*x + y, lst)

print(result)

#14
numbers = [21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]
result = list(filter(lambda x: x % 3 != 0 and x % 7 == 0, numbers))
print(result)

#15
def square(num):
    return num*num

my_list = [1, 2, 3, 4, 5]
squared_list = list(map(square, my_list))
print(squared_list)

#16
(i) The output of the code will be 2. 
This is because the finally block is executed always, whether an exception is raised or not.
In this case, the finally block contains a return statement that returns 2, overriding the return statement in the try block.

(ii) The output of the code will be an error message "NameError: name 'f' is not defined".
This is because the function a() is calling a function f(x, 4) which is not defined anywhere in the code, causing a NameError. 
Since there is no exception handler for this error, the program will terminate and the second print statement will not be executed.



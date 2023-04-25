#1
#1 42 (integer)
#2 3.14 (float)
#3 "Hello, world!" (string)
#4 (1+2j) (complex)
#5 -17 (integer)
#6 2.718 (float)
#7 "Data Science" (string)
#8 (-4+3j) (complex)
#9 100 (integer)
#10 6.626e-34 (float)

#2
my_list = ["apple", "banana", "orange", "kiwi", "pear"]
print(my_list[1:3])

#3
my_list = [2, 3, 5, 7, 11]
total_sum, total_product = sum_and_multiply(my_list)
print(f"Sum of all items: {total_sum}")
print(f"Product of all items: {total_product}")

#4
def find_min_max(lst):
    
    smallest = lst[0]
    largest = lst[0]

    
    for item in lst:
        if item < smallest:
            smallest = item
        elif item > largest:
            largest = item

    
    return smallest, largest

#5
def filter_odd_numbers(lst, specified_numbers):
    
    odd_numbers = [item for item in lst if item % 2 != 0]

   
    result = [item for item in odd_numbers if item in specified_numbers]

    
    return result

#6
def square_first_and_last_5():
    
    result = []


    for i in range(1, 6):
        result.append(i ** 2)

    
    for i in range(26, 31):
        result.append(i ** 2)

    
    return result

#7
def replace_last_element(lst, new_lst):
    
    lst.pop()

    
    lst.extend(new_lst)

    
    return lst
#8
def concatenate_dict(a, b):
    
    a.update(b)
    return a

#9
def create_dict(n):
    
    result = {}

    for i in range(1, n + 1):
        result[i] = i ** 2

    
    return result

#10
def convert_to_list_and_tuple(s):
    # Split the string into a list of strings
    lst = s.split(',')

    # Create a tuple from the list
    tup = tuple(lst)

    # Return both the list and the tuple
    return lst, tup

s = input("Enter a sequence of comma-separated numbers: ")
lst, tup = convert_to_list_and_tuple(s)
print(lst) 
print(tup)  



#1
string = "Hello World"

uppercase_chars = [char for char in string if char.isupper()]

print("Uppercase characters:", uppercase_chars)
#2
students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']


pairs = zip(students, subjects)


dictionary = {student: subject for student, subject in pairs}

print(dictionary)

#3
def reverse_string(string):
    
    for i in range(len(string)-1, -1, -1):
       
        yield string[i]


input_string = "Consultadd Training"

output_string = ''.join(reverse_string(input_string))

print(output_string)

#5

def greeting_decorator(func):
    def wrapper():
        print("Hello,")
        func()
        print("Nice to meet you!")
    return wrapper


def say_name():
    print("My name is Alice.")

say_name = greeting_decorator(say_name)

say_name()




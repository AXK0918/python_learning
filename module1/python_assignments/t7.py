#1
import math

C = 50
H = 30


def calculate_Q(D):
    
    values = D.split(',')
    
    results = []
    for value in values:
        Q = round(math.sqrt((2 * C * int(value)) / H))
        results.append(Q)
    
    return ','.join(str(result) for result in results)

D = input("Enter values for D (comma-separated): ")
result = calculate_Q(D)

print("Result: " + result)

#2
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

#3

class FindTriplets:
    def __init__(self, arr):
        self.arr = arr

    def find_triplets(self):
        n = len(self.arr)
        found = False
        result = []

        
        self.arr.sort()

        
        for i in range(n - 2):
            
            left = i + 1
            right = n - 1

            
            while left < right:
                
                if self.arr[i] + self.arr[left] + self.arr[right] == 0:
                    result.append([self.arr[i], self.arr[left], self.arr[right]])
                    left += 1
                    right -= 1
                    found = True
                
                elif self.arr[i] + self.arr[left] + self.arr[right] < 0:
                    left += 1
                
                else:
                    right -= 1

        
        if not found:
            result.append("No triplets found")

        return result

#4
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, t1, t2):
        self.hours = t1.hours + t2.hours
        self.minutes = t1.minutes + t2.minutes
        if self.minutes >= 60:
            self.hours += 1
            self.minutes -= 60

    def displayTime(self):
        print("Time is", self.hours, "hours and", self.minutes, "minutes.")

    def displayMinute(self):
        print("Total minutes in the time is:", (self.hours * 60) + self.minutes)

#5
class Person:
    def __init__(self, age):
        if age < 0:
            self.age = 0
            print("Age is not valid, setting age to 0")
        else:
            self.age = age

    def yearPasses(self, num_years):
        self.age += num_years

    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif self.age >= 13 and self.age <= 19:
            print("You are a teenager.")
        else:
            print("You are old.")

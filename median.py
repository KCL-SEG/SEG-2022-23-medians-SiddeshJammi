"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort()
print(numbers)
n = len(numbers)

if (n % 2) == 0: 
    n1 = numbers[int(n/2)-1]
    print(n1)
    n2 = n1 + 1
    median = (n1+n2)/2
    print(n2)
    print("the median for the list of numbers is: ",median)

elif (n % 2) == 1:
    median = numbers[int((n-1)/2)]
    print(median)

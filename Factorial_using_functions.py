#This program will find out the factorial of the given number. Recursion concept is used here.
def fact(number):
    if number==1 or number==0:
        return 1
    else:
        factorial=number*fact(number-1)
        return factorial 
number=int(input("Enter a number: "))
if number<0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"the factorial of {number} is {fact(number)}")

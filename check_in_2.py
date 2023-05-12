"Check In 2"
from main import get_message

print()
print()
print("1. Greet The Person Based On The Time Of Day")
print()
A = get_message()
print("   {A}")
print()
print()
print(
    "2. Write a probram to tell someone if there eligible to vote based on their age."
)
print()
A = "0"
input("   What is your age : ")
print()
while not A.isnumeric:
    print("   Invalid Age")
    print("   Please Try Again")
    print()
    input("   What is your age : ")
    print()
if int(A) >= 18:
    print("   You Are Elgible To Vote!")
else:
    print("   You Are NOT Elgible To Vote!")
print()
print()
print("3. Enter a whole number")
print()
A = "0"
A = input("   Enter a whole number : ")
print()
while not A.isnumeric():
    print("   Invalid Number")
    print("   Please Try Again")
    print()
    A = input("   Enter a whole number : ")
print()
if int(A) % 2 == 1:
    print("   You Entered An Odd Number")
else:
    print("   You Entered An Even Number")

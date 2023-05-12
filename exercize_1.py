"Exercise 1"
print()
print()
print("1. Add the numbers for your birthday and birth month.")
print("   Find that number times itself seven times.")
A, B = "A", "A"
while not A.isnumeric() or not B.isnumeric():
    print()
    A, B = input(
        "   Please enter your birth day, then enter your birth month : "
    ).split()
    if not A.isnumeric() and not B.isnumeric():
        print()
        print(f"   {A} and {B} were not valid numbers")
        print("   Please Try Again")
    elif not A.isnumeric():
        print()
        print(f"   {A} was not a valid number")
        print("   Please Try Again")
    else:
        print()
        print(f"   {B} was not a valid number")
        print("   Please Try Again")
print()
print("   Added :", int(A) + int(B))
print()
print("   Added and to the power 0f 7:", (int(A) + int(B)) ** 7)
print()
print()
print("2. What is the remainder when 5 to the eleventh power is divided by 121?")
print()
print("  ", (5 ^ 11) % 121)
print()
print()
print("3. The square root is the 0.5 power.")
print(
    "   Make a variable to hold 7*9*11*13*15 and then find the square root of that number."
)
print()
A = 7 * 9 * 11 * 13 * 15
print("  ", 7 * 9 * 11 * 13 * 15)
print()
print("  ", A**0.5)
print()
print()
print("4. Ask a person for their name")
print()
A = input("   What is your name : ")
print()
print()
print("5. Greet them: 'Hello, _____'")
print()
print(f"   Hello, {A}")
print()
print("6. Ask a person how old they are")
print()
A = "a"
A = input("   How old are you : ")
while not A.isnumeric:
    print(
        """
 
	Invalid Age
 	Please Try Again
  
	"""
    )
    A = input("   How old are you : ")
B = int(A) + 5
print()
print()
print("7. Tell them 'You are ___ years old now and in five years you will be ____'")
print()
print(f"You are {A} years old now and in five years you will be {B}")
print()
print()
print("8. Ask for two numbers and tell what you get when you multiply them.")
A, B = "a", "b"
while not A.isnumeric() or not B.isnumeric():
    print()
    A, B = input("Please enter 2 numbers : ").split()
    if not A.isnumeric() and not B.isnumeric():
        print()
        print(f"   {A} and {B} were not valid numbers")
        print("   Please Try Again")
    elif not A.isnumeric():
        print()
        print(f"   {A} was not a valid number")
        print("   Please Try Again")
    else:
        print()
        print(f"   {B} was not a valid number")
        print("   Please Try Again")
print()
C = int(A) * int(B)
print("   Multiplied :", C)

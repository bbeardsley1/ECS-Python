"Exercise 3"
print(
    """

Day 3 Practice

"""
)
A = int(input("How many miles did you run yesterday : "))
print()
A += int(input("How many miles did you run today : "))
print(
    f"""
You have ran {A} miles so far.

"""
)
if input("Are you a student(y/n) : ") == "y":
    A = 9 / 10
else:
    A = 1
print()
A = A * int(input("What is the price of the sticker : "))
print(
    f"""
${A} please

Thank You!


You have $100 left
"""
)
A = 100
if input("Would you like to buy a shirt(y/n) : ") == "y":
    A -= 20
print()
if input("Would you like to buy pants(y/n) : ") == "y":
    A -= 45
print(
    """
You have ${A} left.

"""
)
A = input("Did you bring a lunch(y/n) : ")
print()
B = input("Did you bring a Snack(y/n) : ")
print()
if A == "y":
    if B == "y":
        print("Enjoy your lunch and snack.")
    else:
        print("Enjoy your lunch.")
elif B == "y":
    print("Enjoy your snack.")
else:
    print("Hope your not hungry.")

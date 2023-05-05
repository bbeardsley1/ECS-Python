"Day 2 Practice"
print()
print()
print("1. Ask how many dollars a person has.")
print("   If that is more than 50 prints 'that is a lot of money'.")
print("   Otherwise print 'my brother has that much'")
print()
a = input("   How much money do you have?(dollars) : ")
while not a.isnumeric:
    print()
    print("   Invalid Number")
    print("   Please Try Again")
    print()
    a = input("   How much money do you have?(dollars) : ")
print()
if int(a) > 50:
    print("   that is a lot of money")
else:
    print("   my brother has that much")
print()
print()
print("2. Ask what a person's favorite color is.")
print("   If that color is blue, print 'I like blue too'.")
print("   Otherwise print 'My favorite color is blue'")
print()
A = input("   What is your favorite color : ")
print()
if A == "blue" or A == "Blue":
    print("   I like blue too")
else:
    print("   My favorite color is blue")
print()
print()
print("3. Ask what a person's name is and how old they are.")
print("   When the person gives an age more than 25, print 'NAME is old'.")
print("   Otherwise print 'NAME is AGE years old'.")
print()
A, B = input("   Enter your name and age : ").split()
while not B.isnumeric:
    print()
    print("   Invalid Age")
    print("   Please Try Again")
    print()
    B = input("   What Is Your Age : ")
print()
if int(B) > 25:
    print(f"   {A} is old")
else:
    print(f"   {A} is {B} years old")
print()
print()
print("4. ATM. The bank ATM starts with $1000 in it.")
print("   Ask the person how many dollars they want to withdraw.")
print("   If they want more than 600, print 'Sorry, the daily limit is $600.'")
print("   Otherwise print 'Here is your money',")
print("   and then subtract the amount they got from how much the ATM contains.")
print("   At the end, print 'Money left in ATM: $_____'.")
print()
A = input("   How many dollars they want to withdraw : ")
while not a.isnumeric:
    print()
    print("   Invalid Number")
    print("   Please Try Again")
    print()
    A = input("   How many dollars they want to withdraw : ")
if int(A) > 600:
    A = 600
    print()
    print("   Sorry, the daily limit is $600.")
print()
print("   Here is your money")
print()
A = 1000 - int(A)
print(f"   Money left in ATM: ${A}.")
print()
print()
print("5. The computer starts out with $5.")
print("   Have it ask your name.")
print("   Then ask 'Hey NAME, can I borrow some money'.")
print("   If it is talking to 'Doc Mo' then give it $20 more dollars.")
print("   If it is talking to '(some other name)' give it $10.")
print("   If it is talking to you, make up a number to give it.")
print("   At the end it should say 'Thanks. Now I have $_____'.")
A = 5
print()
B = input("   Hello, what is your name : ")
print(
    f"""
    Hey {B}, can I borrow money from you : yes
"""
)
if B == "Doc Mo":
    A += 20
elif B == "bbeardsley":
    A += input("   How much money can I have : ")
    print()
else:
    A += 10
print(f"   Thanks. Now I have ${a}")
print(
    """
  
6.  It is 8:45pm and Sam is tired but still has homework to do. Sam's plan is to sleep for a while, then get up and do the homework. Sam is too tired to figure out the time to 
    set the alarm clock, so needs you to write a Python program that asks how many hours and minutes of sleep Sam needs, and then prints out the time to set the alarm clock. 

"""
)
A, B = input("How many hours and minutes of sleep do you need : ").split()
A = int(A) + 8
B = int(B) + 45
C = "PM"
while int(B) >= 60:
    A = int(A) + 1
    B = int(B) - 60

while int(A) >= 12:
    A = int(A) - 12
    if C == "PM":
        C = "AM"
    else:
        C = "PM"
if int(A) == 0:
    A = 12
if int(B) < 10:
    B = (str(0), str(B))
    B = "".join(B)
print(
    """
	Sam should set his alarm clock for {A}:{B} {C}"""
)

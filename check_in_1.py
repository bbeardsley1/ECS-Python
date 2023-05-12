"Check in 1"
print()
print()
print("1. Hmm?")
print()
a = input("   What is your name : ")
print()
print()
print("2. Greet them: 'Hello, _____'")
print()
print("   Hello,", a)
print()
print()
print("3. Ask users for their favorite two numbers.")
print()
a, b = "a", "b"
while not a.isnumeric() or not b.isnumeric():
    print()
    a, b = input("Please enter 2 numbers : ").split()
    if not a.isnumeric() and not b.isnumeric():
        print()
        print(f"   {a} and {b} were not valid numbers")
        print("   Please Try Again")
    elif not a.isnumeric():
        print()
        print(f"   {a} was not a valid number")
        print("   Please Try Again")
    else:
        print()
        print(f"   {b} was not a valid number")
        print("   Please Try Again")
print()
print()
print(
    "4. Create a variable with the user's two numbers added and multiplied itself once."
)
C = int(a) + int(b)
D = C**2
print()
print()
print("5. Print --> Your two number picks were __ and __.")
print("   If you add those numbers up, it would be __.")
print("   If you multiply that by itself, it would be __.")
print()
print(f"   Your two number picks were {a} and{b}.")
print(f"   If you add those numbers up, it would be {C}.")
print(f"   If you multiply that by itself, it would be {D}.")

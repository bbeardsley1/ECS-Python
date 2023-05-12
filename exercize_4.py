"Exercise 4"
A = ""
print(
    """
"""
)
while A != "⠀":
    A = input("Enter The Password : ")
print(
    """
Welcome"""
)
while A <= 500:
    print()
    A = 10 * int(input("Enter a number : "))
    print()
    print(A)
print()
A = int(input("How much money do you have : "))
while A >= 10:
    print()
    A -= int(input("How much money would you like to spend : "))
    print(
        f"""
    You have ${A} Left"""
    )
print()
B = A = int(input("What number should I start counting at : "))
print(
    f"""
{B}"""
)
A += 20 - (A % 20)
while B != A:
    B += 1
    print(B)
print(
    """
Complete"""
)

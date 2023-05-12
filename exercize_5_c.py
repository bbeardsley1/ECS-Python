"Exercise 5C"
A = 100
B = 0
C = 0
print()
while A > B:
    print()
    B = int(input("Enter A Number :"))
    C += 1
    if A > B + 20:
        print(
            """
        Far Away..."""
        )
    elif A > B + 5:
        print(
            """
        Getting Closer..."""
        )
    elif A > B:
        print(
            """
        Very Close..."""
        )
if A == B:
    print(
        """
You Win!"""
    )
else:
    print(
        """
To High!
Game Over"""
    )
print(
    f"""
You Guessed {C} Times
Thank You for playing!"""
)

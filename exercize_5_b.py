"Exercise 5B"
print(
    """
"""
)
A, B = input("What is your name, and how much money do you have".split())
print(
    f"""
Hello {A}"""
)
if int(B) >= 20:
    print()
    if input("Can I borrow $20(y/n) : ") == "y":
        print(
            """
Thank You!"""
        )
        B -= 20
print(
    f"""
You now have ${B}"""
)

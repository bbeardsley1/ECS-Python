"Check In 3"
print(
    """

1. 	Repeat the questions until you have successfully studied more than 5 times
	Ask if they have studied
	If they say no: (Make sure the capital “N” or lowercase “n” does not affect the code)
	tell them they have to start studying soon.
	If they say yes: (Make sure the capital “Y” or lowercase “y” does not affect the code)
	Print the number of times they have studied so far.
	Ask them how many times they have studied now.
	Hint: create an equation to add the number of times they studied. The variable will be constantly checked in the while loop.
	Once they have studied more than 5 times, you can stop repeating the questions and say, “Congratulations, you are going to kill your exam!”
"""
)
A = "n"
B = 0
while 5 > int(B):
    print("    Type y or n in your response")
    A = input("    Have you studied : ")
    if A == "y" or A == "Y":
        print(
            f"""
    You have studied {B} times last time
        """
        )
        B += int(input("    How many times have you studied since then : "))
    else:
        print(
            """
    study"""
        )
print(
    """
	go take the exam now"""
)

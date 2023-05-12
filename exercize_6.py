"Exercise 6"
import random

print("""""")

# Problem1
A = 0
while A < 5:
    num = random.randint(10, 20)
    print(num)
    A += 1

# Problem2
A = random.randint(1, 5)
B = 0

while B != A:
    B = int(input("B a random number 1 to 5 --> "))

print("You got it!!")

# Problem3a
flip = random.randint(1, 2)
if flip == 1:
    print("You landed on heads")
else:
    print("You landed on tails")

# Problem3b
flipA = int(input("How many flips would you like? "))
while flipA > 0:
    flipA -= 1
    flip = random.randint(1, 2)
    if flip == 1:
        print("You landed on heads")
    else:
        print("You landed on tails")

# Problem4
fake = random.randint(1, 100)
if fake >= 1 and fake <= 45:
    print("heads")

elif fake >= 46 and fake <= 90:
    print("tails")

elif fake >= 91 and fake <= 100:
    print("side??")

# Problem5
C = 100
chance = random.randint(1, 10)
while C > 75:
    if chance >= 1 and chance <= 4:
        C += 10
        print("You've won $10. Now you have: $", C)
    if chance >= 5 and chance <= 9:
        C -= 9
        print("You've lost $9. Now you have: $", C)
    else:
        C += 10
        print("You've won $10. Now you have: $", C)
# Problem6
A = 6
B = 0
C = 0
while B != A and C < 3:
    if B == A:
        print("Noice")

    elif B == A - 1 or B == A + 1:
        print("close")

    elif B >= A - 3 or B <= A + 3:
        print("gettign warmer")

    else:
        print("Try Again")

"Review 1"


def randint(z_z, y_y):
    "Return random integer in range [a, b], including both end points."
    return y_y + randbelow(z_z - y_y + 1)


def randbelow(o_o):
    "Return a random int in the range [0,n).  Raises ValueError if n<=0."
    if o_o <= 0:
        raise ValueError
    k_k = o_o.bit_length()
    numbytes = (k_k + 7) // 8
    while True:
        r_r = int.from_bytes(random_bytes(numbytes), "big")
        r_r >>= numbytes * 8 - k_k
        if r_r < o_o:
            return r_r


def random_bytes(n_n):
    "Return n random bytes"
    with open("/dev/urandom", "rb") as file:
        return file.read(n_n)


# Problem1
A = 0
random = int(input("Give random number"))
while A < 3:
    print(random)
    A += 1

# Problem2
name = input("What is your name : ")
year = int(input("What year were you born : "))
print("Hello", name, "you are ", 2023 - year, "years old in 2023")

# Problem3
month = int(input("What month is your birthday(year) : "))
if month <= 2 or month == 12:
    print("Winter")

elif month <= 5:
    print("Spring")

elif month <= 8:
    print("Summer")

else:
    print("Fall")

B = 150
ask = input("Would you like to buy a gucci plastic bag : ")

if ask == "yes" or ask == "Yes":
    B = B - 102
elif ask == "no" or ask == "No":
    B = B - 40

print("You have $", B)
# Problem 4
D = 150
if input("Would you like to buy a bag : ") == "yes":
    D -= 102
else:
    print("fee")
    D -= 40
print(f"Money left ${D}")
# Problem 5

C = 0
ask = int(input("How many times would you like to print? "))

while C < ask:
    print("Today's going to be a good day!")
    C += 1
# Problem6
E = 6
F = 0
G = 0
while F != E and G < 3:
    if F == E:
        print("Noice")

    elif F <= E - 1 or F >= E + 1:
        print("close")

    elif F <= E - 3 or F >= E + 3:
        print("gettign warmer")

    else:
        print("Try Again")
# Problem 7
A = 10
B = 10
while C > 0:
    input("would you like to fight : ")
    C = randint(1, 100)
    if C <= 35:
        B -= 2
    elif C <= 70:
        A -= 3
    else:
        A += 1

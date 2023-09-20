import random

Capitals = "QAZWSXEDCRFVTGBYHNUJMIKOLP"
smalls = "qazwsxedcrfvtgbyhnujmikolp"
numbers = "1234567890"
Symbols = "!@#$%^&*-=+?/"
length = int(input("Enter The length : "))
password = " "
length = length/3
length = int(length)
for a in range (length):
    password+=random.choice(Capitals)
    password+=random.choice(smalls)
    password+=random.choice(Symbols)
    password+=random.choice(numbers)
print(password)
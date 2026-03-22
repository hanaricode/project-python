import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
dice3 = random.randint(1, 6)

def dieRoll():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    return dice1, dice2, dice3

dieRoll()
print(f"{dice1}, {dice2}, {dice3}")
dieRoll()
print(f"{dice1}, {dice2}, {dice3}")

-----------------------------------------

# mendapatkan nomor random
import random
print(f"Random number: {random.randint(1, 100)}")

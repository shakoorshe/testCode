import random
x = random.randint(1,100)
y = int(input("Pick a number 1-100: \n"))
if x > y:
    print("You should have guessed higher")
    print("The number was: " + str(x))
elif x < y:
    print("You guessed too high")
    print("The number was: " + str(x))
else:
    print("You did it!")
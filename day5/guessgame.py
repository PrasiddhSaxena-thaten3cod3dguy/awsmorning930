from random import randint

computernum=randint(1, 50)

print(computernum)

chance=1

while chance <= 5:
    humanguess=int(input("Ener your guess: "))
    if computernum == humanguess:
        print(f"You Win with {5-chance} remaining ")
    elif computernum > humanguess:
           print("Try Higher")
    else:
        print("Try Lower")

    chance = chance + 1 # chance += 1
    
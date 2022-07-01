import random

print("\nWelcome to number guessing game.")
num = random.randint(1, 100)

gnum = 0
# print(num)

print("Random Number Generated...")
print("You Have 5 Guesses..\n")
try:
    for i in range(1, 6):
        if gnum < num:
            gnum = int(input("Choice number " + str(i) + ", enter a greater number:"))
        elif gnum > num:
            gnum = int(input("Choice number " + str(i) + ", enter a smaller number:"))
        if gnum == num:
            print("\nCongo You Guessed in " + str(i) + " Turns.\n\t\t... GAME OVER ...")
            break
    if gnum != num:
        print("\nYou did not find the number it was:" + str(num)+ "\n\t\t... GAME OVER ...")
except Exception as e:
    print("\nAn Error Occurred ")
    print(e)

import os
import random

os.system('cls')

print("Welcome to kuku")
print("by Airlex")

def ReviewTable(a, b):
    while True:
        n1 = random.randint(a,b)
        n2 = random.randint(a,b)

        user_answer = input(f"{n1}*{n2} = ")

        if (user_answer == "x"):
            break

        try:
            if (int(user_answer) == n1 * n2):
                print("correct")
            else:
                print("incorrect")
        except:
            print("invalid input")

    print("see you soon!")

ReviewTable(1, 10)

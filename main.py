import os
import random

os.system('cls')

print("Welcome to kuku")
print("by Airlex")

def SelectTable(string):
    string = string.replace(" ", "")
    separator = ","
    tables = list(string.split(separator))
    int_tables = [int(element) for element in tables]

    return int_tables

def ReviewTable(tables):
    point = 0
    multiplicationCount = 0
    while True:
        n1 = random.randint(tables[0],len(tables))
        n2 = random.randint(tables[0],len(tables))

        user_answer = input(f"{n1}*{n2} = ")

        if (user_answer == "x"):
            break

        multiplicationCount += 1

        try:
            if (int(user_answer) == n1 * n2):
                print("correct")
                point += 1
            else:
                print("incorrect")
        except:
            print("invalid input")

    print(f"Your score: {point}/{multiplicationCount}")
    print("see you soon!")

user_input = input("Enter your multiplication tables : ")

ReviewTable(SelectTable(user_input))

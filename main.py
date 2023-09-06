import os
import random
import time
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

os.system('cls')
colorama_init()

print(f"{Fore.GREEN}Welcome to kuku{Style.RESET_ALL}")
print(f"by {Fore.MAGENTA}Airlex{Style.RESET_ALL}")
print("")

def SelectTable(string):
    string = string.replace(" ", "")
    separator = ","
    tables = list(string.split(separator))
    int_tables = [int(element) for element in tables]

    return int_tables

def ReviewTable(tables):
    point = 0
    multiplicationCount = 0
    start_time = time.time()

    while True:
        n1 = random.randint(tables[0],len(tables))
        n2 = random.randint(tables[0],len(tables))

        user_answer = input(f"{n1}*{n2} = ")

        if (user_answer == "x"):
            break

        multiplicationCount += 1

        try:
            if (int(user_answer) == n1 * n2):
                print(f"{Fore.GREEN}correct{Style.RESET_ALL}")
                point += 1
            else:
                print(f"{Fore.RED}incorrect{Style.RESET_ALL}")
        except:
            print(f"{Fore.RED}invalid input{Style.RESET_ALL}")

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"{Fore.CYAN}Your score: {point}/{multiplicationCount}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Time : {round(elapsed_time, 3)} seconds{Style.RESET_ALL}")
    print("See you soon!")

user_input = input(f"{Fore.CYAN}Enter your multiplication tables : {Style.RESET_ALL}")

try:
    ReviewTable(SelectTable(user_input))
except:
    print("See you soon!")
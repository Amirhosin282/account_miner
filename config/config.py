try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.service import Service
    from time import sleep
    from colorama import Fore
    import sys
    import os
    from pyfiglet import figlet_format
    from rainbowtext import text
    import platform
    from random_word import RandomWords
    from datetime import datetime
    import random
except:
    print ("error!, You don't have the required libraries. install from requirment or active virtual envirment (for linux users) - recommended versions : python3.11.* and selenium 4.10.0")
    exit()

def cl():
    if platform.system() == 'Linux':
        return 'clear'
    elif platform.system() == 'Windows':
        return 'cls'

# get real date
now = datetime.now()
real_date = now.strftime("%Y-%m-%d")

def real_time():
    # get real time
    time = f"{datetime.now().hour:02d} : {datetime.now().minute:02d} : {datetime.now().second:02d}"
    return time

if __name__ == '__main__': # sey to user
    os.system(cl())
    print(Fore.RED, 'run main.py, this is not main file ')
    sleep(5)
    sys.exit()


line = "___________________________________________________________________________________________                                                                                   "


def view(a, b): # app banner

    os.system(cl())

    print(Fore.GREEN)
    print(b)

    print(text(figlet_format("Instagram Account Miner", font="slant")))

    print(Fore.BLUE)

    print(Fore.YELLOW)
    print("_________________________________________________________________                                                                                             ")

    print(Fore.RED,'    date time',Fore.GREEN, f"{a} - {b}")
    print(Fore.RED,'    github',Fore.GREEN,' github.com/amirhosin282')

    print(Fore.RED,'    by',Fore.BLUE,' amirhosin282')

    print(Fore.WHITE)

    print(Fore.YELLOW)
    print("_________________________________________________________________                                                                                             ") 

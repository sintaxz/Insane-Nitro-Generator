import os
import ctypes
import requests
import random
import string
import time
print("""


 /$$$$$$ /$$   /$$  /$$$$$$   /$$$$$$  /$$   /$$ /$$$$$$$$        /$$$$$$  /$$$$$$$$ /$$   /$$
|_  $$_/| $$$ | $$ /$$__  $$ /$$__  $$| $$$ | $$| $$_____/       /$$__  $$| $$_____/| $$$ | $$
  | $$  | $$$$| $$| $$  \__/| $$  \ $$| $$$$| $$| $$            | $$  \__/| $$      | $$$$| $$
  | $$  | $$ $$ $$|  $$$$$$ | $$$$$$$$| $$ $$ $$| $$$$$         | $$ /$$$$| $$$$$   | $$ $$ $$
  | $$  | $$  $$$$ \____  $$| $$__  $$| $$  $$$$| $$__/         | $$|_  $$| $$__/   | $$  $$$$
  | $$  | $$\  $$$ /$$  \ $$| $$  | $$| $$\  $$$| $$            | $$  \ $$| $$      | $$\  $$$
 /$$$$$$| $$ \  $$|  $$$$$$/| $$  | $$| $$ \  $$| $$$$$$$$      |  $$$$$$/| $$$$$$$$| $$ \  $$
|______/|__/  \__/ \______/ |__/  |__/|__/  \__/|________/       \______/ |________/|__/  \__/
                        |___/                                
╔═══════════════════════╦══════════════════════════╦═══════════════════════╗
║  Dev : .Mystic#1020   ║  Info  : Nitro Generator ║  Programm  : Python   ║
╚═══════════════════════╩══════════════════════════╩═══════════════════════╝



""")
time.sleep(0.1)
print("INSANE GENERATOR")
time.sleep(0.1)
print("FAST AND EASY FOR USE NITRO GENERATOR .\n")
time.sleep(0.1)

num = int(input('Input How Many Codes to Generate and Check: '))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("Please wait ...")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"Generated {num} codes | Time taken: {time.time() - start}\n")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f" Valid | {nitro} ")
            break
        else:
            print(f" Invalid | {nitro} ")


print("Discord : https://discord.gg/Y8HEva63Hj\n")

time.sleep(0.2)

input("\nCodes generated !! If Valide codes.txt is empty retry to gen ")


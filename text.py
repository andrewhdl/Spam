import pyautogui, time
from time import sleep
import colorama
from colorama import Fore, Back, Style
import requests
from requests.sessions import session


colorama.init()

session = requests.session()
print(Fore.GREEN + """ 
  _________                      __________        __         ____ 
 /   _____/__________    _____   \______   \ _____/  |____  _/_   |
 \_____  \\____ \__  \  /     \    |    |  _//  _ \   __\  \/ /|   |
 /        \  |_> > __ \|  Y Y  \  |    |   (  <_> )  |  \   / |   |
/_______  /   __(____  /__|_|  /  |______  /\____/|__|   \_/  |___|
        \/|__|       \/      \/          \/                        
""")
print(Fore.YELLOW+"Made BY StevenBlade\n\n\n")

input("[+]Press ENTER to continue.")
sleep(0.1)
print("[-]Please wait for 5s...")
sleep(5)
print("[+]Bot is ready!!!")
sleep(2)
print("[+]Open massenger,telegram,... or where you wanna spam!")
sleep(3)
input("[+]Press ENTER when you already open!")
sleep(5)
input("[+]Press ENTER to start bot")
sleep(1)
print(Fore.BLUE+"[-]Please wait...")
sleep(1)
print("[-]Bot is start in 5s")

time.sleep(5)
print(Fore.GREEN+"[!]Bot is starting")
f=open("tset.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
 
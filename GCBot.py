#!/usr/bin/python3
# Currntly running on Windows so no need for the #! line however I left it for Linux.
# Added a feature to check the current time so that we don't just request the page 24 hours/day. Take a load off the server and maybe avoid detection a little.
import requests
import re
import os
import time
import random as rand
from colorama import Fore, Back, Style, init
init() # as far as I know this is only required for Windows.
#

now = ""

print("Inventory Informer bot v0.1b by EZKILLs\n")

# Best Buy requires a user agent. We cannot leave this out or we get access denied.
# Added the referer line because script was stopping after a few minutes likely due to the website having anti-bot technology
user_agent = {
        'User-Agent': 'Mozilla/5.0',
        'referer': 'https://store.nvidia.com/'
        }

# Here you should enter the URLs you want to include for the bot. The purchase process is manual so you should be quick.
urls = [
    #Enter URLS separated by commas
    # Top link is just to test the data-button-state statement below.. and it works! :)
    #"https://www.bestbuy.com/site/beats-by-dr-dre-powerbeats-pro-totally-wireless-earphones-lava-red/6397383.p?skuId=6397383",
    "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3070-eagle-8gb-gddr6-pci-express-4-0-graphics-card/6437912.p?skuId=6437912",
    "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-ti-8gb-gddr6x-pci-express-4-0-graphics-card-dark-platinum-and-black/6465789.p?skuId=6465789",
    "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442",
    "https://www.bestbuy.com/site/evga-geforce-rtx-3070-xc3-ultra-gaming-8gb-gddr6-pci-express-4-0-graphics-card-light-hash-rate/6477077.p?skuId=6477077",
    "https://www.bestbuy.com/site/evga-geforce-rtx-3070-xc3-ultra-gaming-8gb-gddr6-pci-express-4-0-graphics-card-light-hash-rate/6479528.p?skuId=6479528",
    "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3070ti-eagle-8gb-gddr6x-pci-express-4-0-graphics-card-black/6467782.p?skuId=6467782"
    ]

# Check to see if we are between 09:00 and 17:00 (may change to 19:00)
def checkTime():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    now = time.strftime("%H:%M:%S")
    if int(hour) > 9 and int(hour) < 19:
        print('Time in range')
        #print(time.strftime('%H'))
        print('Hour: ' + hour + ' Minute: ' + minute)
        return True
    else:
        return False

print(now)
def check(link):
    r = requests.get(link, headers = user_agent)
    # Trying data-button-state="ADD_TO_CART" instead of detecting "Sold Out"
    if not (re.search('data-button-state="ADD_TO_CART"', r.text)): #(re.search('Sold Out', r.text)) or (re.search('Shop Open-Box', r.text)):
        print(Fore.RED + "[!] Out of stock :( -------------------------" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "[+]IN STOCK!!!!! :D Opening browser............." + Style.RESET_ALL)
        while(os.system("\"c:\Program Files\\Mozilla Firefox\\firefox.exe\" " + link)):
            print("Loading")
            time.sleep(rand.randint(250, 1000)/1000)

while True:
    if checkTime():
        for i in range(len(urls)):
            print("Checking : " + Fore.GREEN + urls[i] + Style.RESET_ALL)
            check(urls[i])
            sleepy=rand.randint(1,10)
            print("Sleeping for [[" + Fore.BLUE + str(sleepy) + Style.RESET_ALL +"]] secdonds")
            time.sleep(sleepy)

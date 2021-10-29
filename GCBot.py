#!/usr/bin/python3
# Currntly running on Windows so no need for the #! line however I left it for Linux.
import requests
import re
import os
import time
import random as rand
from colorama import Fore, Back, Style, init
init()
#
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
    "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-ti-8gb-gddr6x-pci-express-4-0-graphics-card-dark-platinum-and-black/6465789.p?skuId=6465789",
    "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442",
    "https://www.bestbuy.com/site/evga-geforce-rtx-3070-xc3-ultra-gaming-8gb-gddr6-pci-express-4-0-graphics-card-light-hash-rate/6477077.p?skuId=6477077",
    "https://www.bestbuy.com/site/evga-geforce-rtx-3070-xc3-ultra-gaming-8gb-gddr6-pci-express-4-0-graphics-card-light-hash-rate/6479528.p?skuId=6479528",
    "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3070ti-eagle-8gb-gddr6x-pci-express-4-0-graphics-card-black/6467782.p?skuId=6467782"
    ]
url = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-ti-8gb-gddr6x-pci-express-4-0-graphics-card-dark-platinum-and-black/6465789.p?skuId=6465789" # Best Buy RTX 3070 Ti link
url2 = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442"    # Best Buy RTX 3070 link



def check(link):
    r = requests.get(link, headers = user_agent)
    if (re.search('Sold Out', r.text)):
        print(Fore.RED + "[!] Out of stock :( -------------------------" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "[+]IN STOCK!!!!! :D Opening browser............." + Style.RESET_ALL)
        while(os.system("\"c:\Program Files\\Mozilla Firefox\\firefox.exe\" " + url)):
            print("Loading")
            time.sleep(rand.randint(250, 1000)/1000)
            exit()

while True:
    for i in range(len(urls)):
        print("Checking : " + Fore.GREEN + urls[i] + Style.RESET_ALL)
        check(urls[i])
        sleepy=rand.randint(1,10)
        print("Sleeping for [[" + Fore.BLUE + str(sleepy) + Style.RESET_ALL +"]] secdonds")
        time.sleep(sleepy)

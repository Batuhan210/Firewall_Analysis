#!/usr/bin/env python

import os

os.system("apt-get install figlet")

os.system("clear")

os.system("figlet FIREWALL")

print("""

Welcome to the firewall analysis 


""")


site = input("Enter an address : ")

os.system("wafw00f " + site)










#!/usr/bin/env python

import pyfiglet
import subprocess
from colorama import Fore

result = pyfiglet.figlet_format("SiTech Security")
print(Fore.YELLOW + result)
print(Fore.RED + "                >>- Mac Address Changing Tool From SiTech Security -<<")
print(Fore.CYAN + "Join with us via Telegram :https://t.me/joinchat/Q8GANUSWgX7er-V13PVUog")
print("Contact me via Telegram :https://t.me/awpsn")
print("Our WebSite :https://sitechsecurity.wordpress.com")
print(Fore.RESET)
interface = input(Fore.GREEN + "interface > ")
new_mac = input(Fore.GREEN + "new MAC > ")
print(Fore.RESET)
print(Fore.RED + "[+] Changing MAC address for " + interface + " to " + new_mac)
print(Fore.RESET)
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
subprocess.call("macchanger -s " + interface, shell=True)
print(Fore.RESET)
print(Fore.BLUE + "[+] MAC Address changed successful.\n[+] Have a nice day!!!")
print(Fore.RESET)

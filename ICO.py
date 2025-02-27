import requests # type: ignore
from colorama import Fore, Style # type: ignore
import os

os.system('cls' if os.name == 'nt' else 'clear')

while True:
        
        print(Fore.MAGENTA)
        
        banner = r"""
           ____ _____ ____  
         |_   _/ ____/ __ \ 
           | || |   | |  | |
           | || |   | |  | |
          _| || |___| |__| |
         |_____\_____\____/ """
        
        print(banner)
        
        print("")
        
        print("A tool to change your PFP or banner on rr!")
        print("Made by 'venzyiskool' on discord :)")
        print("(and 'venzylmao' on github)")
        
        print(Style.RESET_ALL)
        
        print("══════════════════════════════════════════")
        
        print("")
        
        print(f"[{Fore.MAGENTA}1{Style.RESET_ALL}] {Fore.MAGENTA} Change PFP {Style.RESET_ALL}   [{Fore.MAGENTA}2{Style.RESET_ALL}] {Fore.MAGENTA} Change banner {Style.RESET_ALL}")
        print(f"[{Fore.MAGENTA}3{Style.RESET_ALL}] {Fore.MAGENTA} Change to default PFP {Style.RESET_ALL}")
        print(f"[{Fore.MAGENTA}4{Style.RESET_ALL}] {Fore.MAGENTA} Change to default banner {Style.RESET_ALL}")
        print(f"[{Fore.MAGENTA}5{Style.RESET_ALL}] {Fore.MAGENTA} Exit")
        
        print("")

        opt = input("Select an option: ")
        
        print(Style.RESET_ALL)
        
        print("══════════════════════════════════════════")
        
        print(Fore.MAGENTA)
        
        if opt == "1":
            auth = input("              Auth session: ")
            image = input("              Image link: ")
            print("")
            headers = {
                'Authorization': f'Bearer {auth}'
            }
            url = 'https://accounts.rec.net/account/me/profileimage'
            data = {
                'ImageName': image
            }
            r = requests.put(url, headers=headers, data=data)
            os.system('cls' if os.name == 'nt' else 'clear')
            if r.status_code == 200:
                print(f"{Fore.GREEN}PFP successfully changed!")
                input("")
        
        if opt == "2":
            auth = input("              Auth session: ")
            image = input("              Image link: ")
            print("")
            headers = {
                'Authorization': f'Bearer {auth}'
            }
            url = 'https://accounts.rec.net/account/me/bannerimage'
            data = {
                'ImageName': image
            }
            r = requests.put(url, headers=headers, data=data)
            os.system('cls' if os.name == 'nt' else 'clear')
            if r.status_code == 200:
                print(f"{Fore.GREEN}Banner successfully changed!")
                input("")
        
        if opt == "3":
            auth = input("              Auth session: ")
            print("")
            headers = {
                'Authorization': f'Bearer {auth}'
            }
            url = 'https://accounts.rec.net/account/me/profileimage'
            data = {
                'ImageName': ""
            }
            r = requests.put(url, headers=headers, data=data)
            os.system('cls' if os.name == 'nt' else 'clear')
            if r.status_code == 200:
                print(f"{Fore.GREEN}PFP successfully changed!")
                input("")

        if opt == "4":
            auth = input("              Auth session: ")
            print("")
            headers = {
                'Authorization': f'Bearer {auth}'
            }
            url = 'https://accounts.rec.net/account/me/bannerimage'
            data = {
                'ImageName': ""
            }
            r = requests.put(url, headers=headers, data=data)
            os.system('cls' if os.name == 'nt' else 'clear')
            if r.status_code == 200:
                print(f"{Fore.GREEN}Banner successfully changed!")
                input("")
        
        if opt == "5":
             break

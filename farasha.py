"""#####################################################################################################"""
"""#copyright by AymanSec this tool is free and open-source, farasha is automation tool for scaning web#"""
"""#####################################################################################################"""



from  bs4 import BeautifulSoup
import re
import requests
import threading
import argparse
import os, sys, subprocess
from colorama import Fore, init
import logging
from urllib.parse import urljoin
import random

import os
import time

def big_text_animation():
    clear_command = "cls" if os.name == "nt" else "clear"

    big_text = [
        "▄▀▀█▄▄   ▄▀▀▄ ▀▀▄      ▄▀▀█▄   ▄▀▀▄ ▀▀▄  ▄▀▀▄ ▄▀▄  ▄▀▀█▄   ▄▀▀▄ ▀▄  ▄▀▀▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▄▄▄▄  ",
        "▐ ▄▀   █ █   ▀▄ ▄▀     ▐ ▄▀ ▀▄ █   ▀▄ ▄▀ █  █ ▀  █ ▐ ▄▀ ▀▄ █  █ █ █ █ █   ▐ ▐  ▄▀   ▐ █ █    ▌ ",
        "  █▄▄▄▀  ▐     █         █▄▄▄█ ▐     █   ▐  █    █   █▄▄▄█ ▐  █  ▀█    ▀▄     █▄▄▄▄▄  ▐ █      ",
        "  █   █        █        ▄▀   █       █     █    █   ▄▀   █   █   █  ▀▄   █    █    ▌    █      ",
        " ▄▀▄▄▄▀      ▄▀        █   ▄▀      ▄▀    ▄▀   ▄▀   █   ▄▀  ▄▀   █    █▀▀▀    ▄▀▄▄▄▄    ▄▀▄▄▄▄▀ ",
        "█    ▐       █         ▐   ▐       █     █    █    ▐   ▐   █    ▐    ▐       █    ▐   █     ▐  ",
        "▐            ▐                     ▐     ▐    ▐            ▐                 ▐        ▐          "
    ]

    green = "\033[92m"
    reset_color = "\033[0m"  

    width = os.get_terminal_size().columns 
    frames = 150  
    padding = " " * width  

    for frame in range(frames):
        os.system(clear_command)  
        offset = frame % (width + len(big_text[0]))  

        for line_index, line in enumerate(big_text):
            colored_line = (
                green +  
                padding[max(0, width - offset):] + 
                line[max(0, offset - width):] +  
                reset_color
            )
            print(colored_line)
        time.sleep(0.002)  

# big_text_animation()

os.system("cls" if os.name == "nt" else "clear")
    
print(Fore.RED + 
r"""                                            hi there
                        -----------------─────────────────────────────────────────────────────┐
                                 │         ____|                                 |            │
                                 │         |        _` |    __|    _` |    __|   __ \     _` |│
                                 │         __|     (   |   |      (   |  \__ \   | | |   (   |│
                                 │         _|      \__,_|  _|     \__,_|  ____/  _| |_|  \__,_|
                                 └────────────────────────────────────────────────────┘-----------
""")
time.sleep(1)
os.system("cls" if os.name == "nt" else "clear")


init(autoreset=True)

with open("quotes/quotes.txt", "r") as quotes:
     quote = quotes.read().splitlines()
ma9ola = random.choice(quote)     
print(Fore.GREEN + "->", Fore.CYAN + ma9ola)


class wordlist:
    
           
        def wordlist_xss(self):
           
           print(f"{Fore.LIGHTYELLOW_EX}reading wordlist xss...")
           with open("wordlist/xss.txt", 'r',  encoding='utf-8') as xss:
                  wordlist_xss = xss.read()
                  return wordlist_xss
           
        def wordlist_subs(self):
           
            print(f"{Fore.LIGHTMAGENTA_EX}reading wordlist subs...")
            with open("wordlist/subs.txt", "r", encoding='utf-8') as subs:
                subd = subs.read().splitlines()
                return subd
        
        def get_func(self, func_name):
                if hasattr(self, func_name) and callable(getattr(self, func_name)):
                  return getattr(self, func_name)()  
                else:
                   print(f"Function '{func_name}' not found.")
                   return None
       
    
        def __call__(self):    
            print("importing ....")
            

class param_crawler:
    
  
    
        def __init__(self, urls=[]):
          self.visited_urls = []
          self.urls_to_visit = urls

        def download_url(self, url):
            return requests.get(url).text
    
        def get_linked_urls(self, url, html):
            soup = BeautifulSoup(html, 'html.parser')
            for link in soup.find_all('a'):
                path = link.get('href')
                if path and path.startswith('/'):
                    path = urljoin(url, path)
                yield path
    
        def add_url_to_visit(self, url):
            if url not in self.visited_urls and url not in self.urls_to_visit:
                self.urls_to_visit.append(url)
    
        def crawl(self, url):
            html = self.download_url(url)
            for url in self.get_linked_urls(url, html):
                self.add_url_to_visit(url)
    
        def run(self):
            while self.urls_to_visit:
                url = self.urls_to_visit.pop(0)
                logging.info(f'Crawling: {url}')
                try:
                    self.crawl(url)
                except Exception:
                    logging.exception(f'Failed to crawl: {url}')
                finally:
                    self.visited_urls.append(url)



class farasha:
    def __init__(self):
        self.number = int
        pass

    def max_dommains(self, numbers):

        if numbers is int:  
            num = self.number
            for number in numbers:
                
                num.append(numbers)

            return numbers
            
        else:
            print("numbers not other thing!!")

  
    def fuzz_subs(self, target):    
        
        wordlist_instance = wordlist()
       
        subd = wordlist_instance.wordlist_subs()
        xss = wordlist_instance.wordlist_xss()
        

        self.xss_wordlist = xss
        self.subd = subd
        
        self.discoverd_subs = ['']
        print(f"{Fore.CYAN}fuzz subs...")
        if self.discoverd_subs != self.number:

            for subdomains in self.subd:
               
    
                url = f"https://{subdomains}.{target}"
                
                #you should do http after, caus we want also scan local host !!   it's nice to think about everything !! ahh77
                try:    
                      
                   
                   req = requests.get(url)
                  
                except requests.ConnectionError:
                            pass
                except KeyboardInterrupt:
                            subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
                            print(f'{Fore.RED}exite success!')      
                            exit(0)  
    
                
                else:
                    print(f"Discoverd Subs: ", f"{Fore.GREEN}{url}")
    
                    self.discoverd_subs.append(url)
    
                    name_preference = target.replace(".com", "")
                    os.makedirs(os.path.dirname(f"resulte/{name_preference}/subs.txt"), exist_ok=True)
                       
                    out = "\n".join(self.discoverd_subs)
                    with open(f"resulte/{name_preference}/subs.txt", "w") as subs:
                      subs.write(out)
        else:
            print(Fore.LIGHTRED_EX + "progress finish")

#++++++++++++++++++++++++++++++                
#+Ayman M9wd chwya zayd nrza!!+               
#++++++++++++++++++++++++++++++
    

    def xss_finder():       

        pass

    def validat_xss():
        pass

    def match_url(self, url):
        
       
        string_regex = re.compile(r"^((?!-)[A-Za-z0-9-]{1,63}(?<!-)\.)+[A-Za-z]{2,6}$")
        
        if  re.match(string_regex, url):
            
      
            print(f"the target:  \033[31m{url}\033[0m","has been taked with success!!✅✅")
       
        else:
            print("""check your url !! ❌
                  
            ^^^^^^^^^^^^^^^^^^      try delete protocol http[s] and put just the name with domain!!  """)
      

    
    def options(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-X", "--XssScan", help="full scan for found all subs and all dir and fuzz xss as everthing ", action='store_true', required=True)
        parser.add_argument("-u", "--url", help="set url target", required=True)
        parser.add_argument("-N","--number", help="numbers of dommains do you want, 'set max of dommain fuzzing'", required=True)
        args = parser.parse_args()
        

        url = args.url
        
        if url:
           self.match_url(url)
        
        if args.XssScan:
          
           self.fuzz_subs(url)
           
           param_crawler(urls=["https://",url]).run()
        
        if args.number:

            self.max_dommains(args.number)


if __name__ == "__main__":  
    
    try:
      farasha().options()    
    

    except KeyboardInterrupt:
               subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
               print(f'{Fore.RED}exite success!')      
               exit(0)

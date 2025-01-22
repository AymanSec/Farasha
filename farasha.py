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


print(r"""
                -----------------─────────────────────────────────────────────────────┐
                                 │ ____|                                 |            │
                                 │ |        _` |    __|    _` |    __|   __ \     _` |│
                                 │ __|     (   |   |      (   |  \__ \   | | |   (   |│
                                 │_|      \__,_|  _|     \__,_|  ____/  _| |_|  \__,_|│
                                 └────────────────────────────────────────────────────┘-----------by AymanSec
""")

init(autoreset=True)




class wordlist:
    
        def wordlist_xss(self):
            print(f"{Fore.LIGHTYELLOW_EX}reading wordlist...")
        
            with open("wordlist/xss.txt", 'r',  encoding='utf-8') as xss:
               wordlist_xss = xss.read()
               return wordlist_xss
        
        def wordlist_subs(self):
        
            print(f"{Fore.LIGHTMAGENTA_EX}reading wordlist...")
            with open("wordlist/subs.txt", "r", encoding='utf-8') as subs:
               subd = subs.read().splitlines()
               return subd
    

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
         
           
        self.xss_wordlist = wordlist().wordlist_xss()
        self.subd = wordlist().wordlist_subs()

    def fuzz_subs(self, target):    

        self.discoverd_subs = ['']
        print(f"{Fore.CYAN}fuzz subs...")

        for subdomains in self.subd:
            url = f"https://{subdomains}.{target}"

            #you should do http after, caus we want also scan local host !!  
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

#+++++++++++++++++++++                 
#+Ayman M9wd chwya !!+               
#+++++++++++++++++++++
    
    def call_subs(self):
        
       
        pass

    def param_crawler(self):
        pass
    
    def xss_finder():       

        pass

    def validat_xss():
        pass

    def match_url(self, url):
        
       
        string_regex = re.compile(r"^((?!-)[A-Za-z0-9-]{1,63}(?<!-)\.)+[A-Za-z]{2,6}$")
        
        if  re.match(string_regex, url):
            
      
            print(f"the target:\033[31m{url}\033[0m","has been taked with success!!✅✅")
       
        else:
            print("""check your url !! ❌
                  
            ^^^^^^^^^^^^^^^^^^      try delete protocol http[s] and put just the name with domain!!  """)
      
    
    def options(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-X", "--XssScan", help="full scan for found all subs and all dir and fuzz xss as everthing ", action='store_true')
        parser.add_argument("-u", "--url", help="set url target", required=True)
        args = parser.parse_args()
        

        url = args.url
        
        if args.url:
           self.match_url(url)
        
        if args.XssScan:
          
           self.fuzz_subs(url)
           
           param_crawler(urls=["https://",url]).run()



if __name__ == "__main__":  

    try:
      farasha().options()                                             
    except KeyboardInterrupt:
               subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
               print(f'{Fore.RED}exite success!')      
               exit(0)
#"""####################################################################################################"""
####copyright by AymanSec this tool is free and open-source, farasha is automation tool for scaning web was made in 
####Kingdom morocco  ###########################################################################################
#"""####################################################################################################"""




import re
import requests
import threading
import argparse
import os, sys
import colorama

print(r"""
                -----------------─────────────────────────────────────────────────────┐
                                 │ ____|                                 |            │
                                 │ |        _` |    __|    _` |    __|   __ \     _` |│
                                 │ __|     (   |   |      (   |  \__ \   | | |   (   |│
                                 │_|      \__,_|  _|     \__,_|  ____/  _| |_|  \__,_|│
                                 └────────────────────────────────────────────────────┘---------------------------------by AymanSec
""")


class farasha:
    

    discoverd_subs = ['']
    
  

    def __init__(self, wordlist_xss, subd):
       
        self.subd = subd
        self.wordlist_xss = wordlist_xss
        
                                                                                             
        
           
    def fuzz_subs(self, target):
        
        
        for subdomains in self.subd:           
            try:
                   
               url = f"https://{subdomains}.{target}"   
               req = requests.get(url)
               print(req)
            
            except:
                        print(SyntaxError,"error!")
    
        
    def fuzz_dir(self):
        
        pass

    def param_crawler(self):
        pass
    
    def xss_test():
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
        parser.add_argument("-f", "--fullScan", help="full scan for found all subs and all dir and fuzz xss as everthing ", action='store_true')
        parser.add_argument("-q", "--quickScan", help="quick scan is for found dir and do fuzz xss as dir just dir:!", action='store_true')
        parser.add_argument("-u", "--url", help="set url target", required=True)
        args = parser.parse_args()
        

        url = args.url
        
        if args.url:
           self.match_url(url)
        
        if args.fullScan:
           self.fuzz_subs(url)
        
def read_subs():
        with open("Farasha/wordlist/subs.txt", "r", encoding='utf-8') as subs:
           subd = subs.read()
           return subs

def read_xss():
        with open("Farasha/wordlist/xss.txt", 'r',  encoding='utf-8') as xss:
           wordlist_xss = xss.read()
          
           return wordlist_xss

if __name__ == "__main__":  

    farasha(read_xss(), read_subs()).options()

#"""####################################################################################################"""
####copyright by AymanSec this tool is free and open-source, farasha is automation tool for scaning web ###
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


    def read_xss(self):
           
        with open("wordlist/xss.txt", 'r',  encoding='utf-8') as xss:
            self.wordlist_xss = xss.read()
       
    def read_subs(self):
        with open("wordlist/subs.txt", "r", encoding='utf-8') as subs:
            self.subs = subs.read()
    
    def fuzz_subs(self):
        pass

    def fuzz_dir(self):
        
        pass

    def param_crawler(self):
        pass



    def match_url(self, url):
      
       
        string_regex = re.compile(r"^((?!-)[A-Za-z0-9-]{1,63}(?<!-)\.)+[A-Za-z]{2,6}$")
        
        if  re.match(string_regex, url):
            
            target = url
      
            print(f"the target:\033[31m{target}\033[0m","has been taked with success!!✅✅")
       
        else:
            print("""check your url plz!! ❌
                  
            ^^^^^^^^^^^^^^^^^^       """)
      

    def options(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-f", "--fullScan", help="full scan for found all subs and all dir and fuzz xss as everthing ")
        parser.add_argument("-q", "--quickScan", help="quick scan is for found dir and do fuzz xss as dir just dir:!")
        parser.add_argument("-u", "--url", help="set url target", required=True)
        args = parser.parse_args()
        
        if self.match_url(args.url):
            print("good")
        

if __name__ == "__main__":  
    
    farasha().options()
    

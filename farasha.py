#"""####################################################################################################"""
####copyright by AymanSec this tool is free and open-source, farasha is automation tool for scaning web ###
#"""####################################################################################################"""





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
                                 └────────────────────────────────────────────────────┘---------------------------------
""")

#def options():
#    parser = argparse.ArgumentParser()
#    parser.add_argument("")
#    args = parser.parse_args()
#    
#
#options()



class farasha:
    def payloads_xss():
           
        with open("payloads/xss.txt", 'r',  encoding='utf-8') as xss:
                wordlist_xss = xss.read()

    
    def paylood_sql():
         
        with open("payloads/sql.txt", 'r', encoding='utf-8') as sql:
            wordlist_sql = sql.read()
        print(wordlist_sql)
            
    payloads_xss()












#if __name__ == "__main__":
#    main()


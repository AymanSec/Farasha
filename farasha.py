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
r"""                                            Hi, there
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


class authentification:
    def __init__(self):
        self.session = requests.Session()

    def crsf(self, url):

        token_page = self.session.get(url)
        
        token_soup = BeautifulSoup(token_page.content, 'html.parser')
        
        token = token_soup.find('input', {'name': '_csrf'})['value']

    def cookies(self):
        pass 

class param_crawler(authentification):
     
    def __init__(self, url):

        visited_url  = []
    
        req = super().__init__(self.session).get(url)

        soup = BeautifulSoup(req.content, "html.parser").prettify()

        pattern =  re.compile(r'href="([^"]+)"')
        inputs = re.compile(r'input="([^"]+)"')
        password = re.compile(r'password="([^"]+)"')
        emails = re.compile(r'email="([^"]+)"')
        tel = re.compile(r'tel="([^"]+)"')
        telphone = re.compile(r'telphone="([^"]+)"')
        comment = re.compile(r'comment="([^"]+)"')
        commentaire = re.compile(r'commentaire="([^"]+)"')
        id = re.compile(r'id="([^"]+)"')
        file = re.compile(r'file="([^"]+)"')
        number = re.compile(r'number="([^"]+)"')
        submet = re.compile(r'submet="([^"]+)"')     
        form = re.compile(r'form="([^"]+)"')

        rey = re.findall(pattern,  soup)
        input = re.findall(inputs,  soup)
        passwo = re.findall(password,  soup)
        mail = re.findall(emails,  soup)
        telo  = re.findall(tel,  soup)
        teloph = re.findall(telphone,  soup)
        commente = re.findall(comment,  soup)
        commentair = re.findall(commentaire,  soup)
        idd = re.findall(id,  soup)
        filee = re.findall(file,  soup)
        numberee = re.findall(number,  soup)
        submete = re.findall(submet,  soup)
        forme  = re.findall(form,  soup)

        for a in rey:
            print(Fore.RED + "discovred:", a)

            for b in  input:
                print(Fore.RED + "discovred:",b)                                       

                for c in passwo:
                  print(Fore.RED + "discovred:",c)
                    
                  for d in mail: 
                    print(Fore.RED + "discovred:",d)
                    for e in telo:
                        print(Fore.RED + "discovred:",e)
                        for f in teloph:
                            print(Fore.RED + "discovred:",f)
                            for g in commente:
                                print(Fore.RED + "discovred:",g)
                                for i in commentair:
                                    print(Fore.RED + "discovred:",i)
                                    for j in idd:
                                        print(Fore.RED + "discovred:", j)
                                        for k in filee:
                                            print(Fore.RED + "discovred:",k)
                                            for l in numberee:
                                                print(Fore.RED + "discovred:",l)
                                                for m in submet:
                                                    print(Fore.RED + "discovred:",m)
                                                    for n in form:
                                                        print(Fore.RED + "discovred:",n)









class farasha(param_crawler):
    def __init__(self):
        self.number = []
        self.discoverd_subs = []


    def max_dommains(self, numbers):
            if numbers:
                self.number = str("".join(map(str, numbers)))

            else:
                for number in numbers:
                 self.number.append(number)

                 self.number = int("".join(map(str, number)))



    def check_subd_discovred(self):
        a = []

        for i, sub in enumerate(self.discoverd_subs, start=1):

            a.append(i)

        numbers = a[-1]  # mrrna i l a omn a l number bax n9dro n5do acess 3la -1 "last number" a777!! onyhyahay !!
        t3 = threading.Thread(target=lambda: print(Fore.RED + f"𝓼𝓾𝓫𝓭𝓸𝓶𝓪𝓲𝓷:{numbers}/{self.number}."))
        t3.start()
        t3.join()

        if str(len(self.discoverd_subs)) in str(self.number):
              print(Fore.LIGHTRED_EX + "process finish")
              a()
              exit(0)
        else:
            pass


    def fuzz_subs(self, target):

        wordlist_instance = wordlist()

        subd = wordlist_instance.wordlist_subs()
        xss = wordlist_instance.wordlist_xss()



        self.xss_wordlist = xss
        self.subd = subd

        print(f"{Fore.CYAN}fuzz subs...")



        for subdomains in self.subd:

            url = f"https://{subdomains}.{target}"

            #you should do http after, caus we want also scan local host !!   it's nice to think about everything !! ahh77
            try:

                req = requests.get(url)
                req = super().__init__(self.session).get(url)

            except requests.ConnectionError:
                        pass
            except KeyboardInterrupt:
                        subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
                        print(f'{Fore.RED}exite success!!!')

                        exit(0)
            else:
                print(f"Discoverd Subs: ", f"{Fore.GREEN}{url}")

                self.discoverd_subs.append(url)

                name_preference = target.replace(".com", "")

                t2 = threading.Thread(target=self.check_subd_discovred())
                t2.start()
                t2.join()

                os.makedirs(os.path.dirname(f"resulte/{name_preference}/subs.txt"), exist_ok=True)

                out = "\n".join(self.discoverd_subs)


                with open(f"resulte/{name_preference}/subs.txt", "w") as subs:
                  subs.write(out.strip())
        


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
        parser.add_argument("-N","--number", help="numbers of dommains do you want, 'set max for dommain fuzzing'", required=True)
        args = parser.parse_args()


        url = args.url


        if url:
           self.match_url(url)

        if args.number == "max":
            self.max_dommains(args.number)


        else:
            if args.number.isdigit() :

             self.max_dommains(args.number)

            else:
                print(Fore.GREEN + "only number azbi or max option!!")
                exit(0)

        if args.XssScan:

           self.fuzz_subs(url)

           param_crawler(urls=["https://",url]).run()


if __name__ == "__main__":

    try:

      farasha().options()
    
      
    #   farasha().options()
      param_crawler("https://youtube.com/")

      

    except KeyboardInterrupt:
               subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
               print(f'{Fore.RED}exite success!')
               exit(0)
               exit(0)

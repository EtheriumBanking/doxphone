# -*- coding: UTF-8
import requests
import pyfiglet
import os
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
os.system("clear")
baner= pyfiglet.figlet_format("DoxPhone")
print(GREEN+baner)
print(YELLOW+"\By: EtheriumBanking")
print(GREEN+"escribe el numero de telefono junto\ncon el prefijo, ejemplo: +523313002435\n")
# Información

api_key = '71c9a91b73291f84764eda1c5ccba175'
number = int(input(GREEN+"Numero de telefono: "+RESET))

data = requests.get("http://apilayer.net/api/validate?access_key=%s&number=%s&country_code&format=1" % (api_key, number))

for key, value in data.json().items():

    print("%s: %s" % (key, value))
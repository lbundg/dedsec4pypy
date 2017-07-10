import os
import time
import datetime
import readline
import logging

from  config.glob import *
from logo.logo import bcolors

gtarget = 0
gport = 0
ghash = 0
gwordlist = 0
guser = 0
gap = 0
ginterface = 0
ip = ''
iprange = ''
modules = 0
show = ''

def Set_ip():
  i = 0
  count = 0
  if ip != 'NILL':
    while True:
      iprange += ip[i]
      i += 1
      if (ip[i] == '.'):
        count += 1
      if (count == 3):
       break
    gap = iprange + '.1'
    iprange += '.0/24'

LOG_FILENAME = '/tmp/completer.log'
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG,
                    )

command_list = [ 'exit' ]
sh_list = [ '.closes the programm']

def list_sp_files():
    dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(dir, 'pymodule')
    counter = 0
    for filename in os.listdir(path):
        print filename[:-3]
        counter += 1
        command_list.append(filename[:-3])
    return counter
time_now = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
modules = list_sp_files()
exec(open("logo/logo.py").read())


if (int(datetime.datetime.now().strftime('%H')) >= 6) & (int(datetime.datetime.now().strftime('%H')) <= 12):
  print ( "  good morning!")
elif (int(datetime.datetime.now().strftime('%H')) > 12) & (int(datetime.datetime.now().strftime('%H')) <= 17):
  print ( "  good afternoon!")
elif (int(datetime.datetime.now().strftime('%H')) > 17) & (int(datetime.datetime.now().strftime('%H')) <= 22):
  print ( "  good evening!")
else :
  print ( "  good night!")

readline.parse_and_bind('tab: complete')
readline.parse_and_bind('set editing-mode vi')

line = raw_input('~ ')
while True:
    if line == 'exit':
        print (bcolors.RED + " hope you made a big loot!" + bcolors.ENDc )
        break
    elif (line == '') | (line == ' '):
        print "nothing to do."

readline.set_completer(SimpleCompleter(command_list).complete)

# Use the tab key for completion
readline.parse_and_bind('tab: complete')

# Prompt the user for text
input_loop()

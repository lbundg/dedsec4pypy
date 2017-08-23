import os
import time
import datetime
import readline
import logging
import os.path

from config.glob import *
from logo.color import bcolors

// test

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
completions = {}

def completer(text, state):
    try:
        matches = completions[text]
    except KeyError:
        matches = [value for value in command_list
                   if text.upper() in value.upper()]
        completions[text] = matches
    try:
        return matches[state]
    except IndexError:
        return None


def list_sp_files():
    dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(dir, 'pymodule')
    counter = 0
    for filename in os.listdir(path):
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

readline.set_completer(completer)
readline.parse_and_bind('tab: menu-complete')
# readline.parse_and_bind('set editing-mode vi')
# readline.set_completer(SimpleCompleter(command_list).complete)
# blablahdhd

while True:
    line = raw_input('\n~ ')
    if line == 'exit':
        print (bcolors.RED + " \n hope you made a big loot!\n" + bcolors.ENDC )
        break
    elif (line == '') | (line == ' '):
        print "nothing to do."
    else:
        modupy = "pymodule/" + line + ".py"
        if (os.path.isfile(modupy)):
            exec(open(modupy).read())

        else:
            print ("command not known please type help." )

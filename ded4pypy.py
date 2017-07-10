import os
import time
import datetime

global gtarget
global gport
global ghash
global gwordlist
global guser
global gap
global ginterface
global ip
global iprange
global modules
global show
global time_now

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
if (int(datetime.datetime.now().strftime('%H')) > 12) & (int(datetime.datetime.now().strftime('%H')) <= 17):
  print ( "  good afternoon!")
if (int(datetime.datetime.now().strftime('%H')) > 17) & (int(datetime.datetime.now().strftime('%H')) <= 22):
  print ( "  good evening!")
else :
  print ( "  good night!")

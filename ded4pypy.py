import os

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
    for filename in os.listdir(path):
        print filename

list_sp_files()
exec(open("logo/logo.py").read())

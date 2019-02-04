#!/usr/bin/python

import os,re,sys,binascii,platform
from time import sleep
from itertools import cycle
from string import lowercase, uppercase
W = '\033[37;1m'
R = '\033[91;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
x = raw_input
if 'linux' and 'unix' and 'linux2' in sys.platform:os.system("clear")
elif 'win' and 'darwin' in sys.platform:os.system("cls")
else:os.system("clear")
str_endeop = '''
{}[{}1{}] {}Encode
{}[{}2{}] {}Decode

{}[{}+{}] {}Pilih {}: {}'''.format(R,Y,R,W,R,Y,R,W,R,B,R,W,R,W)
l_edr = ['[+] Hasil : ',\
         '[+] Text to Encode : ',\
         '[+] Text to Decode : ']
def  fn_hex():
 a = int(x(str_endeop))
 print ''
 if (a > 2): sys.exit()
 b = x(l_edr[a])
 return a,b
try:
 print("""
{}[+] {}Coded by : afelfgie
{}[+] {}GitHub   : github.com/afelfgie
{}[+] {}Facebook : m.facebook.com/aries.isisas.3""".format(R,W,R,W,R,W))
 o,s = fn_hex()
 print '{}{}'.format(l_edr[0], bin(int(binascii.hexlify(s), 16)) if (o == 1) else binascii.unhexlify('%x' % int(s, 2)) if (o == 2) else '')
 print("")
except KeyboardInterrupt:sys.exit()


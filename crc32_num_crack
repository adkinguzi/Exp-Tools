from zlib import crc32
from pip._vendor.distlib.compat import raw_input
import random


char='0123456789'
def crc32_f(data):
      return hex(crc32(data)&0xffffffff)[2:10]
length=input('length:')
crc32_=raw_input('crc32:').lower()
while True:
     text=''
     for i in range(length):
         text+=char[random.randint(0,len(char)-1)]
         print(i)
     if crc32_f(text)==crc32_:
         raw_input('find it:'+text)
         exit

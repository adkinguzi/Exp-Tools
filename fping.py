# -*- coding: utf-8 -*-
# Author By:ice
import os
import time
m = input('请选择扫描模式： c C段扫描'+'  b B段扫描'+'   a A段扫描'+'\n')
i = input('请输入检测ip'+'\n')
try:
    def fping(i,m):
        if m == 'c':
            ip = i.split('.')
            cip = ip[0]+'.'+ip[1]+'.'+ip[2]
            print('扫描结果：' +'\n')
            os.system('fping -a -g '+cip+'.'+'0/24')
        elif m == 'b':
            ip = i.split('.')
            bip = ip[0] + '.' + ip[1]
            print('扫描结果：' + '\n')
            for i in range(0, 256):
                bip + '.' + str(i) + '.0/24'
                os.system('fping -a -g ' + bip + '.' + str(i) + '.0/24')
        elif m == 'a':
            ip = i.split('.')
            aip = ip[0]
            print('扫描结果：' + '\n')
            for i in range(0, 256):
                for k in range(0,256):
                    aip = ip[0] + '.' + str(i)+'.'+str(k)+ '.0/24'
                    print(aip)
                    print(os.system('fping -a -g '+aip))
    fping(i,m)
except Exception:
    pass

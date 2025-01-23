from pwn import *
import re

host = '83.136.254.158'
port = 45937

r = remote(host,port)
res_list = []
for i in range(1,103):
    message = str(i)
    r.sendline(message)
    res = r.recvline()
    res = str(res)
    res = res.strip()
    res = res.replace("[ * CORRECT *]")
    res = re.sub(str(i)+': ','',res)
    res = re.sub("\n'" ,'',res)
    res_list.append(res)
    print(res)
    r.recvuntil('Which character (index) ')
print(''.join(res_list))
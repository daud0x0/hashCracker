#!/usr/bin/python3
#hashcraker

import hashlib, sys, os
from termcolor import colored

hashTodecrypt = str(input('[+] Enter your hash to bruteforce:'))
typeOfHash = str(input('[+] Enter type of hash:'))
filePath = str(input('[+] Enter your wordlists to bruteforce:'))

if os.path.exists == False:
    print('[-] Enter your filePath does not exists!')
    sys.exit()

hashList = ['md5','sha1','sha224','sha256']
if not typeOfHash in hashList:
    print(f'[!] Sorry {typeOfHash} this type of hash is not avalable')
    print(f'avalable hash is {hashList} ')
    sys.exit(1)
    
with open(filePath, 'r') as file:
    for lines in file.readlines():
        if typeOfHash == 'md5':
            hashOb = hashlib.md5(lines.strip().encode())
            hashword = hashOb.hexdigest() 
            if hashword == hashTodecrypt:
                print(colored((f'[!!] Found {typeOfHash} is: {lines} '),'green'))
                sys.exit(0)
        elif typeOfHash == 'sha1':
            hashOb = hashlib.sha1(lines.strip().encode())
            hashword = hashOb.hexdigest()
            if hashword == hashTodecrypt:
                 print(colored((f'[!!] Found {typeOfHash} is: {lines} '),'green'))
    print('Password not found in file')


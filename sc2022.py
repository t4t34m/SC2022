# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import random
import time
import requests
import sys, os
def clz():
    zl="clear"
    os.system(zl)
def header():
    clz()
    print(("""
\x1b[30;38;5;68m
 ____                     ____ _     _____      _    _____
/ ___| _ __   __ _ _ __  / ___| |__ |___ /  ___| | _|___ / _ __
\___ \| '_ \ / _` | '_ \| |   | '_ \  |_ \ / __| |/ / |_ \| '__|
 ___) | | | | (_| | |_) | |___| | | |___) | (__|   < ___) | |
|____/|_| |_|\__,_| .__/ \____|_| |_|____/ \___|_|\_\____/|_|
                  |_|
 2022.v1
\x1b[0m
Usage :
[✔]\x1b[1;38;5;255m python3\x1b[0m sc2022.py a#z
[✔]\x1b[1;38;5;255m python3\x1b[0m sc2022.py a##z
[✔]\x1b[1;38;5;255m python3\x1b[0m sc2022.py a###z

try:
\x1b[0m"""))
if len(sys.argv) == 1:
        header()
        sys.exit(0)
possibleChar = 'qwertyuioplkjhgfdsazxcvbnm1236547890-._'
t = sys.argv[1]
x = sys.argv[1]
attemptThis = ''.join(random.choice(possibleChar) for i in range(len(x)))
attemptNext = ''
done= False
iteration = 0
while done == False:
    gotRandom=attemptThis
    attemptNext = ''
    done = True
    for i in range(len(x)):
        if attemptThis[i] != t[i]:
            done = False
            attemptNext += random.choice(possibleChar)
        else:
            attemptNext += t[i]
            time.sleep(2.4)
            headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://accounts.snapchat.com/",
    "Cookie": "xsrf_token=a-mMpF6dwym43afgEibJew; web_client_id=12126659-1ddb-3d0b-8c4c-e19610ddf0f3; _sca={%22cid%22:%2235552e91-18cd-56fc-bb26-b220994ae1d7%22%2C%22token%22:%22v1.key.2022-01-01_8lt9BOpW.iv.ykqLG02DA/OtGORO.j0/QFbsqE82bUtb8Qa0jO6//zEXiS4ZQT4tYissWzZ42fsdCsi8fl7Hy2bEHDm3hs1Li8jciZDbraK3xOUQoTk21tiPgsPcMQvecgafXovbGZOKh%22}; _scid=f2fd66fb-9e11-14d8-a36f-42d807b8d061; sc_at=v2|H4sIAAAAAAAAADNITjFJNjca100zNjTVNTE2M9RNtDAz1k1NtjAzMU01TElKSqoxNDKwMjQ1NQZKA0VrkJgGgGh4Yl9AAAAA; _sctr=1|1553100000000; oauth_client_id=scan",
    "Connection": "close",
    "Content-Type": "application/x-www-form-urlencoded; charset=utf-8"
    }
            url = "https://accounts.snapchat.com/accounts/get_username_suggestions"
            data = "requested_username="+gotRandom+"&xsrf_token=a-mMpF6dwym43afgEibJew"
            url = "https://accounts.snapchat.com/accounts/get_username_suggestions"
            request = requests.post(url, headers=headers, data=data)
            po = request.content
            if b"OK" in po:
              print(("""[ + ] \x1b[30;38;5;119mAvailable \x1b[0m: %s"""%(gotRandom)))
              file = open("available.txt", "a+")
              file.write("[+] %s , %s \n" %(gotRandom,po))
              file.close()
              file2 = open("availableUsers.txt", "a+")
              file2.write("%s \n" %(gotRandom))
              file2.close()
            elif b"TAKEN" in po:
              print(("""[ - ] \x1b[30;38;5;197mSnapchat account is token \x1b[0m: %s"""%(gotRandom)))
              file = open("token.txt", "a+")
              file.write("%s \n" %(po))
              file.close()
            else:
              print(("""[ ! ] \x1b[30;38;5;160maccount being permanently locked or deleted \x1b[0m: %s"""%(gotRandom)))
              file = open("deleted.txt", "a+")
              file.write("%s \n" %(po))
              file.close()
    iteration = iteration + 1
    attemptThis = attemptNext
    time.sleep(0.3) # sleep time
print("Target matched after ",iteration," iterations")

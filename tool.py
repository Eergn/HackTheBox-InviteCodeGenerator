import os
import subprocess
import platform
import base64

#checking if it is widows
is_windows = any(platform.win32_ver())

#geting Amount Of Invite Codes Needed
x = input("How Many Invite Codes You Want -->")
amount = int(x)
if is_windows == True:
    os.system("cls")
else:
    os.system("clear")
while amount > 0:
    hi = subprocess.check_output(["curl","-ss","-XPOST","https://www.hackthebox.eu/api/invite/generate"],universal_newlines=True)
    #                                                                                               get all output          return string not bytes
    dec = base64.b64decode(hi.split('"')[7]).decode()
    print(dec)
    amount -= 1
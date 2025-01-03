import os
from datetime import date, datetime, timedelta
try:
	from telethon.sync import TelegramClient
	from telethon.sessions import StringSession
	from colorama import init
	from termcolor import colored
except ImportError:
	import os
	os.system('pip install telethon')
	from telethon.sync import TelegramClient
	from telethon.sessions import StringSession
	from colorama import init
	from termcolor import colored
init()

try:
    apiss = open('api.txt','r')
    apis = apiss.readlines()
except:
    apiss = open('api.txt','w')
    apiss.close()
    apiss = open('api.txt','r')
    apis = apiss.readlines()

if apis == []:
    api_id = int(input("\033[34mApi\033[37mId: \033[34m"))
    api_hash = input("\033[34mApi\033[37mHash: \033[34m")
    with TelegramClient(StringSession(), api_id, api_hash) as client:
        ss = client.session.save()
    api_id = int(api_id.replace(' ', ''))
    api_hash = api_hash.replace(' ', '')
    with open('api.txt', 'w') as apiss:
        apiss.write(str(api_id) + '\n')
    apiss.write(api_hash+'\n'+ss)
    apiss = apiss.close()
    ewdewde = input("\n\033[34mPress enter to \033[37mExit\033[34m.")
    os.system('clear || cls')
    exit()
elif len(apis) == 2:
    api_id = int(apis[0])
    api_hash = apis[1]
    print ("\033[34mApi\033[37mId: " + "\033[34m" + str(api_id))
    print ("\033[34mApi\033[37mHash: " + "\033[34m" + api_hash) 
    print("\n\033[34mIf you want to change your \033[37mapi\033[34m delete '\033[37mapi.txt\033[34m'.")
    print('\n')
    with TelegramClient(StringSession(), api_id, api_hash) as client:
        ss = client.session.save()
    with open('api.txt', 'a') as apiss:
        apiss.write(f'\n{ss}')
    sdwed = input("\033[37mPress enter to \033[34mExit\033[37m.")
    os.system('clear || cls')
    exit()
elif len(apis) == 3:
    api_id = int(apis[0])
    api_hash = apis[1]
    string = apis[2]
    print(" Scrap CCV - New Version")
    sdwed = input("\033[37mPress enter to \033[34mcontinue\033[37m.")
    os.system('clear || cls')
try: os.chdir('Scraped')
except:
	os.mkdir('Scraped')
	os.chdir('Scraped')
username = 'XScrap'
lst = ["0","1","2","3","4","5","6","7","8","9","|","\n"]
ccp = list(set())
c = set()
repeated = set()
cnter = 0
clorr1 = "\033[34m"
clorr2 = "\033[37m"
clord = 0
os.system('rm XScrap.session || del XScrap.session')
os.system('clear || cls')
print(colored('\nEnter The Number Of Days To Scrape Messages = ',color = 'magenta'),end = '')
egg = int(input())
today = datetime.now()
DD = timedelta(days=egg)
earlier = today - DD
din = earlier.strftime("%Y-%m-%d")
print('\n')
chanil = input('\033[37mChannel\033[34m/\033[37mGroup\033[37m:\033[34m')
chanil = chanil.replace('@','')
with TelegramClient(StringSession(string), api_id, api_hash) as client:
    os.system('clear || cls')
    print(clorr2 + "Scraping" + clorr1 + " Started...")
    binuu = chanil
    try:
        chanil = client.get_entity(chanil)
        print(colored('\n Enter The Name For Output File = ', color='magenta'), end='')
        onichan = input()
    except:
        chanil = binuu
        onichan = chanil
    for message in client.iter_messages(chanil):
        if din <= message.date.strftime('%Y-%m-%d'):
            msg = str(message.text)
        else:
            break
        msgln = len(msg)
        rr = 0
        cc = ""
        lstc = []
        while rr != msgln:
            if msg[rr] in lst:
                if msg[rr] == lst[0]:
                    cc = cc + lst[0]
                elif msg[rr] == lst[1]:
                    cc = cc + lst[1]
                elif msg[rr] == lst[2]:
                    cc = cc + lst[2]
                elif msg[rr] == lst[3]:
                    cc = cc + lst[3]
                elif msg[rr] == lst[4]:
                    cc = cc + lst[4]
                elif msg[rr] == lst[5]:
                    cc = cc + lst[5]
                elif msg[rr] == lst[6]:
                    cc = cc + lst[6]
                elif msg[rr] == lst[7]:
                    cc = cc + lst[7]
                elif msg[rr] == lst[8]:
                    cc = cc + lst[8]
                elif msg[rr] == lst[9]:
                    cc = cc + lst[9]
                elif msg[rr] == lst[10]:
                    cc = cc + lst[10]
                elif msg[rr] == lst[11]:
                    cc = cc + lst[11]
                rr = rr + 1
            else:
                rr = rr + 1
        neme = f'{onichan}_Scrapped.txt'
        texti = open(neme, 'a')
        #default
        r = cc
        f = 0
        d = 0
        def detector(detect):
            global f, d
            f = int(detect.count('|'))
            d = int(f // 3)
        detector(r)
        if d >= 2:
            if f % 3 == 0:
                r = r.replace('\n', ' ')
                l = r.split(' ')
                for i in range(d):
                    try:
                        c.add(l[i])
                    except Exception as e:
                        pass
                    for item in c:
                        if len(item) == 28 and "|" not in str(item)[0:14] and "|" not in str(item)[26:28]:
                            if item not in repeated:
                                repeated.add(item)
                                texti.write(f'{item}\n')
                                cnter += 1
                                if clord == 0:
                                    clord = 1
                                    print(clorr1 + str(cnter) + clorr2 + "|" + clorr1 + onichan + clorr2 + "|" + clorr1 + "CyMon" + clorr2 + "|" + clorr1 + "CYCheck" + clorr2 + "|" + clorr1 + "CYSCRAPE" + clorr2 + "|" + clorr1 + "XMON")
                                elif clord == 1:
                                    clord = 0
                                    print(clorr2 + str(cnter) + clorr1 + "|" + clorr1 + onichan + clorr2 + "|" + clorr2 + "CyMon" + clorr1 + "|" + clorr2 + "CYCheck" + clorr1 + "|" + clorr2 + "CYSCRAPE" + clorr1 + "|" + clorr2 + "XMON")
                                elif len(item) == 26 and "|" not in str(item)[0:14] and "|" not in str(item)[24:26]:
                                    repeated.add(item)
                                    mm = item.split('|')[1]
                                    anos = item.split('|')[2]
                                    cvv = item.split('|')[3]
                                    item = item.split('|')[0]
                                    items = '20' + str(anos)
                                    item = f'{item}|{mm}|{items}|{cvv}'
                                    if item not in repeated:
                                        texti.write(f'{item}\n')
                                        texti.close()
                                        cnter +=1
                                        if clord == 0:
                                            clord = 1
                                            print(clorr1 + str(cnter) + clorr2 + "|" + clorr1 + onichan + clorr2 + "|" + clorr1 + "CyMon" + clorr2 + "|" + clorr1 + "CYCheck" + clorr2 + "|" + clorr1 + "CYSCRAPE" + clorr2 + "|" + clorr1 + "XMON")
                                        elif clord == 1:
                                            clord = 0
                                            print(clorr2 + str(cnter) + clorr1 + "|" + clorr1 + onichan + clorr2 + "|" + clorr2 + "CyMon" + clorr1 + "|" + clorr2 + "CYCheck" + clorr1 + "|" + clorr2 + "CYSCRAPE" + clorr1 + "|" + clorr2 + "XMON")
                                        else:
                                            pass
        if "|" in cc:
            cc = cc.split('\n')
            ccln = len(cc)
            ccl = 0
            while ccl != ccln:
                if len(cc[ccl]) == 28 and "|" not in str(cc[ccl])[0:14] and "|" not in str(cc[ccl])[26:28] :
                    if cc[ccl] not in ccp:
                        repeated.add(cc[ccl])
                        ccp.append(cc[ccl])
                        texti.write(ccp[-1])
                        texti.write('\n')
                        texti.close
                        cnter = cnter + 1
                        if clord == 0:
                            clord = 1
                            print(clorr1 + str(cnter) + clorr2 + "|" + clorr1 + onichan + clorr2 + "|" + clorr1 + "CyMon" + clorr2 + "|" + clorr1 + "CYCheck" + clorr2 + "|" + clorr1 + "CYSCRAPE" + clorr2 + "|" + clorr1 + "XMON")
                        elif clord == 1:
                            clord = 0
                            print(clorr2 + str(cnter) + clorr1 + "|" + clorr1 + onichan + clorr2 + "|" + clorr2 + "CyMon" + clorr1 + "|" + clorr2 + "CYCheck" + clorr1 + "|" + clorr2 + "CYSCRAPE" + clorr1 + "|" + clorr2 + "XMON")

                        else:
                            pass        
                elif len(cc[ccl]) == 26 and "|" not in str(cc[ccl])[0:14] and "|" not in str(cc[ccl])[24:26] :
                    if cc[ccl] not in ccp:
                        cch = cc[ccl]
                        cch = cch.split('|')
                        ccn = cch[0]
                        mmm = cch[1]
                        yyy = cch[2]
                        cbv = cch[3]
                        yyy = '20'+str(yyy)
                        cch = f'{ccn}|{mmm}|{yyy}|{cbv}'
                        if cch not in repeated:
                            repeated.add(cch)
                            ccp.append(cch)
                            texti.write(ccp[-1])
                            texti.write('\n')
                            texti.close
                            cnter = cnter + 1
                            if clord == 0:
                                clord = 1
                                print(clorr1 + str(cnter) + clorr2 + "|" + clorr1 + onichan + clorr2 + "|" + clorr1 + "CyMon" + clorr2 + "|" + clorr1 + "CYCheck" + clorr2 + "|" + clorr1 + "CYSCRAPE" + clorr2 + "|" + clorr1 + "XMON")
                            elif clord == 1:
                                clord = 0
                                print(clorr2 + str(cnter) + clorr1 + "|" + clorr1 + onichan + clorr2 + "|" + clorr2 + "CyMon" + clorr1 + "|" + clorr2 + "CYCheck" + clorr1 + "|" + clorr2 + "CYSCRAPE" + clorr1 + "|" + clorr2 + "XMON")
                            else: 
                                pass
                ccl = ccl + 1
        elif len(cc) < 15:
            pass
        #ccnum
        elif cc[0:15].isdigit and cc[0] == "4" or "3" or "5" or "6" and cc.split('\n')[1].isdigit and cc.split('\n')[2].isdigit:
            try:
                cc = cc.split('\n')
                nrte = cc[2]
                nrta = cc[3]
                if nrte[0] == "2" or nrte[0] == "3" and len(nrte) == 2:
                    yyyy = "20" + nrte
                elif nrta[0] == "2" or nrta[0] == "3" and len(nrta) == 2:
                    yyyy = "20" + nrta
                if len(cc[2]) == 2 and str(cc[2])[0] != "2":
                    mm = cc[2]
                elif len(cc[3]) == 2 and str(cc[3])[0] != "2":
                    mm = cc[3]
                ccer = cc[0] + "|" + mm + "|" + yyyy + "|" + cc[1]
                if ccer not in ccp and len(ccer) == 28:
                    ccp.append(ccer)
                    if ccer not in repeated:
                        repeated.add(ccer)
                        texti.write(ccer)
                        texti.write('\n')
                        texti.close()
                        cnter += 1
                        if clord == 0:
                            clord = 1
                            print(clorr1 + str(cnter) + clorr2 + "|" + clorr1 + onichan + clorr2 + "|" + clorr1 + "CyMon" + clorr2 + "|" + clorr1 + "CYCheck" + clorr2 + "|" + clorr1 + "CYSCRAPE" + clorr2 + "|" + clorr1 + "XMON")
                        elif clord == 1:
                            clord = 0
                            print(clorr2 + str(cnter) + clorr1 + "|" + clorr1 + onichan + clorr2 + "|" + clorr2 + "CyMon" + clorr1 + "|" + clorr2 + "CYCheck" + clorr1 + "|" + clorr2 + "CYSCRAPE" + clorr1 + "|" + clorr2 + "XMON")
                        else:
                            pass
            except:
                pass
        else:
            pass

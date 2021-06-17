
import urllib.request
import requests
import time
import re
import os,re
import os
import datetime
    
    
account="000"
password="000"

if os.access("D:\HKD-wifi-account.txt", os.F_OK):
    f = open("D:\HKD-wifi-account.txt","r")   #设置文件对象

    
    account=f.read()
    f.close() #关闭文件
else:
    f = open("D:\HKD-wifi-account.txt","w")
    f.write('')  
    f.close()

if os.access("D:\HKD-wifi-password.txt", os.F_OK):
    f = open("D:\HKD-wifi-password.txt","r")   #设置文件对象

    
    password=f.read()
    f.close() #关闭文件
else:
    f = open("D:\HKD-wifi-password.txt","w")
    f.write('')
    f.close()

yys=""

if os.access("D:\HKD-wifi-yys.txt", os.F_OK):
    f = open("D:\HKD-wifi-yys.txt","r")   #设置文件对象
    yys=f.read()
    f.close() #关闭文件
else:
    f = open("D:\HKD-wifi-yys.txt","w")
    f.write('')
    f.close()

kv={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9",
"Cache-Control": "max-age=0",
"Connection": "keep-alive",
"Content-Length": "165",
"Content-Type": "application/x-www-form-urlencoded",
"Cookie": "PHPSESSID=925ucrjemcq23rd0hs4t9sqq20",
"Host": "10.10.10.111:801",
"Origin": "http://10.10.10.111",
"Referer": "http://10.10.10.111/",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    }

data_yd={
    "DDDDD": ",0,"+account+"@wcmcc",
"upass": password,
"R1": "0",
"R2": "0",
"R3": "0",
"R6": "0",
"para": "00",
"0MKKey": "123456",
"buttonClicked": "",
"redirect_url": "",
"err_flag": "",
"username":"" ,
"password": "",
"user": "",
"cmd": "",
"Login": ""
    }

data_lt={
    "DDDDD": ",0,"+account+"@unicom",
"upass": password,
"R1": "0",
"R2": "0",
"R3": "0",
"R6": "0",
"para": "00",
"0MKKey": "123456",
"buttonClicked": "",
"redirect_url": "",
"err_flag": "",
"username":"" ,
"password": "",
"user": "",
"cmd": "",
"Login": ""
    }

data_dx={
    "DDDDD": ",0,"+account+"@wtelecom",
"upass": password,
"R1": "0",
"R2": "0",
"R3": "0",
"R6": "0",
"para": "00",
"0MKKey": "123456",
"buttonClicked": "",
"redirect_url": "",
"err_flag": "",
"username":"" ,
"password": "",
"user": "",
"cmd": "",
"Login": ""
    }


if yys=="1":
    data=data_yd
elif yys=="2":
    data=data_lt
else:
    data=data_dx



            

for mm in range(1,20):

    try:

        aaa=requests.get("http://10.10.10.111")
        re1 = r'v46ip=\'(.*?)\''
        re2 = r'v4ip=\'(.*?)\''
        ip = re.findall(re1, aaa.text)
        if len(ip)==0:
            ip = re.findall(re2, aaa.text)

                
        url="http://10.10.10.111:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=10.10.10.111&iTermType=1&wlanuserip="+str(ip[0])+"&wlanacip=null&wlanacname=null&mac=00-00-00-00-00-00&ip="+str(ip[0])+"&enAdvert=0&queryACIP=0&jsVersion=2.4.3&loginMethod=1"


        html = requests.post(url,headers=kv,data=data)
        baidu=requests.get("https://www.baidu.com")


        now=datetime.datetime.now()

        f2 = open('D:\\HKD_wifi_log.txt','a+',encoding='utf-8')
        f2.write('\n\n\n'+str(now)+'\n'+str(ip[0])+"\n"+str(baidu.status_code)+'\n\n\n\n')
        f2.close
        if baidu.status_code==200:
            break
    except:
        pass





















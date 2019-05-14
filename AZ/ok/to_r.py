from stem import Signal
from stem.control import Controller
import time ,os ,subprocess
from requests import get
import urllib.request
from urllib import request
import requests
controller = Controller.from_port(port=9051)
proxies = {
    'http': 'socks5://127.0.0.1:9050','https': 'socks5://127.0.0.1:9050',}






def fix_tor():
	print(" FIXING TOR  CONNECTION : ",end='',flush=True)
	with open(os.devnull, 'wb') as hide_output:
		exit_code = subprocess.Popen(['service', "tor", 'restart'], stdout=hide_output, stderr=hide_output).wait()
		if exit_code==0:
			print("TOR FIXED")
			#check_connect_mysql()
fix_tor()




def call_ip():
	s = requests.Session()
	s.proxies = proxies
	r = s.get('https://api.ipify.org')
	#print(r.text)
	m_ip=r.text
	print(m_ip)
	return m_ip

def renew_tor():
	controller.authenticate(password="1234")
	controller.signal(Signal.NEWNYM)
	time.sleep(controller.get_newnym_wait())
	call_ip()

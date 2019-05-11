from stem import Signal
from stem.control import Controller
import time
from requests import get
import urllib.request
from urllib import request
import requests
controller = Controller.from_port(port=9051)
proxies = {
    'http': 'socks5://127.0.0.1:9050','https': 'socks5://127.0.0.1:9050',}

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

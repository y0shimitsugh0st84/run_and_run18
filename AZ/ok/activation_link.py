import smtplib
import time
import imaplib ,os ,sys
import email
import bs4
from bs4 import BeautifulSoup
from faker import Faker
import datetime
import random
import string
import subprocess as sp
from urllib.parse import quote
imaplib._MAXLINE = 80000
def save_it(finall):
	with open('shift_url2','a') as f:
	        f.write(finall+"\n")
	        f.close()

activation=[]
def connection_imap():
	conn = imaplib.IMAP4_SSL("imap.gmail.com", 993)
	gmail_user = 'wa33iorx2@gmail.com'
	gmail_pwd = 'agoon007'
	conn.login(gmail_user, gmail_pwd)
	return conn

#read_uniq()gather_acces("john21peolg6brown@multi-service-seller.tk")
###################################https://gitlab.com/users/confirmation?confirmation_token=26C4-BVxW_8MwTaHP9x-#########################################################################
############################################################################################################
def l0g (messa):
	messa=messa.upper()
	outpu_l0g="echo '  --> "+messa+"' >> cchck "
	print(messa)
	os.system(outpu_l0g)
############################################################################################################
############################################################################################################

def gather_acces(emmail):
	print("search for email")
	magic_formul='(TO "xxxxx" SUBJECT "Confirmation instructions")'
	magic_formul=magic_formul.replace("xxxxx",emmail)
	mail=connection_imap()
	mail.select('inbox')
	status, data = mail.search(None, magic_formul)
	ids = data[0]
	unread_msg_nums = data[0].split()
	print (" [ ",len(unread_msg_nums)," ]",flush =True,end = " ")
	if len(unread_msg_nums) == 0 :
		#print("NOTHING FOUND")
		l0g ("NOTHING FOUND")
		mail.close()
		
		time.sleep(8)
		gather_acces(emmail)

	l0g ("hmm mybe email FOUND")
	for emailid in unread_msg_nums:
		resp3, data3 = mail.uid("fetch", emailid,"(RFC822)" )#mail.uid('search', None, "ALL")
		result, data = mail.fetch(emailid, "(RFC822)")
		email_body = data[0][1].decode("utf-8")
		za_body_mail = email.message_from_string(email_body)
		iii=za_body_mail.get_content_type()
		ohh=za_body_mail.get_payload()
		#charset = za_body_mail.get_content_charset()
		html0 = za_body_mail.get_payload()#, str(charset), "ignore"#.encode('utf8', 'replace')
		#print(iii)
		if za_body_mail.is_multipart():
			for part in za_body_mail.get_payload():
				
				if part.get_content_type() == 'text/plain' :
					#print(part.get_content_type())
					#print(part)
					html0=part.get_payload()
					#print(html0)

		else:
			print(za_body_mail.get_payload())

		all_links=html0.split('\n')
		shit_valid=all_links[3]
		if "confirmation_token=" in shit_valid :
			activation.append(shit_valid)
			print(shit_valid)
	mail.close()
	return activation

def remove_emails():
	print("search for email")
	magic_formul='(SUBJECT "Pipeline")'
	mail=connection_imap()
	mail.select('inbox')
	status, data = mail.search(None, magic_formul)
	ids = data[0]
	unread_msg_nums = data[0].split()
	print (" [ ",len(unread_msg_nums)," ]",flush=True,end= " ")
	
	if len(unread_msg_nums) == 0 :
		#print("NOTHING FOUND")
		l0g ("NOTHING FOUND")
		mail.close()
		
		time.sleep(8)
		gather_acces(emmail)

	l0g ("hmm mybe email FOUND")
	for emailid in unread_msg_nums:
		mail.store(emailid, '+FLAGS', '\\Deleted')
	mail.expunge()
	mail.close()
	mail.logout()
	return 

#gather_acces("lauren6bxenlewis@k0f0.onthewifi.com")
#print(link.get('href')) https://gitlab.com/users/confirmation?confirmation_token=iGVyD-hesU7kv-zVBztf

#read_uniq()gather_acces("john21peolg6brown@multi-service-seller.tk")remove_emails()
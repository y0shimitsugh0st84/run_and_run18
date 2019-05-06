import random,datetime,string , os ,time ,subprocess 
from selenium import webdriver
from faker_e164.providers import E164Provider
from faker import Faker
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from pyvirtualdisplay import Display
import requests
import io
from pydub import AudioSegment
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from stem import Signal
from stem.control import Controller
from zoho_act_mail import *
import curses
import speech_recognition as sr
display = Display(visible=0, size=(960, 860))
######################################################
#controller = Controller.from_port(port=9051)ay pydub
#apt-get install python-pyaudio python3-pyaudio ffmpeg
# pip3 install speechrecognition requests pyvirtualdisplay pydub
#apt-get install python-pyaudio python3-pyaudio ffmpeg
#kx_id echo $HOSTNAME > /root/id_docker

email_users=["m2","m3","m4","m5","m6","m7","m8","m10","m20","m21","m30"]

print(email_users)
f = open("/root/id_docker", "r")
lines=f.readline().split("\n")
host_name=lines[0]
print(lines[0])
try:
	for ll in email_users :
		if host_name in ll:
			email_users.remove(ll)
			break
except :
	print("ok nothing ")
print(email_users)






randomindex = random.randint(0,len(email_users)-1)


new_host=email_users[randomindex]
print (new_host)
kx_id=new_host



url_kxd=gather_acces(kx_id+"@chokariz.tk")
url_kxd=url_kxd[-1]
print (url_kxd,kx_id)
#input()
#input()
dk_image="s00ka/da0"
dk_liste_image="s00ka/list"
comd="docker rm  -f 80x || docker pull "+dk_image+":latest && docker run -d --name 80x --hostname "+kx_id+" -e PASSWORD=123456789 --cap-add=NET_ADMIN --device=/dev/net/tun -p 6080:6080 -p 5001:22 -p 6001:3389 -p 1022:1022   --dns=8.8.4.4 --dns=8.8.8.8 "+dk_image+" && clear && ioo=$(curl ipinfo.io/ip) && echo $ioo:6080 && docker rm -f 50x || docker pull balitch00/bl_1:latest && docker run -d --privileged --cap-add SYS_ADMIN --name 50x --hostname l"+kx_id+" -p 5002:22 -p 1984:1984 --dns=8.8.4.4 --dns=8.8.8.8 "+dk_liste_image+" && clear && ioo=$(curl ipinfo.io/ip) && echo $ioo:6080  "
cmd_tran=comd.replace("xxx-xxx",kx_id)
print(cmd_tran)

######################################################
#red="https://trial.docker.com/launching?token=800af145-2b45-487c-b62b-11acdf3c374e"
red=url_kxd
global arr_info
arr_info=[]
domains=["@gmail.com"]

############################################################################################################
############################################################################################################
Profile_name="s0ob7y28.gitlab_fire_prof"
Binarry="/root/firefox-sdk/bin/firefox-bin"
path_profile="/root/.mozilla/firefox/"+Profile_name
gecko_path="/usr/bin/geckodriver13"


	#return outpu_l0g

	#os.system("echo 'CAPTCHA KILLED' >> cchck ")


def sstart():
	new_prof()
	capabilities = webdriver.DesiredCapabilities().FIREFOX
	capabilities["marionette"] = True
	profile = webdriver.FirefoxProfile(path_profile)
	binary = FirefoxBinary(Binarry)
	driver = webdriver.Firefox(firefox_binary=binary , capabilities=capabilities , firefox_profile=profile , executable_path=gecko_path)
	return driver




######################################################


reasonableCharacters = (string.digits + string.ascii_letters )
def password0(minimum=5, maximum=6):
    return ''.join(
        random.choice(reasonableCharacters) for x in range(
            random.randint(minimum, maximum)
        )
    )




########################################################################################################"
###################################### "               "################################################"
###################################### "               "################################################"
###################################### "               "################################################"
###################################### "               "################################################"
########################################################################################################"



########################################################################################################"
###################################### "               "################################################"
###################################### "               "################################################"
###################################### "               "################################################"
###################################### "               "################################################"
########################################################################################################"


def new_prof():
	l0g ("new profile")
	display.start()


	print("C R E A T I N G    P R O F I L E  : " ,end="",flush=True)
	remove_prof="rm -rf /root/.mozilla/firefox/"+Profile_name
	extract_prof="tar xf "+Profile_name+".tar.gz -C /root/.mozilla/firefox"
	empty_tmp="rm -rf /tmp/*"
	#vpn_ip=get_myip()
	#l0g(vpn_ip)


	try:
		subprocess.Popen(remove_prof, shell=True)
		time.sleep(1)
		subprocess.Popen(empty_tmp, shell=True)
	except:
		pass
	try:
		subprocess.Popen(extract_prof, shell=True)
		time.sleep(1)
		print("  O  K  ")
	except:
		pass
########################################################################################################"
###################################### "               "################################################"
###################################### "               "################################################"
###################################### "               "################################################"
###################################### "               "################################################"
########################################################################################################"
def go_820():
	l0g("----------------------------------------> START <-------------------------------------- ")
	l0g("")
	l0g ("new session")
	driver=sstart()
	driver.get(red)

	#vpn_ip=get_myip()
	

	try:
		if "153.92.30.200" in vpn_ip :
			l0g("VPN down  ---> "+vpn_ip)
		else:
			l0g("VPN UP  ---> "+vpn_ip)
	except:
		pass

########################################################################################################"
########################################################################################################"

	try:
		star_new_trial=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._1HzQ5Leqk_2upNfof4J1WE')))
		star_new_trial.click()
		xx=13
		l0g("ready !! WAITING "+str(60*xx)+"  ---> ")
		time.sleep(60*xx)
		
	except:
		l0g("no trial !!  ---> ")

	#time.sleep(2)driver.get(red)https://trial.docker.com/launching?token=05e8ae1f-0ce3-49cf-830b-d0a351220b42
########################################################################################################"
########################################################################################################"
	try:
		star_new_trial=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.LFciOZ2c0shORRbilT_zE')))
		xx=1
		l0g("ready !! WAITING "+str(60*xx)+"  ---> ")
		time.sleep(60*xx)
		l0g("ready !!NO  WAITING "+str(60*xx)+"  ---> ")
	except:
		l0g("no trial !!  ---> ")
########################################################################################################"
########################################################################################################"
########################################################################################################"
	
	activvat=gather_acces(kx_id+"@chokariz.tk")
	print(kx_id ,activvat)
	driver.get(activvat[-1])
	#input()

	
	driver.get("https://trial.docker.com/demo")
	time.sleep(25)
	#input()
	c_url=driver.current_url
	if "demo" in c_url :
		try:
			#element = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='posted_1']/div[3]")))
			trial_lisst=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[1]/ul/li[3]/div')))
			print("docker ok ","G_BLOOD_END")
			lis1=driver.find_elements_by_xpath('//*[@id="root"]/div/div/div[1]/ul/li[3]/div')[0]
			lis1.click()
			print(" ADMIN O K","G_BLOOD_END")
		except Exception as e :
			print("errrrooo "+str(e))
		try:
			B_button=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.terminal.xterm.xterm-theme-default.xterm-cursor-style-block')))
			B_button.click()
			time.sleep(10)
			B2_button=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.xterm-rows')))
			tter=B2_button.text
			#xterm-rows
			if "admin@trial-console:~$" in tter:
				B_button.send_keys(Keys.RETURN)
				time.sleep(5)
				B_button.send_keys(cmd_tran,Keys.RETURN)
				print(" admin@trial-console : O K ","G_BLOOD_END")
			else:
				pass
				#driver.refresh()
				#chk(driver)
		except  Exception as e:
				print(" N O "+str(e),"G_BLOOD_END")
	#input()
	try:
		#OU3wpEgR9LahNNZBRuuF6 _2Emw38rNoK7Azp0MbyegGI
		admin_cosol=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.OU3wpEgR9LahNNZBRuuF6._2Emw38rNoK7Azp0MbyegGI')))
		print("okkkkkkkkkkkkk")
	except Exception as e :
		print("okkkkkkkkkkkkk"+str(e))
	try:
		#element = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='posted_1']/div[3]")))
		trial_lisst=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[1]/ul/li[3]/div')))
		print("docker ok ","G_BLOOD_END")
		lis1=driver.find_elements_by_xpath('//*[@id="root"]/div/div/div[1]/ul/li[3]/div')[0]
		lis1.click()
		lis1.click()
		print(" ADMIN O K","G_BLOOD_END")
	except Exception as e :
		print("nooooooooooooooooooo"+str(e))
	#input()
	exit(0)
	driver.quit()


try:
	visibilityo=sys.argv[1]
	print(visibilityo)
except:
	visibilityo="0"



def starter(visibilityo):
	if visibilityo != "1":
		print("Visible = hide")
		#display = Display(visible=0, size=(800, 600))
		#display.start()
		go_820()
		display.stop()
	else:
		print("Visible = visible")
		go_820()

starter(visibilityo)
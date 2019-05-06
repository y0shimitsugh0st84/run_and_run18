#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql
from datetime import *
import time , os ,sys
#print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))


host= 'remotemysql.com'
db='DPeymQOKW9'
user='DPeymQOKW9'
password='92ecgL69FU'




def read_activ_user():
	connection =pymysql.connect(host, user, password, db)
	#user_id=str(user_id)
	cmdf=""
	os.system("echo '' > /root/list_api && sed -i '/^$/d' /root/list_api")
	#os.
	print('PRINT RAW  [ '+"active"+' ] :  ',flush=True , end="")
	try:
		with connection.cursor() as cursor:
			sql = "SELECT * FROM `t_user_done` WHERE `user_status`=%s"
			cursor.execute(sql, ("active"))
			#connection.commit()
			result = cursor.fetchall()
			for raa in result:
				outpu_2=raa[1]+'#'+str(raa[0])
				print(outpu_2)
				cmdo4="echo "+outpu_2+" >> /root/list_api"
				os.system(cmdo4)
			#print(' DONE')
	except Exception as e :
		connection.rollback()
		print(' SQL ERROR :',e)

	finally:
		connection.close()


#   "UPDATE Employee set DepartmentCode = 102 where id=121"

def delete_user(user_id):
	connection =pymysql.connect(host, user, password, db)
	#today = str(date.today())
	user_id=str(user_id)
	create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
	print('REMOVE ALL RAW : '+user_id+'   ',flush=True , end="")
	try:
		with connection.cursor() as cursor:
			sql = "DELETE FROM `t_user_done` WHERE user_id = %s"
			cursor.execute(sql, (user_id))
			connection.commit()
			print(' DONE')
	except Exception as e :
		connection.rollback()
		print(' SQL ERROR :',e)

	finally:
		connection.close()
		


#v_check()
#insert_user('0candace58zpmbmeyer#12058269#61d732a8495aa796c5dbaab40da3ba','active')
#insert_user()
#search_user("active")
#time.sleep(1)
##delete_user("11")

#search_user("banned")
#update_user(4,"active")
#read_activ_user()
#print(sys.argv[1])
#search_user("banned")
if len(sys.argv) > 1:
    blah = sys.argv[1]
    delete_user(blah)
else:
    read_activ_user()

try:
	os.system("rm /root/dead_list_api")
except:
	pass
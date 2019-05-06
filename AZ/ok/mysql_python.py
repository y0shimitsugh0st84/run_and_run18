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



init_connection = pymysql.connect(host, user, password, db)

#print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

def v_check():


	try:
		with connection.cursor() as cursor:
			cursor.execute("SELECT VERSION()")
			version = cursor.fetchone()
			print("Database version: {}".format(version[0]))
	finally:
		connection.close()


def insert_user(user_key=None,user_status ='active',user_create=None):
	connection =pymysql.connect(host, user, password, db)
	#today = str(date.today())
	create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
	print('ADD RAW TO DATABAE :',flush=True , end="")
	try:
		with connection.cursor() as cursor:
			sql = "INSERT INTO `t_user_done` (`user_key`, `user_status`, `user_date`) VALUES (%s, %s, %s)"
			cursor.execute(sql, (user_key,user_status,create_time))
			connection.commit()
			print(' DONE')
	except Exception as e :
		connection.rollback()
		print(' SQL ERROR :',e)

	finally:
		connection.close()



def read_user(user_id):
	connection =pymysql.connect(host, user, password, db)
	user_id=str(user_id)
	print('PRINT RAW  [ '+user_id+' ] :  ',flush=True , end="")
	try:
		with connection.cursor() as cursor:
			sql = "SELECT * FROM `t_user_done` WHERE `user_id`=%s"
			cursor.execute(sql, (user_id))
			#connection.commit()
			result = cursor.fetchone()
			print('[ '+str(result[0]),result[1],result[2],str(result[3])+' ]')
			#print(' DONE')
	except Exception as e :
		connection.rollback()
		print(' SQL ERROR :',e)

	finally:
		connection.close()






def search_user(user_id):
	#user_id=str(user_id)
	connection =pymysql.connect(host, user, password, db)
	print('SEARCH ALL RAW : '+user_id+'   ',flush=True , end="\n")
	try:
		with connection.cursor() as cursor:
			sql = "SELECT * FROM `t_user_done` WHERE `user_status`=%s"
			cursor.execute(sql, (user_id))
			#connection.commit()
			result = cursor.fetchall()
			print(len(result))

			#for row in result:
				 #print(row[0],row[1],row[2],str(row[3]))
			#print(result[0],result[1],result[2],str(result[3]))
			#print(' DONE')
	except Exception as e :
		connection.rollback()
		print(' SQL ERROR :',e)

	finally:
		connection.close()





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

def update_user(user_id,user_status):
	connection =pymysql.connect(host, user, password, db)
	#today = str(date.today())
	user_id=str(user_id)
	create_time=time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
	print('UPDAT-E  ALL RAW : '+user_id+'   ',flush=True , end="")
	try:
		with connection.cursor() as cursor:
			sql = "UPDATE `t_user_done` set user_status = %s WHERE user_id = %s"
			cursor.execute(sql, (user_status ,user_id))
			connection.commit()
			print(' DONE')
		read_user(user_id)
	except Exception as e :
		connection.rollback()
		print(' SQL ERROR :',e)

	finally:
		connection.close()

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



#v_check()
#insert_user('0candace58zpmbmeyer#12058269#61d732a8495aa796c5dbaab40da3ba','active')
#insert_user()
#search_user("active")
#time.sleep(1)
##delete_user("11")

#search_user("banned")
#update_user(4,"active")
#read_activ_user()
#search_user("banned")
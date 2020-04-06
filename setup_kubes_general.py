#!/usr/bin/python

import os
import sys
import time

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan

if os.geteuid() == 0:
	print (P + "root level confirmed" + W)
else:
	print (R + "Not running as root\nExiting..." + W)
	sys.exit()

print (C + "Running apt update..." + W)

os.system("sudo apt update")

print (C + "Running dist-upgrade -y..." + W)

os.system("sudo apt dist-upgrade -y")

print (C + "Adjusting /boot/cmdline.txt..." + W)

file = open("/boot/cmdline.txt", 'r')
file_lines = file.readlines()
line = file_lines[0].replace("\n", "")

if " cgroup_enable=cpuset cgroup_memory=1 cgroup_enable=memory" not in line:
	print (C + "File content will be " + str(line) + " cgroup_enable=cpuset cgroup_memory=1 cgroup_enable=memory" + W)

	os.system("sudo echo \"" + str(line) + " cgroup_enable=cpuset cgroup_memory=1 cgroup_enable=memory\" > /boot/cmdline.txt")
else:
	print(O + "/boot/cmdline.txt already configured" + W);

print (C + "Creating kubelist..." + W)

os.system("sudo echo \"deb http://apt.kubernetes.io/ kubernetes-xenial main\" > /etc/apt/sources.list.d/kubernetes.list")

print (C + "Adding key..." + W)

os.system("curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -")

print (C + "Running apt update..." + W)

os.system("sudo apt update")

print (C + "Installing kubectl..." + W)

os.system("sudo apt install kubectl -y")

print (C + "Installing k3sup..." + W)

os.system("curl -ssL https://get.k3sup.dev | sudo sh")

print (C + "Rebooting..." + W)

time.sleep(5)

os.system("sudo reboot")

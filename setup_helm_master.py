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

print (C + "Getting helm install script..." + W)

os.system("curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3")

print (C + "Changing permissions on helm install script..." + W)

os.system("chmod 700 get_helm.sh")

print (C + "Running helm install script..." + W)

os.system("./get_helm.sh")

print (C + "helm installing stable repo..." + W)

os.system("helm repo add stable https://kubernetes-charts.storage.googleapis.com/")

print (O + "helm installed" + W)
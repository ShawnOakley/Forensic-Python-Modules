# Converts REG_BINARY values to a string MAC address

def val2addr(val):
	addr = ""
	for ch in val:
		addr += ("02x "% ord(ch))
	addr = addr.strip(" ").replace(" ",":")[0:17]
	return addr

# Grabs key from Windows registry, loops through extracting
# network name and DefaultGatewayMAC

# NOTE: Relies on python-registry

from python-registry import *
import sys
from Registry import Registry

# from _winreg import *
# Does not work in Linux

# Prints all keys in a Registry

def rec(key, depth=0):
	print "\t" * depth + key.path()
	for subkey in key.subkeys():
		rec(subkey, depth + 1)

def printNets(reg = ""):
	# NOTE: below is code for _winreg module
	# net = "SOFTWARE\Microsoft\Windows NT\Current Version"+\
	# 	"\NetworkList\Signatures]Unmanaged"
	# key = OpenKey(HKEY_LOCAL_MACHINE.net)
	# print "\n[*] Networks You have Joined."
	# for i in range(100):
	# 	try:
	# 		guid = EnumKey(key, i)
	# 		netKey = OpenKey(key, str(guid))
	# 		(n, adrr, t) = EnumValue(netKey, 5)
	# 		(n, name, t) = EnumValue(netKey, 4)
	# 		macAddr = val2addr(addr)
	# 		netName = str(name)
	# 		print '[+]' + netName + ' ' + macAddr
	# 		CloseKet(netKey)
	# 	except:
	# 		break
	reg = Registry.Registry(reg || "SOFTWARE\Microsoft\Windows NT\Current Version"+\
	"\NetworkList\Signatures]Unmanaged")

	rec(reg.root())





# Create an instance of mechanize browser
# Open the wigle.net page
# encode username and password as parameteres and request 
# a login at the Wigle login page
# Once logged in, creates an HTTP post using parameter 
# the parameter netid as the MAC address to search the 
# database

import mechanize, urllib, re, urlparse


def main():
	printNets()
if __name__ == "__main__":
	main()

# Converts REG_BINARY values to a string MAC address in Windows 7
# Resources: http://support.microsoft.com/kb/147797
# http://www.irongeek.com/i.php?page=security/windows-forensics-registry-and-file-system-spots
# http://blog.superuser.com/2011/05/16/windows-7-network-awareness/
# http://eptuners.com/forensics/contents/examination.htm
# http://electronics.howstuffworks.com/how-to-tech/clean-computer-registry.htm
# http://msdn.microsoft.com/en-us/library/aa394582%28v=vs.85%29.aspx
# http://technet.microsoft.com/en-us/library/bb742610.aspx

def val2addr(val):
	addr = ""
	for ch in val:
		addr += ("02x "% ord(ch))
	addr = addr.strip(" ").replace(" ",":")[0:17]
	return addr

# Grabs key from Windows registry, loops through extracting
# network name and DefaultGatewayMAC

# from python-registry import *
import sys
# from Registry import Registry
from winreg import *
# Prints all keys in a Registry

def rec(key, depth=0):
	print("\t" * depth + key.path())
	for subkey in key.subkeys():
		rec(subkey, depth + 1)

def printNets(reg = ""):
	net = "Network"
	# net = "SOFTWARE"
	# NOTE: The below method call appears specific to Windows-7.  
	# The 'network' subkey in localhost doesn't exist, per se.  It merely references the subkey as
	# it exists in the user.
	# http://serverfault.com/questions/522065/missing-hkcu-network-subkey-when-browsing-registry-remotely-with-powershell
	# Below code does not print anything as that registry file appears to be empty, along with
	# the other network reg files to which I have access.
	with OpenKey(HKEY_CURRENT_USER, net) as key:
		print("\n[*] Networks You have Joined.")
		for i in range(100):
			try:
				guid = EnumKey(key, i)
				with OpenKey(key, str(guid)) as netKey:
					(n, adrr, t) = EnumValue(netKey, 5)
					(n, name, t) = EnumValue(netKey, 4)
					macAddr = val2addr(addr)
					netName = str(name)
					print('[+]' + netName + ' ' + macAddr)
			except:
				print("Something happened")
				# break
	# reg = Registry.Registry(reg or "SOFTWARE\\Microsoft\Windows NT\\Current Version\\NetworkList\\Signatures\\Unmanaged")
	# rec(reg.root())





# Create an instance of mechanize browser
# Open the wigle.net page
# encode username and password as parameteres and request 
# a login at the Wigle login page
# Once logged in, creates an HTTP post using parameter 
# the parameter netid as the MAC address to search the 
# database

# import mechanize, urllib, re, urlparse


def main():
	printNets()

if __name__ == "__main__":
	main()

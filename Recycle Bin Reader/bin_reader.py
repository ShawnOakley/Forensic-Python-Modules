import os
from winreg import *
import optparse

# Good model for variability between OS versions
# In this case, the code handles differences b/t
# (1) Windows 98 and other FAT file systems, (2) NTFS systems such as Windows NT, 2000, and XP
# and (3) Windows Vista and Windows 7

def returnDir():
	dirs=['C:\\Recycler\\', 'C:\\Recycled\\', 'C:\\$Recycle.Bin\\']
	for recycleDir in dirs:
	  	if os.path.isdir(recycleDir):
	  		return recycleDir
	return None

def sid2user(sid):
	try: 
		key = OPENKey(HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList" + '\\' + sid)
		(type, value) = QueryValueEx(key, 'ProfileImagePath')
		user = value.split('\\')[-1]
		return user
	except:
		return sid

def findRecycled(recycleDir):
	dirList = os.listdir(recycleDir)
	for sid in dirList:
		files = os.listdir(recycleDir + sid)
		user = sid2user(sid)
		print ('n[*] Listing Files for User: ' + str(user))
		for file in files:
			print ('[+] Found File: ' + str(file))

def main():
	recycleDir = returnDir()
	findRecycled(recycleDir)

if __name__ == '__main__':
	main()
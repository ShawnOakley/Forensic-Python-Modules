#!/usr/bin/python

import guestfs
import hivex

# The name of a Windows virtual machine on this host.  This
# example script makes some assumptions about the registry
# location and contents which only apply on Windows Vista
# and later versions.
# Adapted from http://rwmj.wordpress.com/2010/11/28/use-hivex-from-python-to-read-and-write-windows-registry-hive-files/
windows_domain = "Win7x32"

# Username on the Windows VM.
username = "rjones"

# Use libguestfs to download the HKEY_CURRENT_USER hive.
g = guestfs.GuestFS ()
g.add_domain (windows_domain, readonly=1)
g.launch ()

roots = g.inspect_os ()
root = roots[0]
g.mount_ro (root, "/")

path = "/users/%s/ntuser.dat" % username
path = g.case_sensitive_path (path)
g.download (path, "/tmp/ntuser.dat")

# Use hivex to pull out a registry key.
h = hivex.Hivex ("/tmp/ntuser.dat")

key = h.root ()
key = h.node_get_child (key, "Software")
key = h.node_get_child (key, "Microsoft")
key = h.node_get_child (key, "Internet Explorer")
key = h.node_get_child (key, "Main")

val = h.node_get_value (key, "Start Page")
start_page = h.value_value (val)
#print start_page

# The registry key is encoded as UTF-16LE, so reencode it.
start_page = start_page[1].decode ('utf-16le').encode ('utf-8')

print "User %s's IE home page is %s" % (username, start_page)
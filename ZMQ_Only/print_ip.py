# Sample code to get IP addresses associated with every interface on our host
# This will make the code decoupled from whether we are in mininet emulated host
# or otherwise. The gethostbyname () typically will read the /etc/hosts and then
# often end up giving our loopback address, particularly on mininet hosts.
#
# For example, my VM is called CourseVM (which is its hostname). The /etc/hosts file
# has 127.0.1.1 listed against this hostname. Thus, a simple gethostbyname will return
# this IP address, which may not be useful in many circumstances.
#
# Instead, we use a different approach.  This and several other approaches are mentioned at this link:
# https://stackoverflow.com/questions/24196932/how-can-i-get-the-ip-address-from-a-nic-network-interface-controller-in-python

import netifaces as ni

# retrieve all the attached interfaces
intfs = ni.interfaces ()
print ("********  Detailed information ************")
for intf in intfs:
  print ("IP addresses associated with interface {} are {}".format (intf, ni.ifaddresses (intf)))

# The above prints a lot of information. We need the AF_INET part, which is numbered 2 and then we retrieve
# the 0th entry and the "addr" field of the dictionary entry.
print ("********  IPv4 Addresses ************")
for intf in intfs:
  print ("IPv4 address associated with interface {} are {}".format (intf, ni.ifaddresses (intf)[ni.AF_INET][0]['addr']))

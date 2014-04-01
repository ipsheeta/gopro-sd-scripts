from scapy.all import *

# we've set a range for the 27 camera IPs using dnsmasq.conf dhcp-range
IP_dest = "10.0.0.3/20"
cam_port = 8484

remote:10.71.79.1
gopro:10.71.79.2

command_turn_on = srloop(IP(dst=IP_dest)/UDP(dport=cam_port)

command_record = 

command_stop = 


gp_packets = rdpcap("/home/ipsheeta/Downloads/gopropackets.pcap")

>>> a = gp_packets[2112][UDP]
>>> a
<UDP  sport=4200 dport=8484 len=22 chksum=0x0 |<Raw  load='\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\xc8lc\x05' |<Padding  load='S\x19<\xc8' |>>>

def udp_test(x):
   try:
      x[UDP]
      return True
   except IndexError:
      return False

>>> udp_packets=gp_packets.filter(udp_test)

#what are you? 
initial = '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00cv'


from scapy.all import *
import sys
import time

conf.iface = 'wlan0'
answer = []
unanswer = []

def send_command(cmd):
	ans, unans = sr(IP(src="10.0.0.1",dst="10.0.0.11")/UDP(sport=4000,dport=8484)/str(cmd))
	return ans, unans

def output(cmd):
	response = send_command(cmd)
	return response[0][UDP][0]

def packet_explorer(filepath):
	with open(filepath, 'r') as commands:
		for i, line in enumerate(commands):
			print i
			ans, unans = sr(IP(src="10.0.0.1",dst="10.0.0.11")/UDP(sport=4000,dport=8484)/str(line[:-1]),timeout=10)
			answer.append(ans)
			unanswer.append(unans)
			raw_input('continue')
	return answer

if __name__ == '__main__':
	packet_explorer(sys.argv[1])

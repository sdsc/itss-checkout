# Author: Nathaniel Moreno
# Purpose: Reports the IP Address and Expiring date of all SSL Certs in the given IP range
# Status: Awaiting completion
# TODO:

import iptools # pip install iptools - provides ip handling
from subprocess import call # provides calls to terminal function
import urllib
import subprocess 

ipSpace = dict(
	test='173.194.207.139' # google.com
)

# terminal commands
com1 = "timeout 2s echo | openssl s_client -connect "

# parses the certificate as if it were DER encoded
com2 = ":443 2>/dev/null | openssl x509 -inform der -noout -dates"

f = open('ssl_checkList.txt', 'w')

# loops through all IP-Spaces
for key in ipSpace.keys():
	
	# r is a list of all valid IPs in IP-Space
	r = iptools.IpRangeList(ipSpace[key])
	
	for ip in r: 
		# resets value of output
		output = None
		
		# flag for handling error
		flag = 0
		
		# executes terminal command with ip
		try:
			output = subprocess.check_output([com1+ ip +com2], shell=True)
		except subprocess.CalledProcessError as e:
			output = e.output
		
		try:
			nl_index = output.index("\n")
		except:
			result = ip + " - error"
			flag = 1
			pass
		
		if (not flag):
			result = ip + " " + output[nl_index+1:len(output)-1]
		
		f.write(result)
f.close()


# here for parsing file produced above
def parseData(in_filename):
        for line in urllib.urlopen(in_filename):
                yield eval(line)

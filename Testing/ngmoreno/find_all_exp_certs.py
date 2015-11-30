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

com1 = "timeout 5s echo | openssl s_client -connect "
com2 = ":443 2>/dev/null | openssl x509 -noout -dates"
# -issuer -subject

f = open('ssl_checkList', 'w')

for key in ipSpace.keys():
	r = iptools.IpRangeList(ipSpace[key])
	for ip in r: 
		output = subprocess.check_output([com1+ ip +com2], shell=True)
		nl_index = output.index("\n")
		result = ip + " " + output[nl_index+1:len(output)-1]
		f.write(result)
f.close()


def parseData(in_filename):
        for line in urllib.urlopen(in_filename):
                yield eval(line)
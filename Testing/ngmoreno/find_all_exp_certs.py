# Author: Nathaniel Moreno
# Purpose: Reports the IP Address and Expiring date of all SSL Certs in the given IP range
# Status: Awaiting completion
# TODO:

import iptools # pip install iptools - provides ip handling
from subprocess import call # provides calls to terminal function
import urllib
import subprocess

# here for parsing file produced above
def parseData(in_filename):
    for line in urllib.urlopen(in_filename):
        yield line

# generate nmap for each ip in ipSpace
# example input: ipSpace = dict(test='google.com')
def generateNmap(ipSpace, output_filename):
    for key in ipSpace:
    
        # ips is a list of all valid IPs in IP-Space
        ips = iptools.IpRangeList(ipSpace[key])

        # for every ip, call nmap on it and write output to file
        for ip in ips:
            
            # resets output
            output = None
    
            # executes terminal command with ip
            
            # EXAMPLE OUTPUT --- begin ---
            # nmap 192.168.1.1
            #
            # Starting Nmap 6.40 ( http://nmap.org ) at 2016-01-11 10:45 PST
            # Nmap scan report for example-host.com (192.168.1.1)
            # Host is up (0.00025s latency).
            # Not shown: 999 closed ports
            # PORT   STATE SERVICE
            # 22/tcp open  ssh

            # Nmap done: 1 IP address (1 host up) scanned in 0.08 seconds
            # --- end ---
            
            try:
                output = subprocess.check_output(["nmap " + ip + ">> " + output_filename], shell=True)
            except subprocess.CalledProcessError as e:
                output = e.output




# parse nmap to get list of hosts and open ports
# returns dict: key:value == ip:[port1, port2, ... ]
def parseNmap(filename):
    ips = {}
    flag = 0
    for line in parseData(filename):
        if line == "\n":
            flag = 0
        words = line.split(" ")
        if words[0] == "Nmap":
            if len(words) == 5:
                ip = words[4]
            else: ip = words[5][1:len(words[5])-2]
            ips[ip] = []
        if flag == 1:
            port = words[0][:words[0].index("/")]
            ips[ip].append(port)
        if words[0] == "PORT":
            flag = 1
    return ips





# loops through all parsed IPs
def getAllSSL(ips)
    f = open('ssl_checkList.txt', 'w')
    for ip in ips:
        for port in ips[ip]:
            target = ip + ":" + port
            result = getSSL(target)
        f.write(result)
    f.close()





def getSSL(ip):
    # terminal commands
    # add this to parseSSLcom for DER encoded certs: -inform der
    getSSLcom = "timeout 2s echo | openssl s_client -connect "
    parseSSLcom = " 2>/dev/null | openssl x509 -noout -dates"
    
    # resets value of output
    output = None
        
    # executes terminal command with ip
    try:
        output = subprocess.check_output([getSSLcom+ target +parseSSLcom], shell=True)
    except subprocess.CalledProcessError as e:
        output = e.output
    
    # resets flag for handling error
    flag = 0
            
    try:
        nl_index = output.index("\n")
    except:
        result = target + " - error"
        flag = 1
        pass
            
    if (not flag):
        result = target + " " + output[nl_index+1:len(output)-1]

    return result



targets = dict(
)

nmap_filename = "nmap_data.txt"


nmap = generateNmap(targets,nmap_filename)
target_ips = parseNmap(nmap_filename)
getAllSSL(target_ips)


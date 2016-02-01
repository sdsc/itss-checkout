# Author: Nathaniel Moreno
# Purpose: Reports the IP Address and Expiring date of all SSL Certs in the given IP range
# Status: Awaiting completion
# TODO:

import iptools # pip install iptools - provides ip handling
from subprocess import call # provides calls to terminal function
import urllib
import subprocess
import pprint

class Window:
	
	def __init__(self):
		self.prompt = Tk()
		
		self.e_url  = Entry(self.prompt,width=15)

		self.e_url.grid(row=1,column=0) 		
		
		Button(self.prompt, text='Add Target', command=self.closePrompt).grid(row=5, column=0, sticky=W, pady=4)
		
		self.prompt.mainloop( )

	def closePrompt(self):
		self.url = str(self.e_url.get())

		self.e_url.delete(0,END)		
		
		self.prompt.quit()

	def getCreds(self):
		return [self.url, self.proxy, self.username, self.password]


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
        else:
	    words = line.split(" ")
            if words[0] == "Nmap" and words[1] == "scan":
                if len(words) == 5:
                    ip = words[4:len(words[4])-2]
                else: 
		    ip = words[5][1:len(words[5])-2]
                ips[ip] = []
            if flag == 1:
                port = words[0][:words[0].index("/")]
                ips[ip].append(port)
            if words[0] == "PORT":
                 flag = 1
    return ips





# loops through all parsed IPs
def getAllSSL(hostsDict, outFile):
    f = open(outFile, 'w')
    for host in hostsDict:
        for port in hostsDict[host]:
            result = getSSL(host+":"+port) + "\n"
        f.write(result)
    f.close()





def getSSL(host):
    # terminal commands
    # add this for DER encoded certs: -inform der
    command = "timeout 2s echo | openssl s_client -connect " + host + " 2>/dev/null | openssl x509 -noout -dates"
    
    # resets value of output
    output = None
        
    # executes terminal command with ip
    try:
        output = subprocess.check_output([command], shell=True)
    except subprocess.CalledProcessError as e:
        output = e.output
    
    # resets flag for handling error
    flag = 0
            
    try:
        nl_index = output.index("\n")
    except:
        result = host + " - error"
        flag = 1
        pass
            
    if (not flag):
        result = host + " " + output[nl_index+1:len(output)-1]

    return result

def filter_hosts_by_port(hosts,ports):
    outDict = {}
    for host in hosts:
	for port in ports:
	    if port in hosts[host]:
	        if outDict.get(host) == None:
		    outDict[host] = []
		outDict[host].append(port)
    return outDict		

def addTarget(target):
	targets["target" + str(len(targets))] = target


"132.249.20.53:8443 notAfter=Nov 16 23:59:59 2018 GMT"	
def parse_SSL_list(filename):
	expDates = {}
	for line in parseData(filename):
		content = line.split(" ")
		if len(content)>=6:
			ipaddress = content[0]
			month = content[1].split("=")[1]
			i = 0
			if len(content[2]) == 0: i += 1
			day = content[2+i]
			year = content[4+i]
			expDates[ipaddress] = [year,month,day] 
	return expDates

import time
def filter_by_date(inDict,monthsout):
	
	tyear = int(time.strftime('%Y'))
	tmonth = int(time.strftime('%m')) + monthsout
	tday = int(time.strftime('%d'))
	
	while tmonth > 12:
		tmonth -= 12
		tyear += 1

	monthDict = {	'Jan':1,
			'Feb':2,
			'Mar':3,
			'Apr':4,
			'May':5,
			'Jun':6,
			'Jul':7,
			'Aug':8,
			'Sep':9,
			'Oct':10,
			'Nov':11,
			'Dec':12
	}


	filtered = {}
	for key in inDict.keys():
		datetime = inDict[key]
		year = int(datetime[0]) 
		month = monthDict[datetime[1]]
		day = int(datetime[2])
		
		if tyear > year or (tyear==year and tmonth >= month):
			filtered[key] = datetime
	return filtered


	  
	  
	  
#TODO: add subnets to target list
targets = dict(
example='192.168.0.1/24',
)

nmap_filename = "nmap_data.txt"
#nmap = generateNmap(targets,nmap_filename)
#target_hosts = parseNmap(nmap_filename)

#TODO: Choose Ports to filter
filtered_hosts = filter_hosts_by_port(target_hosts,["443","8443"])

getAllSSL(filtered_hosts,'ssl_checkList.txt')

expDates = parse_SSL_list('ssl_checkList.txt')
filteredDict = filter_by_date(expDates,2)


import emailer
#TODO: Fill out parameters below
notifier = emailer.email_client("server","port","user@email.com","password")
email_to = ""

for key in filteredDict.keys():
	datetime = filteredDict[key]
	year = str(datetime[0])
	month = str(datetime[1])
	send_email(email_to,key,year + " " + month)




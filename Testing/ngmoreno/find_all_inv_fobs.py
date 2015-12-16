# Author: Nathaniel Moreno
# Purpose: Finds all invalid secureID FOBS
# Status: Awaiting completion
# TODO:


import logging
from subprocess import call
import subprocess
logging.basicConfig(level=logging.INFO)

#from Tkinter import *

def inFilter(inData, inKey, inFilterList):
	outData = []
	for datum in inData:
		for inFilter in inFilterList:
			if datum[inKey] == inFilter:
				outData.append(datum)
				break
	return outData

def outFilter(inData, inKey, inFilterList):
	outData = []
	for datum in inData:
		flag = True
		for inFilter in inFilterList:
			if datum[inKey] == inFilter:
				flag = False
		if flag == True:
			outData.append(datum)
	return outData

#class login:
#	
#	def __init__(self):
#		self.prompt = Tk()
#		
#		self.e_url  = Entry(self.prompt,width=15)
#		self.e_proxy= Entry(self.prompt,width=15)
#		self.e_user = Entry(self.prompt,width=15)
#		self.e_pass = Entry(self.prompt, show="b", width=15)
#
#		self.e_url.grid(row=1,column=0) 		
#		self.e_proxy.grid(row=2,column=0) 
#		self.e_user.grid(row=3,column=0) 
#		self.e_pass.grid(row=4,column=0)
#		
#		Button(self.prompt, text='Login', command=self.closePrompt).grid(row=5, column=0, sticky=W, pady=4)
#		
#		self.prompt.mainloop( )
#
#	def closePrompt(self):
#		self.url = str(self.e_url.get())
#		self.proxy = str(self.e_proxy.get())
#		self.username = str(self.e_user.get())
#		self.password = str(self.e_pass.get())
#
#		self.e_url.delete(0,END)		
#		self.e_proxy.delete(0,END)
#		self.e_user.delete(0,END)
#		self.e_pass.delete(0,END)
#		
#		self.prompt.quit()
#
#	def getCreds(self):
#		return [self.url, self.proxy, self.username, self.password]


# Produces Login GUI
#loginWindow = login()
#creds = loginWindow.getCreds()

# Set Parameters
#url = creds[0]
#proxy_url = creds[1]
#username = creds[2]
#password = creds[3]

col = ' "*" ' # this should be the columns required to reference the SecureID database"
table = ' "Employee Checkout" '
reqCol = ' "Status" '
reqVal = "Pending"


url = ""
proxy = ""
un = ""
pw = ""

class footprints_client:
	
	def __init__(self, username, password, url, proxy):
		self.username = username
		self.password = password
		self.url = url
		self.proxy = proxy
		self.connection_params = un+" "+pw+" "+url+" "+proxy

	def query(self, col, table, filterDict):
		command = "perl fpQuery.pl"
		command += " "
		
		for col in cols:
			command += col
			if len(cols) > 1:
				command += ","
		
		command += " "
		command += "from" + " " + table
		command += " "

		command += "where" + " "

		for key in filterDict.keys():
			command += key + " = " + fiterDict[key]
			command += " or "
	
		try:
			output = subprocess.check_output(com, shell=True)
		except:


client = footprints_client(un,pw,url,proxy)

# TODO: input correct filter value
# Search for pending
client.query("","",{'':''})



# Query secureID API
# TODO: Configure client to query secureID's API
#userData = 


# if ( user does NOT have FOB )
# - mark return status as NA
#usersNoFOB = inFilter(userData,'FOB',[False])


#updateStatus(usersNoFOB,"NA")


# if ( user has FOB AND if FOB has been revoked or returned )
# - mark return status as YES
# - else return status as NO
#usersWithFOb         =  inFilter(userData,'FOB',[True])

#usersWithFOBnolonger =  inFilter(usersWithFOb,'FOBstatus',["returned","revoked"])
#usersWithFOBstill    = outFilter(usersWithFOb,'FOBstatus',["returned","revoked"])

#updateStatus(usersWithFOBnolonger, "YES")
#updateStatus(usersWithFOBstill, "NO")





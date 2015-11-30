# Author: Nathaniel Moreno
# Purpose: Finds all invalid secureID FOBS
# Status: Awaiting completion
# TODO:


import logging
logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)

from Tkinter import *
from suds.client import Client

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

def updateStatus(inUserData,status):
	for user in inUserData:
		client.service.setStatus(user,status)

class login:
	
	def __init__(self):
		self.prompt = Tk()
		
		self.e_url  = Entry(self.prompt,width=15)
		self.e_proxy= Entry(self.prompt,width=15)
		self.e_user = Entry(self.prompt,width=15)
		self.e_pass = Entry(self.prompt, show="b", width=15)

		self.e_url.grid(row=1,column=0) 		
		self.e_proxy.grid(row=2,column=0) 
		self.e_user.grid(row=3,column=0) 
		self.e_pass.grid(row=4,column=0)
		
		Button(self.prompt, text='Login', command=self.closePrompt).grid(row=5, column=0, sticky=W, pady=4)
		
		self.prompt.mainloop( )

	def closePrompt(self):
		self.url = str(self.e_url.get())
		self.proxy = str(self.e_proxy.get())
		self.username = str(self.e_user.get())
		self.password = str(self.e_pass.get())

		self.e_url.delete(0,END)		
		self.e_proxy.delete(0,END)
		self.e_user.delete(0,END)
		self.e_pass.delete(0,END)
		
		self.prompt.quit()

	def getCreds(self):
		return [self.url, self.proxy, self.username, self.password]


loginWindow = login()
creds = loginWindow.getCreds()

url = creds[0]
proxy_url = creds[1]
username = creds[2]
password = creds[3]


client = Client(url)

# Proxy
d = dict(https=proxy_url)
client.set_options(proxy=d)

print client


# Authorization
#token = client.factory.create('AuthToken')
#token.username = username
#token.password = password
#client.set_options(soapheaders=token) 


# Query checkout
# TODO: Correct function and input paramaters
#checkoutData = client.service.checkout()


# TODO: Process response into dictionary if not already done


# Search for pending
#pendingData = filterData(checkoutData,'status',['pending'])


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





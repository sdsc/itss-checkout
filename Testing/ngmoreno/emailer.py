import smtplib
from email.mime.text import MIMEText


#TODO: Fill out email parameters below
class email_client:
	def __init__(self,server,port,username,password):
		self.SMTP_SERVER = server
		self.SMTP_PORT = port
		self.SMTP_USERNAME = username
		self.SMTP_PASSWORD = password
		self.EMAIL_FROM = username

	def send_email(self,emailTo, ipAddress, expDate):
		msg = MIMEText("The SSL Certificate for host at"+ipAddress+" is either expiring or has expired.\nExpiration Date: "+expDate)
		msg['Subject'] = "SSL EXPIRY NOTICE: " + ipAddress
		msg['From'] = self.EMAIL_FROM
		msg['To'] = emailTo
		debuglevel = True
		mail = smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT)
		mail.set_debuglevel(debuglevel)
		mail.starttls()
		mail.login(self.SMTP_USERNAME, self.SMTP_PASSWORD)
		mail.sendmail(self.EMAIL_FROM, emailTo, msg.as_string())
		mail.quit()

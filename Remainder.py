import MySQLdb
import sys
import calendar
import smtplib
from datetime import date
from email.mime.text import MIMEText
d = date.today()
d1 = str(d.strftime("%d.%m.%Y"))
def modify(d1) : 
	index = 0
	s = ''
	for i in d1 :
		if(index < 8) : 
			s = s + i
		else :
			s = s + 'X'
		index = index + 1
	return s
que = modify(d1)
s = smtplib.SMTP('smtp.gmail.com',587) #For gmail!
s.starttls()
s.login("user_name@gmail.com","password") #specify the user name and password.
connection = MySQLdb.connect (host = "localhost", user =" ",passwd = " ",db = "data_base_name") #connect to your mysql database!
cursor = connection.cursor ()
cursor.execute ('SELECT Number, Amount from insurancetable where Date = %s',(que,)) #the query gets executed
data = cursor.fetchall () #returns immutable python tuple
for row in data:
	message1 = str(row) #typecasting row to string. 
	msg = MIMEText('The insurance number and amount is mentioned in the parenthesis.'+message1)
	msg['Subject'] = 'Insurance Payment details'  
	s.sendmail("sender_email_id","reciever_email_id",msg.as_string()) #send the mail!
s.quit()
cursor.close ()
connection.close ()
sys.exit ()
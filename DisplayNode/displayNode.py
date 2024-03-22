import pyrebase 
import credentials
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Init
firebase = pyrebase.initialize_app(credentials.config) 
#connect to SQL database file
SQLconnect = sqlite3.connect("displayNode.db");
# Get a reference to the auth service
auth = firebase.auth()
# Log the user in
userToken = auth.sign_in_with_email_and_password(credentials.username, credentials.password)
db = firebase.database()
#Create a cursor to work with db
cursor = SQLconnect.cursor();

###Functions

#make SQL table match dictionary
def updateTable(dictionary, tableName):
	cursor.execute("DROP TABLE IF EXISTS "+tableName+";")

	#If the table is empty write nothing
	if dictionary.each() == None:
		return

	columns = "(id integer, "
	for key in dictionary.each()[0].val():
		typeName = "TEXT"
		#typeName = "INTEGER"
		#typeName = "REAL"
		columns += key +" "+ typeName +", "

	columns = columns.rstrip(", ")
	columns +=");"

	statement = "CREATE TABLE IF NOT EXISTS "+tableName+columns
	print(statement)
	cursor.execute(statement)

	for item in dictionary:
		values="("+item.key()+" , "
		keys="(id, "
		for column in item.val():
			keys+=column+", "
			test = db.child(tableName).child(item.key()).child(column).get(userToken)
			values+= "'"+str(test.val())+"'" +", "
		
		values = values.rstrip(", ")
		keys = keys.rstrip(", ")
		values+=")"
		keys+=")"
		statement = "insert into "+tableName+" "+keys+" values "+values+";"
		print(statement)
		cursor.execute(statement)

	SQLconnect.commit();



def sendEmail(address, subject, body):
	msg = MIMEMultipart()

	msg["From"] = credentials.email_user
	msg["To"] = address
	msg["Subject"] = subject

	msg.attach(MIMEText(body,"plain"))

	text = msg.as_string()
	server = smtplib.SMTP("smtp.gmail.com",587)
	server.starttls()
	server.login(credentials.email_user,credentials.email_password)

	server.sendmail(credentials.email_user,address,text)
	server.quit()

def updateTables():
	# read patients and write
	patients = db.child("patients").get(userToken)
	updateTable(patients, "patients")
	# read rules
	rules = db.child("rules").get(userToken)
	updateTable(rules, "rules")
	# read actuators
	actuators = db.child("actuators").get(userToken)
	updateTable(actuators, "actuators")
	# read sensors
	sensors = db.child("sensors").get(userToken)
	updateTable(sensors, "sensors")
	# read sensor data
	if sensors.each() != None:
		for sensor in sensors.each():
			sensorData = db.child("sensorData"+str(sensor.key())).get(userToken)
			print(sensorData.each())
			updateTable(sensorData, "sensorData"+str(sensor.key()))	

def fetchRules():
	print("todo")
	#result = cursor.execute('SELECT * FROM winds WHERE city=\''+inputCity+'\' ORDER BY date DESC LIMIT 1');
	#row = result.fetchone()


### MAIN
def main():
	print("main")
	updateTables()


if __name__ == '__main__':
	main()
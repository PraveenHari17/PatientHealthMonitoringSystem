import pyrebase 
import credentials
import sqlite3

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


### MAIN
def main():
	# read patients and write
	patients = db.child("patients").get(userToken)
	updateTable(patients, "patients")
	# read rules

	# read actuators

	# read sensors

	# read sensor data



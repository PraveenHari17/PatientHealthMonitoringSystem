import pyrebase 
import sqlite3
import auth
import sys
import os
import traceback
dir = os.getcwd()
dir = dir[0:dir.rfind("/")+1]
sys.path.insert(0, dir+'DisplayNode/')
import displayNode

#connect to SQL database file
SQLconnect = sqlite3.connect("displayNode.db");
#Create a cursor to work with db
cursor = SQLconnect.cursor();
SQLconnect.row_factory = sqlite3.Row;

def assertEquals(a, b) -> bool:
	if a == b:
		return True
	else:
		print(str(a)+" does not equal "+str(b))
		return False

def main(db, userToken) -> bool:
	try:
		displayNode.sendEmail("sysc3010l2g5.24@gmail.com", "Test", "Test body")
	except:
		print(traceback.format_exc())
		return False
	return True

#run main and capture result in exit code
db, userToken = auth.auth()
status = main(db, userToken)
print(status)
if status:
	exit(1)
else:
	exit(0)
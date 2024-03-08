import pyrebase 
import sqlite3
import auth
import sys
import os
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
	testsPassed=0
	testsRun=0
	#Read and asserts
	patients = db.child("patients").get(userToken)
	displayNode.updateTable(patients, "patients")
	#assert
	result = cursor.execute("SELECT * FROM patients");
	rows = result.fetchall()

	a = rows[0]
	b = (100, "Eva")
	print(a)
	print(b)
	testsPassed += int(assertEquals(a, b))
	testsRun += 1

	a = rows[1]
	b = (101, "Eva")
	print(a)
	print(b)
	testsPassed += int(assertEquals(a, b))
	testsRun += 1


	rules = db.child("rules").get(userToken)
	displayNode.updateTable(rules, "rules")
	#assert
	result = cursor.execute("SELECT * FROM rules");
	rows = result.fetchall()

	a = rows[0]
	b = (100, "1", "0", "<", "Temperature above 20C", "0", "20")
	print(a)
	print(b)
	testsPassed += int(assertEquals(a, b))
	testsRun += 1

	a = rows[1]
	b = (101, "1", "0", "<", "Temperature above 20C", "0", "20")
	print(a)
	print(b)
	testsPassed += int(assertEquals(a, b))
	testsRun += 1

	#Sum results
	print("Tests passed: "+testsPassed +" Tests Run: "+ testsRun)
	if testsPassed == testsRun:
		Print("All tests passed")
		return True
	else:
		Print(str(testsRun - testsPassed) +" tests Failed")
		return False

#run main and capture result in exit code
db, userToken = auth.auth()
status = main(db, userToken)
print(status)
if status:
	exit(1)
else:
	exit(0)
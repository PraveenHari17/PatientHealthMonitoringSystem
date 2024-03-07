import pyrebase 
import sqlite3
import auth
import sys
import os
dir = os.getcwd()
dir = dir[0:dir.rfind("/")+1]
sys.path.insert(0, dir+'DisplayNode/')
import displayNode

def main(db, userToken) -> bool:

	#Read and asserts
	#displayNode.updateTable()
	#assert

	return False

#run main and capture result in exit code
db, userToken = auth.auth()
status = main(db, userToken)
if status:
	exit(1)
else:
	exit(0)
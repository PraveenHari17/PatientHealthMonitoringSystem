import pyrebase 
import sqlite3
import run

def main(db, userToken) -> bool:
	# Run display node
	runFile("DisplayNode/displayNode.py", "DisplayNode/venv/bin/python")


	return false

#run main and capture result in exit code
db, userToken = auth.auth()
status = main(db, userToken)
if status:
	exit(1)
else:
	exit(0)
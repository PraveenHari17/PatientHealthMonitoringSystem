import auth
import pyrebase

def main(db, userToken) -> bool:
	print("Hello")
	return False;

db, userToken = auth.auth()
status = main(db, userToken)
if status:
	exit(1)
else:
	exit(0)
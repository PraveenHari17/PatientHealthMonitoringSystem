import auth
import pyrebase

def main(db, userToken) -> bool:
	print("Hello")
	return True;

#run main and capture result in exit code
db, userToken = auth.auth()
status = main(db, userToken)
if status:
	exit(1)
else:
	exit(0)
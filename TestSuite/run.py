import pyrebase 
import subprocess
import credentials
import populateDB
import depopulateDB
import os
import auth

#Run a test case and capture result in result using exit codes BLOCKING
def runTest(file, venv) -> bool:
	dir = os.getcwd()
	dir = dir[0:dir.rfind("/")+1]
	# Path to a Python interpreter that runs any Python script
	# under the virtualenv /path/to/virtualenv/
	python_bin = dir+venv

	# Path to the script that must run under the virtualenv
	script_file = dir+file

	process = subprocess.Popen([python_bin, script_file])
	result = process.wait()
	print(result)
	return result

#Run a python file
def runFile(file, venv) -> bool:
	dir = os.getcwd()
	dir = dir[0:dir.rfind("/")+1]
	# Path to a Python interpreter that runs any Python script
	# under the virtualenv /path/to/virtualenv/
	python_bin = dir+venv

	# Path to the script that must run under the virtualenv
	script_file = dir+file

	process = subprocess.Popen([python_bin, script_file])



#Authenticate to Firebase
db, userToken = auth.auth()

populateDB.main(db, userToken)
testsPassed = 0
testsRun = 0

#example
result = runTest("TestSuite/runTest.py", "DisplayNode/venv/bin/python")

#Display Node Test
testsPassed += runTest("TestSuite/displayNodeTest.py", "DisplayNode/venv/bin/python")
testsRun += 1

#Enviromental Control Node Test
runTest("TestSuite/end_to_end_1.py", "EnviromentalControlNode/venv/bin/python")
testsPassed += runTest("TestSuite/end_to_end2.py", "EnviromentalControlNode/venv/bin/python")
testsRun += 1


print("Tests passed: "+str(testsPassed) +" Tests Run: "+ str(testsRun))
print(str((testsPassed/testsRun)*100)+"% tests passing")
if testsPassed == testsRun:
	print("All tests passed")
else:
	print("Tests Failing")
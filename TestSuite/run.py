import pyrebase 
import subprocess
import credentials
import populateDB
import depopulateDB
import os
import auth

db, userToken = auth.auth()

#populateDB.main(db, userToken)







dir = os.getcwd()
dir = dir[0:dir.rfind("/")+1]
# Path to a Python interpreter that runs any Python script
# under the virtualenv /path/to/virtualenv/
python_bin = dir+"DisplayNode/venv/bin/python"

# Path to the script that must run under the virtualenv
script_file = dir+"TestSuite/runTest.py"

process = subprocess.Popen([python_bin, script_file])
result = process.wait()
print(result)

# L2-G5 Project

## [DisplayNode](DisplayNode/)
Sub-directory containing the files related to the display node. 

## [EnviromentalControlNode](EnviromentalControlNode/)
Sub-directory containing the files related to the enviromental control node. 

## [SensorNode](SensorNode/)
Sub-directory containing the files related to the sensor node. 

## [WebServer](WebServer/)
Sub-directory containing the files related to the web server and web site. 

## [TestSuite](TestSuite/)
Sub-directory containing the files related to the unit test suite. run.py executes the automated test suite that encapsulates the tests that could be automated.
There are also various other tests in this directory that cannot be automated such as testing the relays. 

## [WeeklyUpdate](WeeklyUpdates/)
Sub-directory containing the weekly WIPUR for all four group members. 

Group L2-G5 Projekt Asclepius

This repository contain all the nessecary files to run the Projekt Asclepius health monitoring system and test it's components.
To run the Projekt Asclepius health monitoring system there are four python scripts that must be run.

### Setup instructions

The sensor nodes must be connected to the sensors and the run SensorNode/unit test/comp_val_read.py which will collect the sensor data and send it to the firebase database.
The display node host the web server as well as the local database. On the display node run DisplayNode/displayNode.py this script will create the local SQL database and
send emails accoding to the automation rules that have been set. WebServer/app.py must also be run to start the web server the website can then be accessed. the enviromental
control node must be connected to the relays controlling the ventilation, heat and lights. Then run EnviromentalControlNode/ec_node.py This will then begin polling the database for the latest sensor data and compare it to the automation rules.

Run
DisplayNode/displayNode.py 
EnviromentalControlNode/ec_node.py
SensorNode/unit test/comp_val_read.py
WebServer/app.py

### Dependancies

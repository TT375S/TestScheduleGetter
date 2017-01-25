#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
args = sys.argv

timetable  = "timetable.txt"
A_schedule = "d_FA.txt"
C_schedules = ["d_FC_kikan.txt", "d_FC_sensin.txt", "d_FC_souzou.txt"]

if len(args) > 1 :
	timetable = args[1]
	for i in range(3):
		C_schedules[i] = args[i+2]


f_timeTable = open(timetable)

f_schedules = []
def openfiles():
	global f_schedules
	f_schedules = []
	f_schedules.append(open(A_schedule))	
	for i in range(3):
		f_schedules.append(open(C_schedules[i]) )
	
openfiles()
		

foundSchedules = []
def searchSchedule(className):
	global foundSchedules
	for i in range(4):
		lines = f_schedules[i].readlines()
		for line in lines:
			if line.find(className.strip().replace("　", " ")) != -1:
				foundSchedules.append(line.strip())
				return True
	return False

className = f_timeTable.readline()
while className:
	openfiles()
#	print className.strip()
	if not searchSchedule(className):
		print className.strip()	
	className = f_timeTable.readline()

print "Content-type: text/html; charset=utf-8\n"
print """<html><meta charset="utf-8"><body>"""

for schedule in foundSchedules:
	print schedule

print "</body></html>"""

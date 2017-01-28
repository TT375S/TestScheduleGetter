#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
args = sys.argv

timetable  = "timetable.txt"
A_schedule = "d_FA.txt"
C_schedules = ["d_FC_kikan.txt", "d_FC_sensin.txt", "d_FC_souzou.txt"]

#受講している授業の一覧を引数で指定
if len(args) > 1 :
	timetable = args[1]
	for i in range(3):
		C_schedules[i] = args[i+2]

f_timeTable = open(timetable)

#使うファイル、時間割と各テストのスケジュールファイルを開く
f_schedules = []
def openfiles():
	global f_schedules
	f_schedules = []
	f_schedules.append(open(A_schedule))	
	for i in range(3):
		f_schedules.append(open(C_schedules[i]) )
	
openfiles()
		
#授業名から、スケジュールを検索する
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

#授業名一覧から全て検索していく
print "-------授業名一覧です。-------"
print "*...テストのある授業\n-...テストのない授業\n"
className = f_timeTable.readline()
while className:
	openfiles()
	if not searchSchedule(className):
		print "- "+ className.strip()
	else:
		print "* "+ className.strip()
	className = f_timeTable.readline()

print "\n-------テストスケジュール一覧--------\n"

#print "Content-type: text/html; charset=utf-8\n"
#print """<html><meta charset="utf-8"><body>"""

for schedule in foundSchedules:
	if schedule.find("Schedule") != -1:
		schedule = schedule[schedule.find("Schedule")+len("Schedule")+1:]
	print schedule

#print "</body></html>"""

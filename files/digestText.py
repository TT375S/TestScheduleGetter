#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

print "Content-type: text/html\n"
print "<html><body>This is my first WebApp. IT'S WORKS!</body></html>"


#扱いやすくdigestして別ファイルに保存します。

args = sys.argv

#コメントアウトせよ
input_file = args[1]
output_file = args[2] 

#input_file = "16FA.txt"
#output_file = "d_FA.txt"

f = open(input_file)
line = f.readline()

f_o = open(output_file, 'w')

time = "EMPTY_TIME"
date = "EMPTY_DATE"

def isTime(text):
	global time
	if text.find("～") != -1 and text.find("：") != -1 :
		time = text.rstrip()+" "
		return True
	return False

def isDate(text):
	global date
	if text.find("月") != -1 and text.find("日") != -1 :
		date = text.rstrip()+" "
		return True
	return False

while line :
	#if isTime(line):
	#	print 'hit!Time'
	#if isDate(line):
	#	print'hit!date'
	if not (isTime(line) or  isDate(line)) :
		f_o.write(date + time + line ) 
	line = f.readline()	

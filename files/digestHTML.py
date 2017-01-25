#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi
import sys

args = sys.argv

output_file = "timetable.txt"
f_o = open(output_file, 'w')

#引数指定なしならば、URLから取得
if len(args) == 1:
	input_file ="htmlsource.txt"
	form = cgi.FieldStorage()
	f_i = open(input_file, 'w')
	f_i.write(form['htmlsource'])
#引数があるなら、そのファイルからHTMLを読み込み
else :
	input_file = args[1]
	f_i = open(input_file)


line = f_i.readline()
className = "EMPTY_CLASSNAME"
while line:
	if line.find("w-col1") != -1:
		line = f_i.readline()
		line = f_i.readline()
		line = f_i.readline()
		className = line.strip(" ")
		f_o.write(className)
	line = f_i.readline()	


#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

#pdfからテキストファイルにしたものを、さらに扱いやすくdigestして別ファイルに保存します。
#第一引数がinputfile、第二引数がoutputfileです。
args = sys.argv

input_file = args[1]
output_file = args[2] 

#input_file = "16FA.txt"
#output_file = "d_FA.txt"

f = open(input_file)
line = f.readline()

f_o = open(output_file, 'w')

time = "EMPTY_TIME"
date = "EMPTY_DATE"

#時間を表す行が出てきたのか判別し、時間ならその内容を保持します
def isTime(text):
	global time
	if text.find("～") != -1 and text.find("：") != -1 :
		time = text.rstrip()+" "
		return True
	return False

#日にちを表す行が出てきたのか判別し、日にちならその内容を保持します
def isDate(text):
	global date
	if text.find("月") != -1 and text.find("日") != -1 :
		date = text.rstrip()+" "
		return True
	return False

#全ての行に対し、日にちか時間か判断し、そのどちらでもないならテスト名だと考えファイルに書き込みます。
#出力は日にち,日付,テスト名,先生,教室
while line :
	#if isTime(line):
	#	print 'hit!Time'
	#if isDate(line):
	#	print'hit!date'
	if not (isTime(line) or  isDate(line)) :
		f_o.write(date + time + line ) 
	line = f.readline()	

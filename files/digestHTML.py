#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi
import sys

args = sys.argv

output_file = "timetable.txt"
f_o = open(output_file, 'w')


if len(args) > 1:
#標準入力から読み込み
	if args[1] == "-l":
		print "course N@viのhtmlソースを貼り付けてください。入力終了はctrl+Dです。(Windowsではctrl+Z?)"
		input_file ="htmlsource.txt"
		form = sys.stdin.readlines()
		f_i = open(input_file, 'w')
		for line in form:
			f_i.write(line)
		#開き直さないと、f_i.readline()で一行目から読み込まれない。書き込んだ最後からの読み込みになってしまう。
		f_i = open(input_file)
#webからダウンロード
	elif args[1] == "-w":
		input_file ="htmlsource.txt"
		form = cgi.FieldStorage()
		f_i = open(input_file, 'w')
		f_i.write(form['htmlsource'])
		f_i = open(input_file)
#ファイルからHTMLを読み込み
	elif args[1] == "-f":
		input_file = args[2]
		f_i = open(input_file)
	else :
		print "オプションを指定してください"
else :
	print "オプションを指定してください"

#htmlソースから授業名を読み込んでいく。
#現在は、classがw-col1になっているとこの3行下に必ず授業名があるためこうしている。htmlパーサ？とかそういうのを使った方がスマートだし変更されてもなんとかなるはず
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

print "受講している授業名の、htmlからの抽出が終了しました。"

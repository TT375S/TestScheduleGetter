#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import subprocess

args = sys.argv
cmd_update = ["update.py ", "digestText.py "]
fileNames = ["FA.txt", "FC_kikan.txt", "FC_sensin.txt", "FC_souzou.txt"]
python = "python "

subprocess.call(python + cmd_update[0], shell = True)
for i in range(4):
	subprocess.call(python + cmd_update[1] + fileNames[i] + " d_"+ fileNames[i], shell= True )

cmd_search = ["digestHTML.py -l", "search.py" ]

subprocess.call(python + cmd_search[0], shell = True)
subprocess.call(python + cmd_search[1], shell = True)



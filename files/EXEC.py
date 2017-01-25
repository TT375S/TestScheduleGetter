#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import subprocess

args = sys.argv
cmd_update = ["update.py ", "digestText.py "]
pdfText = ["16FA.txt", "16FC_kikan.txt", "16FC_sensin.txt", "16FC_souzou.txt"]
digestedText = ["d_FA.txt", "d_FC_kikan.txt", "d_FC_sensin.txt", "d_FC_souzou.txt"]
python = "python "

subprocess.call(python + cmd_update[0], shell = True)
for i in range(4):
	subprocess.call(python + cmd_update[1] + pdfText[i] + " "+ digestedText[i], shell= True )

cmd_search = ["digestHTML.py anohtml.txt", "search.py" ]

subprocess.call(python + cmd_search[0], shell = True)
subprocess.call(python + cmd_search[1], shell = True)



#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess

url = "https://www.waseda.jp/fsci/assets/uploads/2017/01/"


input_f = "16_F_ABgun.pdf"
output_f = "16FA.txt"
cmdwget = "wget -N "
subprocess.call(cmdwget + url + input_f, shell = True)

cmd = "pdftotext -raw  %s %s" % (input_f, output_f )
subprocess.call( cmd, shell=True  ) 

input_f = "16_F_C_27souzou.pdf"
output_f = "16FC_souzou.txt"
cmd = "pdftotext -raw %s %s" % (input_f, output_f )
subprocess.call(cmdwget + url + input_f, shell = True)
subprocess.call( cmd, shell=True  ) 

input_f = "16_F_C_26kikan-2.pdf"
output_f = "16FC_kikan.txt"
cmd = "pdftotext -raw %s %s" % (input_f, output_f) 
subprocess.call(cmdwget + url + input_f, shell = True)
subprocess.call( cmd, shell=True  )

input_f = "16_F_C_28sensin-1.pdf"
output_f = "16FC_sensin.txt"
cmd = "pdftotext -raw %s %s" % (input_f, output_f) 
subprocess.call(cmdwget + url + input_f, shell = True)
subprocess.call( cmd, shell=True  ) 

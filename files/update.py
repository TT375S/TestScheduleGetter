#!/usr/bin/python
# -*- coding: utf-8 -*-

#試験情報ページのhtmlからリンクを全て取り出し、その中で試験情報pdfファイルへのリンクからpdfをダウンロードし、
#pdftotextでtextファイルにします。
import subprocess
import urllib2
from bs4 import BeautifulSoup

#試験情報ページ
parentURL = "https://www.waseda.jp/fsci/students/exam/"
print "試験情報ページhttps://www.waseda.jp/fsci/students/exam/から試験情報を探しています..."
#subprocess.call("wget -O sourcePage.html " + parentURL, shell=True)
#f = open("sourcePage.html")
#html = f.readlines()

#htmlをスクレイピングしてリンクのURLを全て取り出していく
html = urllib2.urlopen(parentURL).read().decode('utf-8', 'ignore')
#print html
soup = BeautifulSoup(html, "html.parser")
links = [a.get("href") for a in soup.find_all("a")]

#生成するファイルの名前たち
fileNames =["FA", "FC_kikan", "FC_souzou", "FC_sensin"]

i=0
for link in links:
	#リンクにABやF_Cが含まれる場合は、試験情報pdfファイルへのリンクだとしてダウンロードしてpdftotext。
	if str( link).find("AB") != -1 or str(link).find("F_C")!=-1:
		subprocess.call("wget -O "+ fileNames[i] +".pdf " + link, shell = True)
		cmd = "pdftotext -raw  %s %s" % (fileNames[i]+".pdf", fileNames[i]+".txt" )
		subprocess.call( cmd, shell=True  )
		i = i+1 
	
print "pdfのダウンロードとプレーンテキストへの変換が終了しました。"


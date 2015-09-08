# -*- coding: utf-8 -*-#
import sqlite3
import sys
import os
import subprocess

#url = subprocess.check_output("mpc current", shell=True)
#url = url.strip()

#print "Looking for:", url
#open playlist for overwrite
fo = open("myplaylist.m3u", "w+")

con = sqlite3.connect('radio.db')
con.row_factory =sqlite3.Row

with con:

	cur = con.cursor()
	cur.execute("SELECT * FROM stations")
	while True:

		row = cur.fetchone()
		if row == None:
			break
		print row[0], row[1], row[2]
		fo.write(row[2] + "\n")
	
	#cur.execute("SELECT callsign FROM stations WHERE url LIKE ?", (url,))
	#row = cur.fetchone()
	#if row == None:
	#	print "Not found!"
	#print "I found this - ", row[0]
con.close()

fo.close()

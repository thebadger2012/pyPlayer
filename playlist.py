#!/usr/bin/env python

import cgi
import cgitb; cgitb.enable()
#import cmd_utils
import subprocess
import sqlite3

print """<ul class='media'>"""

dbname='/var/www/html/scripts/py/radio.db'
con = sqlite3.connect(dbname)
con.row_factory =sqlite3.Row
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM stations")
    while True:    
        row = cur.fetchone()
        if row == None:
            break
        print """
	<li id='%s'>""" % row[0]
        print """
	<span>%s</span>""" % row[0]
        print """
        <span>%s</span>""" %  row[1]
        print """
	</span>%s</span>""" % row[2]
        print """
        </li>"""
con.close()

print """</ul>"""

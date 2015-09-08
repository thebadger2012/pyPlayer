#!/usr/bin/env python

import re
import cgi
import cgitb; cgitb.enable()
import cmd_utils
import sqlite3

working_dir = "/tmp"
pattern = '[0-9]'

form = cgi.FieldStorage()
mpc_action = form.getvalue('action')
match = re.search(pattern, mpc_action)

def get_name(url):
    ''' Retrieves the station name for the url passed to this function '''
    dbname='/var/www/html/scripts/py/radio.db'
    url = url.strip()
    con = sqlite3.connect(dbname)
    con.row_factory =sqlite3.Row
    with con:
        cur = con.cursor()
        cur.execute("SELECT callsign FROM stations WHERE url LIKE ?", (url,))
        row = cur.fetchone()
        if row == None:
            station = "Radio Off"
        else:
            station = row[0]
    con.close()
    return station

if match == None:
    #
    # a command button was clicked
    #
    if mpc_action == "play":
        command = "mpc play "
        output = cmd_utils.run_cmd(command, working_dir)	
    if mpc_action == "next":
        command = "mpc next "
        output = cmd_utils.run_cmd(command, working_dir)
    if mpc_action == "prev":
        command = "mpc prev "
        output = cmd_utils.run_cmd(command, working_dir)
    if mpc_action == "stop":
        command = "mpc stop "
        output = cmd_utils.run_cmd(command, working_dir)
    if mpc_action == "vup":
        command = "mpc volume +5 "
        output = cmd_utils.run_cmd(command, working_dir)
    if mpc_action == "vdn":
        command = "mpc volume -5 "
        output = cmd_utils.run_cmd(command, working_dir)
else:
    #    
    # a url item was clicked
    #
    command = "mpc play " + mpc_action + " "
    output = cmd_utils.run_cmd(command, working_dir)
    
command = "mpc status "
output = cmd_utils.run_cmd(command, working_dir)
#print """<p>%s</p>""" % output
urlEnd = output.find('[')
output = get_name(output[0:urlEnd])
print """<p>%s</p>""" % output
print """<script>document.title = '""" + output + """'</script>"""


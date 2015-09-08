#
import sqlite3 as lite
import sys

con = None

try:
	con = lite.connect('radio.db')

	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS stations")
	cur.execute("CREATE TABLE stations(id INTEGER PRIMARY KEY, callsign TEXT, url TEXT)")
	cur.execute("INSERT INTO stations(callsign, url) VALUES('CBC Radio One:London 1', 'http://3373.live.streamtheworld.com:80/CBC_R1_LDN_L_SC')")
	cur.execute("INSERT INTO stations(callsign, url) VALUES('CBC Radio One:London 2', 'http://3373.live.streamtheworld.com:3690/CBC_R1_LDN_L_SC')")
	cur.execute("INSERT INTO stations(callsign, url) VALUES('CBC Radio One:London 3', 'http://3373.live.streamtheworld.com:443/CBC_R1_LDN_L_SC')")
	cur.execute("INSERT INTO stations(callsign, url) VALUES('AM980:CFPL London','http://live.leanstream.co/CFPLAM?type=.flv&playertype=socast1')")
	con.commit()

except lite.Error, e:

	if con:
		con.rollback()

	print "Error %s:" % e.args[0]
	sys.exit(1)

finally:

	if con:
		con.close()


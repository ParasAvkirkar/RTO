import sqlite3


def insertRTO(rtocode, district, territory):
	try:
		conn = sqlite3.connect('rto.db')

		print "Database opened successfully"
		# conn.execute('''CREATE TABLE codes(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
		# 				 rtocode TEXT NOT NULL UNIQUE, district TEXT, territory TEXT)''')
		parameters = (rtocode, district, territory)
		conn.execute('''INSERT INTO codes(rtocode, district, territory) VALUES(?, ?, ?)''', parameters)


		conn.commit()
		conn.close()
	except sqlite3.Error as e:
	        print "An error occurred:"
	        for a in e.args:
	        	print a

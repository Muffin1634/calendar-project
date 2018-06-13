import sqlite3

conn = sqlite3.connect('calendar.db') # database file
c = conn.cursor() # create cursor

c.execute('''CREATE TABLE IF NOT EXISTS dates (
	month INTEGER,
	day INTEGER,
	year INTEGER,
	name TEXT,
	jobid INTEGER 
	)''')
# the id is for identifying which job is being selected
# have a manual insertion fix currently but need to automate id creation later
c.commit()

def assignment(arguments):
	arguments = arguments.replace("", "\n")
	data = []
	for line in data: # splits the data and isolates them in list entries.
		data.append(line)  
		month = data[0]
		day = data[1]
		year = data[2]
		name = data[3]
		jobid = data[4]
	sql_insert = str("INSERT INTO dates VALUES (month, day, year, name, jobid)")
	c.execute(sql_insert)
	c.commit()

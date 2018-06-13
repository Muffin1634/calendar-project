import sqlite3


conn = sqlite3.connect('calender.db') #database file

c = conn.cursor()#create cursor

try: #creates a table called dates. However, if there is a problem, like if 'dates' already exists, it just moves on.
	c.execute('''CREATE TABLE dates ( 

			month integer,
			day integer,
			year integer,
			name text

	)''')
	c.commit()
else:
	pass

c.commit()

def assignment(arguments):
	arguments = arguments.replace("", "\n")
	data = []
	for line in data: #splits the data and isolates them in list entries.
		data.append(line)  
		month = data[1]
		day = data[2]
		year = data[3]
		name = data[4]
	sql_insert = str("INSERT INTO dates VALUES ("month", " day", " year", "name")")
	c.execute(sql_insert)
	
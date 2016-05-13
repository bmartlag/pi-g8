import MySQLdb
db = MySQLdb.connect("localhost", "root", "raspberry", "eyebaby")
cursor = db.cursor()
query = ("""
	INSERT INTO test (str) 
	VALUES 
	('essai')
""")
cursor.execute (query)
db.commit()
db.close()
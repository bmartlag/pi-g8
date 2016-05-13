import MySQLdb
db = MySQLdb.connect("localhost", "root", "raspberry", "eyebaby")
cursor = db.cursor()
query = ("""
	UPDATE test
	SET str='changement'
	WHERE
	str='essai' 
""")
cursor.execute (query)
db.commit()
db.close()
import MySQLdb

class DBConnection():

	__db = None
	
	def __init__(self):
		pass
		
	def __init__(self, hostName, userName, pwd, dbName):
		self.connect(hostName, userName, pwd, dbName)
		
	def connect(self, hostName, userName, pwd, dbName):
		self.__db = MySQLdb.connect(
			host=hostName, 
			user=userName, 
			passwd=pwd, 
			db=dbName)
	
	def getResults(self, query):
		cursor = self.__db.cursor()
		cursor.execute(query)
		return cursor.fetchall()
		
	def executeStatemement(self, statement):
		cursor = self.__db.cursor()
		cursor.execute(statement)
		
class DBConnectionDummy():
	
	def __init__(self):
		pass
		
	def __init__(self, hostName, userName, pwd, dbName):
		pass
		
	def connect(self, hostName, userName, pwd, dbName):
		pass
	
	# Should be able to define return value
	def getResults(self, query):
		return [(0,"http://www.yle.fi/uutiset/rss/uutiset.rss"),
				(1, "http://www.mtv3.fi/rss/uutiset.rss")]
		
	def executeStatemement(self, statement):
		pass
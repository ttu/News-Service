import time

class FeedSaver():

	__db = None 
	__queue = None
	__keepAlive = True
	__query = "SELECT * FROM News WHERE Url='{0}'"
	__insert = "INSERT INTO News (Title, Url, FeedID, Date) \
				VALUES ('{0}', '{1}', {2}, '{3}');"
	
	def __init__(self, db, queue):
		self.__db = db
		self.__queue = queue
		
	def execute(self, sleepTime):
		while self.__keepAlive:
			counter = 0
			while not self.__queue.empty():
				e = self.__queue.get()
				# check if url in db
				result = self.__db.getResults(self.__query.format(e[1]))
				if result == ():
					counter = counter + 1
					self.__db.executeStatemement(
						self.__insert.format(
							e[0].replace("'", ""), e[1], e[2], e[3]))
							
			if counter > 0:
				print "Saved rows: {0}".format(counter)
				
			time.sleep(sleepTime)
			
		print "Saver finished"
	
	def stop():
		self.__keepAlive = False
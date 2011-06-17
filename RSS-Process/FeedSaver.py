import time
import datetime

class FeedSaver():

	__repo = None 
	__queue = None
	__keepAlive = True
		
	def __init__(self, repo, queue):
		self.__repo = repo
		self.__queue = queue
		
	def execute(self, sleepTime):
		while self.__keepAlive:
			counter = 0
			while not self.__queue.empty():
				e = self.__queue.get()
				# check if url in db
				result = self.__repo.getNews(e[1])
				if result == ():
					counter = counter + 1
					self.__repo.addNews(
							e[0].replace("'", ""), e[1], e[2], e[3])
							
			if counter > 0:
				print "{0} - Saved rows: {1}".format(datetime.datetime.utcnow(), counter)
				
			time.sleep(sleepTime)
			
		print "Saver finished"
	
	def stop():
		self.__keepAlive = False
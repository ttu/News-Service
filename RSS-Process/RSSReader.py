import time

class RSSReader():

	__repo = None
	__fp = None
	__queue = None
	__keepAlive = True
	
	def __init__(self, repo, feedp, queue):	
		self.__repo = repo
		self.__fp = feedp
		self.__queue = queue
		
	def execute(self, sleepTime):
		while self.__keepAlive:			
			result = self.__repo.getFeeds()
			for record in result:
				# TODO: Should this be done is separate thread?
				d = self.__fp.parse(record[1])
				for entry in d['entries']:
					e = self.__parseRSSEntry(entry, record[0])
					self.__queue.put(e)
					
			time.sleep(sleepTime)
	
		print "Reader finished"
			
	def stop():
		self.__keepAlive = False
		
	# RSS Help function
	# entry should be multiple strings
	def __parseRSSEntry(self, entry, feedID):
		date = '{0}-{1}-{2} {3}:{4}:{5}'.format(
			entry.updated_parsed[0], 
			entry.updated_parsed[1], 
			entry.updated_parsed[2],  
			entry.updated_parsed[3],  
			entry.updated_parsed[4],  
			entry.updated_parsed[5])
			
		return entry.title.encode("utf-8"), \
				entry.link.encode("utf-8"), \
				feedID, date
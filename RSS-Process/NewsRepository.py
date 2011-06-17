class NewsRepository():

	__getFeedsQuery = "SELECT ID, Url FROM Feed"
	__getNewsQuery = "SELECT * FROM News WHERE Url='{0}'"
	__getAllNewsQuery = "SELECT * FROM News"
	__getUsersQuery = "SELECT * FROM User"
	__getUserQuery = "SELECT * FROM User WHERE Name='{0}'"
	
	__insertFeed = "INSERT INTO Feed (Name, Url) VALUES ('{0}', '{1}');"
	__insertUser = "INSERT INTO User (Name) VALUES ('{0}');"
	__insertNews = "INSERT INTO News (Title, Url, FeedID, Date) \
				VALUES ('{0}', '{1}', {2}, '{3}');"
	__insertVote = "INSERT INTO Vote (UserID, NewsID, Rate, Date) VALUES ({0}, {1}, {2}, '{3}');"
				
	def __init__(self, db):
		self.db = db
		
	def addUser(self, name):
		self.db.executeStatemement(
			self.__insertUser.format(name))
		
	def addFeed(self, feedName, url):
		self.db.executeStatemement(
			self.__insertFeed.format(feedName, url))
		
	def addNews(self, title, url, feedID, date):
		self.db.executeStatemement(
			self.__insertNews.format(
				title.replace("'", ""), url, feedID, date))
		
	def addVote(self, userID, newsID, rate, date):
		self.db.executeStatemement(
			self.__insertVote.format(
				userID, newsID, rate, date))
				
	def getUser(self, name):
		return self.db.getResults(self.__getNewsQuery.format(name))
	
	def getUsers(self):
		return self.db.getResults(self.__getUsersQuery)
	
	def getUserCount(self):
		return self.__getResultCount(self.__getUsersQuery)
		
	def getNews(self, url):
		return self.db.getResults(self.__getNewsQuery.format(url))
	
	def getNewsCount(self):
		return self.__getResultCount(self.__getAllNewsQuery)
		
	def getFeeds(self):
		return self.db.getResults(self.__getFeedsQuery)
		
	def __getResultCount(self, query):
		result = self.db.getResults(query)
		if result == None:
			return 0
		return len(result)
	
	def countUserMatches(self, date):
		pass
			
		
class NewsRepositoryDummy():

	feeds = [(0, "http://www.yle.fi/uutiset/rss/uutiset.rss"),
			(1, "http://www.mtv3.fi/rss/uutiset.rss")]
	news = [(0, "Title", "Some url", "2011-01-01")]
	user = [(0, "Timmy")]
	userCount = 5
	newsCount = 10
	
	def __init__(self, db):
		self.db = db
	
	def addUser(self, name):
		print "Add user: {0}".format(name)
		
	def addFeed(self, feedName, url):
		print "Add feed: {0}, {1}".format(feedName, url)
		
	def addNews(self, title, url, feedID, date):
		print "Add news: {0}, {1}, {2}, {3}".format(title, url, feedID, date)
		
	def addVote(self, userID, newsID, rate, date):
		print "Add vote: {0}, {1}, {2}, {3}".format(userID, newsID, rate, date)
		
	def getUser(self, name):
		return self.user
		
	def getUsers(self):
		return self.user
		
	def getUserCount(self):
		return self.userCount
		
	def getNews(self, url):
		return self.news
		
	def getNewsCount(self):
		return self.newsCount
		
	def getFeeds(self):
		return self.feeds
	
	def countUserMatches(self, date):
		pass
import sys

class NewsRepository():

	__getFeedsQuery = "SELECT ID, Url FROM Feed"
	__getNewsQuery = "SELECT * FROM News WHERE Url='{0}'"
	__getAllNewsQuery = "SELECT * FROM News"
	__getUsersQuery = "SELECT * FROM User"
	__getVotesQuery = "SELECT UserID, NewsID, Rate FROM Vote WHERE Date = '{0}'"
	__getVotesWithNewsIDQuery = "SELECT UserID, NewsID, Rate FROM Vote WHERE NewsID = {0}"
	__getUserQuery = "SELECT * FROM User WHERE Name='{0}'"
	__getUserVotes = "SELECT Rate FROM Votes WHERE UserID = {0} AND NewsID = {0}"
	__getTempMatches = "SELECT * FROM TempMatch"
	__getMatchValues = "SELECT Matches, Misses FROM UserMatch WHERE UserID_1 = {0} AND UserID_2 = {1}"
	
	__insertFeed = "INSERT INTO Feed (Name, Url) VALUES ('{0}', '{1}');"
	__insertUser = "INSERT INTO User (Name) VALUES ('{0}');"
	__insertNews = "INSERT INTO News (Title, Url, FeedID, Date) \
				VALUES ('{0}', '{1}', {2}, '{3}');"
	__insertVote = "INSERT INTO Vote (UserID, NewsID, Rate, Date) VALUES ({0}, {1}, {2}, '{3}');"
	__insertTemp = "INSERT INTO TempMatch VALUES ({0}, {1}, {2});"
	__insertLastUpdated = "INSERT INTO Stats (LastUpdated) VALUES ('{0}');"
	
	__replaceUserMatches = "REPLACE INTO UserMatch VALUES ({0}, {1}, {2}, {3}, '{4}');"
	__deleteTempMatches = "DELETE FROM TempMatch WHERE 1=1"
	
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
	
	def addTempMatch(self, userID_1, userID_2, value):
		self.db.executeStatemement(self.__insertTemp.format(
			userID_1, userID_2, value))
		
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
	
	def getVotes(self, date):
		return self.db.getResults(self.__getVotesQuery.format(date))
	
	def getVotesWithNewsID(self, newsID):
		return self.db.getResults(self.__getVotesWithNewsIDQuery.format(newsID)) 
		
	def getTempMatches(self):
		return self.db.getResults(self.__getTempMatches)
		
	def getMatchValues(self, userID_1, userID_2):
		return self.db.getResults(self.__getMatchValues.format(userID_1, userID_2))
		
	def deleteTempMatches(self):
		self.db.executeStatemement(self.__deleteTempMatches)
		
	def insertOrUpdateUserMatch(self, userID_1, userID_2, match, miss, date):
		self.db.executeStatemement(self.__replaceUserMatches.format(userID_1, userID_2, match, miss, date))
		
	def updateLastUpdated(self, date):
		self.db.executeStatemement(self.__insertLastUpdated.format(date))
		
	def __getResultCount(self, query):
		result = self.db.getResults(query)
		if result == None:
			return 0
		return len(result)
		
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
	
	def getTempMatches(self):
		pass
		
	def getMatchValues(self, userID_1, userID_2):
		pass
		
	def deleteTempMatches(self):
		pass
		
	def insertOrUpdateUserMatch(self, userID_1, userID_2, match, miss):
		pass
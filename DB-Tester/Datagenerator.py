import sys
sys.path.append('..\RSS-Process')

import string
import random
import datetime
import DBConnection
import NewsRepository

class DummyDataGenerator():
	
	def __init__(self, repo):
		self.repo = repo
		
	def generatedata(self, userCount, feedCount, newsCount, date):
		self.generateUsers(userCount)
		self.generateFeeds(feedCount)
		self.generateNews(newsCount, feedCount, date)
		
	def generateUsers(self, count):
		for i in range(0, count):
			self.__generateUser(i)
		
	def generateNews(self, count, feedCount, date):
		for i in range(0, count):
			feedID = random.randint(1, feedCount)
			self.__generateNews(i, feedID, date)
		
	def generateFeeds(self, count):
		for i in range(0, count):
			self.__generateFeed(i)
	
	def generateVotes(self, count, date):
		userCount = self.repo.getUserCount()
		newsCount = self.repo.getNewsCount()
		for i in range(0, userCount):
			voteCount = random.randint(1, count)
			for v in range(0, voteCount):
				try:
					newsID = random.randint(0, newsCount)
					up = random.randint(0, 1)
					self.__generateVote(i, newsID, up, date)
				except:
					pass
					#print "failed to insert vote"
		
	def countUserMatches(self, date):
		pass
		
	def __generateUser(self, i):
		username =  self.__generateRandomString(8)
		self.repo.addUser(username)
	
	def __generateFeed(self, i):
		name =  self.__generateRandomString(8)
		url =  self.__generateRandomString(8)
		self.repo.addFeed(name, url)
		
	def __generateVote(self, userID, VoteID, rate, date):
		self.repo.addVote(userID, VoteID, rate, date)
		
	def __generateNews(self, i, feedID, date):
		title = self.__generateRandomString(8)
		url = self.__generateRandomString(10)
		self.repo.addNews(title, url, feedID, date)
		
	def __generateRandomString(self, length):
		return ''.join(random.choice(string.ascii_lowercase) for x in range(length))
		
	def __generateDate(self, year, month, day):
		return "{0}-{1}-{2} 12:13:34".format(year, month, day)
		
def main():
	db = DBConnection.DBConnection("localhost", "root", "", "NewsService_Test")
	repo = NewsRepository.NewsRepository(db)
	ddg = DummyDataGenerator(repo)

	start = datetime.datetime.utcnow()
	
	ddg.generateUsers(2000)
	repo.userCount = 2000
	ddg.generateFeeds(40)
	ddg.generateNews(5000, 40, "2011-06-01")
	repo.newsCount = 5000
	ddg.generateVotes(200, "2011-06-01")
	
	end = datetime.datetime.utcnow()
	timdelta = end - start
	
	print timdelta
	
if __name__ == '__main__':
	main()
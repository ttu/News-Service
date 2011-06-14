import feedparser

class Feedparser():
	
	def __init__(self):
		pass

	def parse(self, url):
		return feedparser.parse(url)

# Testing this takes too much time, should make dummy entry.
class FeedparserDummy():
	
	def __init__(self):
		pass

	def parse(self, url):
		return [("",""),("","")]
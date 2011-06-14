from DBConnection import DBConnection
from DBConnection import DBConnectionDummy
from MyFeedParser import Feedparser
from RSSReader import RSSReader
from FeedSaver import FeedSaver
from multiprocessing import Process, Queue

def main():
	fp = Feedparser()
	db = DBConnection("", "", "", "")
	q = Queue()
	
	rss = RSSReader(db, fp, q)
	saver = FeedSaver(db, q)
	
	readerProcess = Process(target=rss.execute, args=(10,))
	readerProcess.start()
	
	saverProcess = Process(target=saver.execute, args=(5,))
	saverProcess.start()

	readerProcess.join()
	saverProcess.join()
	
if __name__ == '__main__':
	main()
	
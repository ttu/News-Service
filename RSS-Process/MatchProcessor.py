class MatchProcessor():

	def __init__(self, repo):
		self.repo = repo
		
	def countUserMatches(self, date):
		votes = self.repo.getVotes(date)
		
		if votes != None:
			print "Found {0} votes".format(len(votes))
		
		for vote in votes:
			sameVotes = self.repo.getVotesWithNewsID(vote[1])
						
			#if sameVotes != None:
			#	print "Found {0} same votes for {1}".format(len(sameVotes), vote[1])
			
			for sameVote in sameVotes:
				#skip self
				if vote[0] == sameVote[0]:
					continue
				
				value = 0
				
				if sameVote[2] == vote[2]:
					# Users have same opinion
					value = 1
					
				try:
					# This prevents duplicates to TempMatches
					# e.g. 1 , 4 and 4 , 1 are same
					if vote[0] < sameVote[0]:
						self.repo.addTempMatch(vote[0], sameVote[0], value)
					else:
						self.repo.addTempMatch(sameVote[0], vote[0], value)
				except:				
					pass				
		
		# Update TempMatches to UserMatches
		tempMatches = self.repo.getTempMatches()
		
		if tempMatches != None:
			print "Found {0} tempmatches".format(len(tempMatches))
			
		for tempMatch in tempMatches:
			existingValues = self.repo.getMatchValues(tempMatch[0], tempMatch[1])
			
			match = 0
			miss = 0
			
			if tempMatch[2] == 1:
				match = 1
			else:
				miss = 1
			
			if existingValues != ():
				match = existingValues[0][0] + match
				miss = existingValues[0][1] + miss
				
			self.repo.insertOrUpdateUserMatch(tempMatch[0], tempMatch[1], match, miss, date)
			
		self.repo.deleteTempMatches()	
		self.repo.updateLastUpdated(date)
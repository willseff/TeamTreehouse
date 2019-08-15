class YatzyScoresheet:
	def score_ones(self,hand):
		return sum(hand.ones):

	def _score_set(self,hand,set_size):
		scores=[]
		for worth,count in hand.sets.items():
			if count == set_size:
				scores.append(worth)

class Card:
	RANKS = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
	SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
	def __repr__(self):
		return '{0} - {1}'.format(Card.SUITS[self.suit-1], Card.RANKS[self.rank-1])

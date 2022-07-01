# File: Hand.py
# Student: Kalei Ragland
#
# Date Created: 12/1/20
# Date Last Modified: 12/1/20
# Description of Program: Evaluates player's hand

import Card
from Deck import *

class Hand :
	def __init__ ( self , deck ):
		if ( len ( deck ) < 5 ):
			print ( " Not enough cards left !" )
			return None
		self . __cards = []
		self.__mysuits = [0] * 4
		self.__myranks = [0] * 13
		amount = 0
		rankNum = 0
		for i in range (5) :
			card = deck . deal () # deal next card
			self . __cards . append ( card ) # append to hand
			
			if card.getSuit() == "Spades":
				amount = self.__mysuits[0]
				amount += 1
				self.__mysuits[0] = amount
			elif card.getSuit() == "Diamonds":
				amount = self.__mysuits[1]
				amount += 1
				self.__mysuits[1] = amount
			elif card.getSuit() == "Hearts":
				amount = self.__mysuits[2]
				amount += 1
				self.__mysuits[2] = amount
			elif card.getSuit() == "Clubs":
				amount = self.__mysuits[3]
				amount += 1
				self.__mysuits[3] = amount
				
		
			if card.getRank() == "Ace":
				rankNum = self.__myranks[0]
				rankNum += 1
				self.__myranks[0] = rankNum
			elif card.getRank() == "Jack":
				rankNum = self.__myranks[10]
				rankNum += 1
				self.__myranks[10] = rankNum
			elif card.getRank() == "Queen":
				rankNum = self.__myranks[11]
				rankNum += 1
				self.__myranks[11] = rankNum
			elif card.getRank() == "King":
				rankNum = self.__myranks[12]
				rankNum += 1
				self.__myranks[12] = rankNum
			else:
				rankNum = self.__myranks[int(card.getRank())-1]
				rankNum += 1
				self.__myranks[int(card.getRank())-1] = rankNum
				
				
				
			
	
	def __str__ ( self ):
		result = ""
		for card in self . __cards :
			result = result + str ( card ) + "\n"
		return result
	
	
	def getCard ( self , i ):
		if (0 <= i <= 4) :
			return self . __cards [ i]
		else :
			return None
			
	def getMySuits(self):
		return self.__mysuits
		
	def getMyRanks(self):
		return self.__myranks
			
			
	def hasRoyalFlush(self):
		if(self.__myranks[0] == 1 and self.__myranks[9] == 1
		and self.__myranks[10] == 1 and self.__myranks[11] == 1
		and self.__myranks[12] == 1 and (self.__mysuits[0] == 5
		or self.__mysuits[1] == 5 or self.__mysuits[2] == 5
		or self.__mysuits[3] == 5)):
			return True
		else:
			return False
	
	def hasStraightFlush(self):
		for i in range(9):
			if(self.__myranks[i] and self.__myranks[i+1] and self.__myranks[i+2]
			and self.__myranks[i+3] and self.__myranks[i+4] and (self.__mysuits[0]==5
			or self.__mysuits[1] == 5 or self.__mysuits[2] == 5
			or self.__mysuits[3] == 5)):
				return True
		return False
	def hasFourOfAKind(self):
		count = 0
		for i in range(13):
			if self.__myranks[i] == 4:
				return True
		return False
			
	def hasFullHouse(self):
		threeSame = False
		pair = False
		
		for i in range(13):
			if self.__myranks[i] == 2:
				pair = True
			elif self.__myranks[i] == 3:
				threeSame = True
		if threeSame and pair:
			return True
		else:
			return False
			
			
	def hasFlush(self):
		for i in range(13):
			if self.__mysuits[i] == 5:
				return True
			else:
				return False
	
	
	def hasStraight(self):
		for i in range(9):
			if(self.__myranks[i] == 1 and self.__myranks[i+1] == 1
			and self.__myranks[i+2] == 1 and self.__myranks[i+3] == 1
			and self.__myranks[i+4] == 1):
				return True
		return False
		
	
	def hasThreeOfAKind(self):
		for i in range(13):
			if self.__myranks[i] == 3:
				return True
		return False
		
		
	def hasTwoPair(self):
		count = 0
		for i in range(13):
			if self.__myranks[i] == 2:
				count+=1
		if count == 2:
			return True
		else:
			return False
			
	
	def hasPair(self):
		for i in range(13):
			if self.__myranks[i] == 2:
				return True
		return False
	
	
	
	def evaluateHand(self):
		if self.hasRoyalFlush():
			return "Royal Flush"
		elif self.hasStraightFlush():
			return "Straight Flush"
		elif self.hasFourOfAKind():
			return "Four of a kind"
		elif self.hasFullHouse():
			return "Full House"
		elif self.hasFlush():
			return "Flush"
		elif self.hasStraight():
			return "Straight"
		elif self.hasThreeOfAKind():
			return "Three of a kind"
		elif self.hasTwoPair():
			return "Two pair"
		elif self.hasPair():
			return "One Pair"
		else:
			return "Nothing"
			
		
			
		
	
	

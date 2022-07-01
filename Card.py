# File: Card.py
# Student: Kalei Ragland
# 
# Date Created: 12/1/20
# Date Last Modified: 12/1/20
# Description of Program: A card class with a suit and rank

class Card :
	# These are class attributes , not instance attributes
	RANKS = ["Ace" , "2" , "3" , "4" , "5" , "6" , "7" , "8" ,
	"9" , "10" , "Jack" , "Queen" , "King" ]
	SUITS = [ 'Spades', 'Diamonds' , 'Hearts' , 'Clubs']
	


	def __init__ ( self , rank , suit ):
		if ( not rank in Card . RANKS or not suit in Card . SUITS ):
			print (" Not a legal card specification .")
			return
		self . __rank = rank
		self . __suit = suit
	
	
	def __str__ ( self ):
		return self . __rank + ' of ' + self . __suit
		
	def rankToIndex ( self,rank ) :
		# Converts a str rank to an index into RANKS
		return Card . RANKS . index ( rank )
	def __lt__ ( self , other ):
		return ( Card . rankToIndex ( self . __rank )
		< Card . rankToIndex ( other . getRank () ))
		
	def getRank(self):
		return self.__rank
		
	def getSuit(self):
		return self.__suit
		
		


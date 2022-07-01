# File: Deck.py
# Student: Kalei Ragland
#
# Date Created: 12/1/20
# Date Last Modified: 12/1/20
# Description of Program: A class that contains a list of cards, one for each rank and suit

import random
from Card import *

class Deck :
	def __init__ ( self ):
		self . __cards = []
		for suit in Card . SUITS :
			for rank in Card . RANKS :
				c = Card ( rank , suit )
				self . __cards . append (c)
		
	def shuffle ( self ) :
		random . shuffle ( self . __cards )
		
	def deal ( self ) :
		if len ( self ) == 0:
			return None
		else :
			return self . __cards . pop (0)
			
	def __len__ ( self ):
		return len( self . __cards )
		
	def __str__ ( self ) :
		result = ""
		for c in self . __cards :
			result = result + str ( c )
		return result




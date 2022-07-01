# File: Poker.py
# Student: Kalei Ragland
#
# Date Created: 12/1/20
# Date Last Modified: 12/1/20
# Description of Program: Deals and evaluates the given number of hands.

from Hand import *

def main():
	d = Deck()
	d.shuffle()
	amountHands = int(input("How many hands should I deal? "))
	count = 1
	while count <= amountHands:
		print("Hand Drawn (",count, "):")
		h = Hand(d)
		print(h)
		print(h.evaluateHand())
		print()
		
		if count % 10 == 0:
			print("Dealing a new Deck.")
			print()
			d = Deck()
			d.shuffle()
		count+=1
		
	
main()
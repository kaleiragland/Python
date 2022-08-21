# File: Project2.py
# Description of Program: Builds a prime factorization library

import math

def isprime(num):
	if num < 2 or num % 2 == 0:
		return num == 2
		
	div = 3
	while div <= math.sqrt(num):
		if num % div == 0:
			return False
		else:
			div += 2
	return True
	
def findNextPrime(num):
	if num < 2:
		return 2
	else:
		guess = num + 1
		while isprime(guess)!= True:
			guess += 1
		return guess

def factor(num):
	origNum = num
	primeList = []
	prime = 2
	if isprime(num):
		primes = [num]
		print("The prime factorization of", num,"is:", primes)
	else:
		while isprime(num) != True:
			while num % prime != 0:
				prime = findNextPrime(prime)
			primeList.append(prime)
			num = num / prime
			prime = 2
		primeList.append(int(num))
		print("The prime factorization of", origNum,"is:", primeList)
		

print("Welcome to the Prime factory!\n")
command = input("Enter a command (factor, isprime, end): ")
command2 = command.lower()
command2 = command2.strip()

while command2 != "end":
	if command2 != "factor" and command2 != "isprime" and command2 != "end":
		print("Command", command2,"not recognized. Try again!")
	elif command2 == "isprime":
		num = int(input("Enter an integer > 1: "))
		if num <= 1:
			print("Illegal input: ", num,"; input must be an integer > 1.", sep = "")
		else:
			if isprime(num):
				print("The number", num,"is prime")
			else:
				print("The number", num,"is not prime")
	elif command2 == "factor":
		num = int(input("Enter an integer > 1: "))
		if num <= 1:
			print("Illegal input: ", num,"; input must be an integer > 1.", sep = "")
		else:
			factor(num)
	print()
	command = input("Enter a command (factor, isprime, end): ")
	command2 = command.lower()
	command2 = command2.strip()
	
print("Thanks for using our service! Goodbye.", end = "")



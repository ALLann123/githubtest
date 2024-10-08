#!/usr/bin/python3
import random

def guess(x):
	random_number=random.randint(1,x)
	guess=0
	while guess!=random_number:
		guess=int(input(f"Guess a random number between 1 to {x}>>"))
		if guess<random_number:
			print("[-]Sorry Try Again!! Number is too low")
		elif guess>random_number:
			print("[-]Sorry Try Again!! Number is too high")
	print(f"[+]Yaiy,Congrats thats the correct number {random_number}")

x=int(input("[+]Enter the last Number to play in>>"))
guess(x)


""" rock-paper-scissors-lizard-spock
	program accepts one of the above inputs and returns a result
	return is win/lose/draw
"""

def rpsls(choice):	
	if choice== "rock": 
		Dictionary = {'lizard':0, 'spock':1, 'rock':2, 'paper':3, 'scissors':4}		
	elif choice== "paper": 
		Dictionary = {'spock':0, 'rock':1, 'paper':2, 'scissors':3, 'lizard':4}
	elif choice== "scissors": 
		Dictionary = {'rock':0, 'paper':1, 'scissors':2, 'lizard':3, 'spock':4}	
	elif choice== "lizard": 
		Dictionary = {'paper':0, 'scissors':1, 'lizard':2, 'spock':3, 'rock':4}
	elif choice== "spock": 
		Dictionary = {'scissors':0, 'lizard':1, 'spock':2, 'rock':3, 'paper':4}
	print Dictionary

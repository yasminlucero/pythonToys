""" rock-paper-scissors-lizard-spock
	program accepts one of the above inputs and returns a result
	returns score, a value of -1/0/1	
"""
def rpsls(choice):	
    name2num = {"rock":0, "paper":2, "scissors":4, "lizard":3, "spock":1}    
    num2name = {0:"rock", 2:"paper", 4:"scissors", 3:"lizard", 1:"spock"}    
    try: choiceNum = name2num[choice]
    except: TypeError
    try:import random as rand
    except: ImportError
    responseNum = rand.randint(0,4)
    response = num2name[responseNum]
    print 'computer chooses ' + response
    outcome = ((choiceNum-responseNum) % 5) > 2
    if outcome: 
        print "you lose" 
        score = -1
    elif choiceNum==responseNum: 
        print "tie"
        score = 0
    else: 
        print "you win"
        score = 1
    return score
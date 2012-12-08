## coin change problem
## exercise
## contact: yasmin.lucero@gmail.com
## Dec 2 2012

def changemaker(totalChange, fCPavailable = False):
    print "Note: Input assumed to be in dollar amount units. Amnts less than one cent will be rounded down to zero."
    coins = {"fiftyCentPieces":None, "quarters":0, "dimes":0, "nickels":0, "pennies":0}
    cents = int(totalChange * 100)
    cents = cents % 100
    if fCPavailable == True:
        coins["fiftyCentPieces"] = cents / 50
        cents = cents % 50    
    coins["quarters"] = cents / 25
    cents = cents % 25
    coins["dimes"] = cents / 10
    cents = cents % 10
    coins["nickels"] = cents / 5
    coins["pennies"] = cents % 5        
    return coins
    
def minCoins(totalChange, fCPavailable=False):
    a = changemaker(totalChange, fCPavailable)  
    cnt = a["quarters"]+a["dimes"]+a["nickels"]+a["pennies"]
    if(fCPavailable): cnt = cnt + a["fiftyCentPieces"]
    return cnt
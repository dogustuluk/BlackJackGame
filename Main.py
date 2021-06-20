import random
dealerCards = []

playerCards = []

while len(dealerCards) != 2:
    dealerCards.append(random.randint(1, 11))
    if len(dealerCards) == 2:
        print ("dealer has X &", dealerCards[1])
    
while len(playerCards) != 2:
    playerCards.append(random.randint(1, 11))
    if len(playerCards) == 2:
        print ("you have:", playerCards)

if sum(dealerCards) == 21:
    print("dealer has 21 and wins")
elif sum(dealerCards) > 21:
    print("dealer has busted")

while sum(playerCards) < 21:
    actionTaken = str(input("do you want to stay or hit?"))
    
    if actionTaken == "hit":
        playerCards.append(random.randint(1,11))
        print("you now have a total:"+ str(sum(playerCards)) + "from theese cards", playerCards)
    else:
        print("the dealer has a total of " + str(sum(dealerCards)) + "width ", dealerCards)
        print("you have a total of " + str(sum(playerCards)) + "with ", playerCards)
        
        if sum(dealerCards) > sum(playerCards):
            print("dealer wins")
            break
        else:
            print("player wins")
            break
if sum(playerCards) >21:
    print("you lose")
elif sum(playerCards) == 21:
    print("you have blackjack! you win")        
        

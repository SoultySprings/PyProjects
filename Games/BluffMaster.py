#The following is a game on two players bluffing, similar to the game between Cpt. Davy Jones and Will Turner in Potc 2
#The game assumes that there are only two players playing atm.

import numpy as np, random, sys

numberOfDices = 5
numberOfPlayers = 2
#BACKSIDE = backside
diceCircle = chr(9679)
diceDict = {
0: f''' _______ 
|???????| 
|???????| 
|_______| 
''',
1:f''' _______ 
|       | 
|   {diceCircle}   | 
|_______| 
''',
2:f''' _______ 
|{diceCircle}      | 
|       | 
|______{diceCircle}| 
''',
3:f''' _______ 
|{diceCircle}      | 
|   {diceCircle}   | 
|______{diceCircle}| 
''',
4:f''' _______ 
|{diceCircle}     {diceCircle}| 
|       | 
|{diceCircle}_____{diceCircle}| 
''',
5:f''' _______ 
|{diceCircle}     {diceCircle}| 
|   {diceCircle}   | 
|{diceCircle}_____{diceCircle}| 
''',
6:f''' _______ 
|{diceCircle}     {diceCircle}| 
|{diceCircle}     {diceCircle}| 
|{diceCircle}_____{diceCircle}| 
'''}


def main() :


    # print(diceDict[0])
    # print(diceDict[1])
    # print(diceDict[2])
    # print(diceDict[3])
    # print(diceDict[4])
    # print(diceDict[5])
    # print(diceDict[6])


    player_name1 = input("Enter the name of player 1 : ")
    player_name2 = input("Enter the name of player 2 : ")
    players = [player_name1, player_name2]
    playerCash = np.array([])
    playerDices = np.array([], dtype=np.int8)


    # for player in players :
    #     money = getBet();
    #     print(f"Bet money of {player} is : ${money}")
    #     playerCash += [money]
    # print(playerCash)
    playerDices = getDices()
    playerNum = 0
    for player in players :
        showDices(player, playerDices, False, playerNum)
        playerNum += 1


    while True:
        for player in players :
            getPlayerReponse(playerNum)
            if get
    #playerDices = playerDices.reshape((2,5))
    #for i in range(1,2):
    #    print(playerDices.)



def getBet() :
    bet = int(input("Enter the amount you want to bet : "))
    return bet

def getDices():
    userDices = np.random.randint(1,6,size=(numberOfPlayers, numberOfDices))
    print(userDices)
    return userDices

def showDices(NameofCurrentPlayer, playerDices, showOpponentHand, playerNumber) :
    # if showOpponentHand == False :
    #     for i in range(numberOfDices):
    #         print(diceDict[0],end="")
    # else :


    print(f"You ({NameofCurrentPlayer}'s) have the following dices :")
    for dice in playerDices[playerNumber,]:
        print(f"{diceDict[dice]}", end="")

    input("Press Enter to continue, if your opponent has closed his eyes...")

def getPlayerReponse(CurrPlayer) :
    print(f"Whats your guess - {CurrPlayer}? : ")
    PlayerDiceGuess = input("Enter Dice Upper Value Choice : ")
    PlayerNumDice = input("Enter the number of dices you guess are : ")
    PlayerLiarChoice = input("Do you think your opponent is bluffing? (Y) for Yes and (N) for No : ")
    if PlayerLiarChoice.lower() == "Y" :
        False
    return PlayerDiceGuess, PlayerNumDice, PlayerLiarChoice

def GameLogic(PlayerResponse, PlayerDiceGuess, PlayerNumDice) :
    if PlayerResponse


if __name__ == '__main__':
    main()
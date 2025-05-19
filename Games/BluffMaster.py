#The following is a game on two players bluffing, similar to the game between Cpt. Davy Jones and Will Turner in Potc 2
#The game assumes that there are only two players playing atm.

import numpy as np, random, sys

numberOfDices = 5
numberOfPlayers = 2

def main() :
    player_name1 = input("Enter the name of player 1 : ")
    player_name2 = input("Enter the name of player 2 : ")
    players = [player_name1, player_name2]
    playerCash = np.array([])
    playerDices = np.array([], dtype=np.int8)
    for player in players :
        money = getBet();
        print(f"Bet money of {player} is : ${money}")
        playerCash += [money]
    print(playerCash)
    playerDices = getDices()

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



if __name__ == '__main__':
    main()
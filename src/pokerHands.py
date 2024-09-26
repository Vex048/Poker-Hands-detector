import copy
class Hands:
    def __init__(self):
        self.player1hand = set()
        self.player2hand = set()
        self.player3hand = set()
        self.player4hand = set()
        self.flop = set()
        self.players = {0: self.flop, 1: self.player1hand, 2:self.player2hand, 3:self.player3hand, 4:self.player4hand}
    def addCard(self,card,turn,numberOfPlayers):
        enoughSpace = self.checkForLimit(turn)
        repetition = self.checkForRepetition(card,turn,numberOfPlayers)
        if enoughSpace == True and repetition == False:
            self.players[turn].add(card)
        else:
            return
    # Sprawdzic czy nie ma tych samych Kart w obydwu setach
    def checkForRepetition(self,card,turn,numberOfPlayers):
        counter = 0
        for hand in self.players:
            if hand == turn:
                continue
            else:
                if card not in self.players[hand]:
                    counter += 1
                else:
                    return True
        if counter == numberOfPlayers:
            return False

    def checkForLimit(self,number):
        if number != 0:
            if len(self.players[number]) < 2:
                return True
            else:
                return False
        else:
            if len(self.players[number]) < 5:
                return True
            else:
                return False
    def nextTurn(self,turn,numberOfPlayers):
        if turn >= numberOfPlayers:
            return 0
        elif turn > 0 and turn < numberOfPlayers:
            return turn + 1
        else:
            return 0
    def getHand(self,player):
        return self.players[player]

    def createHand(self,turn):
        tempList= list(self.flop)
        possibleHands = []
        toCheck=copy.deepcopy(self.players[turn])
        for i in range(len(tempList)):
            for j in range(i+1,len(tempList)):
                for k in range(j+1,len(tempList)):
                    toCheck.add(tempList[i])
                    toCheck.add(tempList[j])
                    toCheck.add(tempList[k])
                    possibleHands.append(toCheck)
                    toCheck=copy.deepcopy(self.players[turn])
        return possibleHands



if __name__ == "__main__":
    hands=Hands()
    hands.flop={"6C", "6H", "6K", "2G", "3C"}
    #hands.player1hand = {}
    hands.addCard("QC",1)
    hands.addCard("JC",1)
    #["AC", "AK", "AH", "6C", "6G"]
    #["3C", "6C", "2C"]
    possibleHands = hands.createHand(1)
    print(possibleHands)










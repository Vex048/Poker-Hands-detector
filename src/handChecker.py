import copy
class handChecker:

    def __init__(self):
        self.suits=[]
        self.ranks=[]
        self.possibleRanks=[]
        self.ranksNumerical = {"A": 14, "K": 13, "Q": 12, "J": 11, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5,
                               "4": 4, "3": 3, "2": 2}
        self.pokerHandRanks = {10: "Royal Flush", 9: "Straight Flush", 8: "Four of a Kind", 7: "Full House", 6: "Flush",
                      5: "Straight", 4: "Three of a Kind", 3: "Two Pair", 2: "Pair", 1: "High Card"}
        self.pokerHandRanksReversed = {"Royal Flush":10, "Straight Flush": 9, "Four of a Kind":8,  "Full House":7, "Flush":6,
                      "Straight":5, "Three of a Kind":4,  "Two Pair":3,  "Pair":2,  "High Card":1 }

    def clearHand(self):
        #self.cards.clear()
        self.possibleRanks.clear()
        self.suits.clear()
        self.ranks.clear()

    def findSuitsAndRanks(self,hand):
        for card in hand:
            self.suits.append(card[-1])
            self.ranks.append(self.ranksNumerical[card[0:-1]])
        self.ranks.sort()
    def printRanks(self):
        for rank in self.ranks:
            print(rank)
    def printSuits(self):
        for suit in self.suits:
            print(suit)
    def checkForHand(self,hand):
        self.findSuitsAndRanks(hand)
        self.ranks.sort()
        straight = False
        #Straight
        for i in range(len(self.ranks) - 1):
            if self.ranks[i] == self.ranks[i + 1] - 1:
                if i == 3:
                    straight = True
                    self.possibleRanks.append(5)
            else:
                break
        # Flush, RoyalFlush, StraightFlush
        if all(i == self.suits[0] for i in self.suits) == True:
            self.possibleRanks.append(6)
            if sum(self.ranks) == 60:
                self.possibleRanks.append(10)
            if 5 in self.possibleRanks:
                self.possibleRanks.append(9)
        temp = {}
        for rank in self.ranks:
            if rank not in temp:
                temp[rank] = 1
            else:
                temp[rank] += 1

        for k in temp:
            #Four of a kind
            if temp[k] == 4:
                self.possibleRanks.append(8)
            if temp[k] == 3:
                self.possibleRanks.append(4)
            if temp[k] == 2:
                if 2 in self.possibleRanks:
                    self.possibleRanks.append(3)
                else:
                    self.possibleRanks.append(2)
            if (temp[k] == 3 and 2 in self.possibleRanks) or (temp[k] == 2 and 4 in self.possibleRanks):
                self.possibleRanks.append(7)
        self.possibleRanks.append(1)

    def returnHand(self):
        hand = max(self.possibleRanks)
        self.clearHand()
        return hand

    def iterareThroughListOfHands(self,listOfHands):
        outputs= []
        for i in listOfHands:
            self.checkForHand(i)
            outputs.append(self.returnHand())
        indexOfMax=outputs.index(max(outputs))

        #print(self.pokerHandRanks[max(outputs)])
        score = max(outputs)
        return self.pokerHandRanks[score],listOfHands[indexOfMax],score

    def checkForSameHand(self,scores):
        bestScore = 0
        bestScoreindexes = []
        for i in range(len(scores)):
            if scores[i]>bestScore:
                bestScore = scores[i]
                bestScoreindexes.clear()
                bestScoreindexes.append(i)
            elif scores[i]==bestScore:
                bestScoreindexes.append(i)
        return bestScoreindexes

    def getHandsToCompare(self,hands,indexes):
        comparedHands = []
        for i in range(len(hands)):
            if i not in indexes:
                continue
            else:
                comparedHands.append(hands[i])
        return comparedHands








if __name__ == "__main__":
    handCheck = handChecker()
    handCheck.addHand(["AH", "KH", "QH", "JH", "10H"])
    handCheck.printCards()
    handCheck.checkForHand()
    print(handCheck.returnHand())
    print("------------")

    handCheck = handChecker()
    handCheck.addHand(["QC", "JC", "10C", "9C", "8C"])
    handCheck.checkForHand()
    print(handCheck.returnHand())
    print("------------")

    handCheck = handChecker()
    handCheck.addHand(["10C", "10H", "10K", "10G", "9C"])
    handCheck.checkForHand()
    print(handCheck.returnHand())
    print("------------")

    handCheck = handChecker()
    handCheck.addHand(["2C", "3C", "4C", "5G", "6G"])
    handCheck.checkForHand()
    print(handCheck.returnHand())
    print("------------")

    handCheck = handChecker()
    handCheck.addHand(["5C", "5H", "3K", "8G", "JC"])
    handCheck.checkForHand()
    print(handCheck.returnHand())
    print("------------")

    handCheck = handChecker()
    handCheck.addHand(["6C", "6H", "6K", "2G", "3C"])
    handCheck.checkForHand()
    print(handCheck.returnHand())
    print("------------")

    handCheck = handChecker()
    handCheck.addHand(["JC", "QC", "3C", "6C", "2C"])
    handCheck.checkForHand()
    print(handCheck.returnHand())
    print("------------")

    handCheck = handChecker()
    handCheck.addHand(["AC", "AK", "AH", "6C", "6G"])
    handCheck.checkForHand()
    print(handCheck.returnHand())
    print("------------")

    handCheck = handChecker()
    handCheck.addHand(["JC", "QC", "3C", "QK", "JG"])
    handCheck.checkForHand()
    print(handCheck.returnHand())
    print("------------")

    handCheck = handChecker()
    handCheck.addHand(["JC", "QC", "3C", "6H", "2C"])
    handCheck.checkForHand()
    print(handCheck.returnHand())


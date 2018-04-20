import Token
from random import randint
"""Dunwich difficulty"""
_easy = ['+1','+1','0','0','0','-1','-1','-1',"skull", "skull", "akolyth", "tentacle", "elder"]
_standard = ['+1','0','0','-1','-1','-1','-2', '-2', '-3', '-4', "skull", "skull", "akolyth", "tentacle", "elder"]
_hard = ['0','0','0','-1','-1','-2','-2','-3','-3','-4','-5',"skull", "skull", "akolyth", "tentacle", "elder"]
_expert = ['0','-1','-1','-2','-2','-3','-3','-4','-4','-5','-6','-8',"skull", "skull", "akolyth", "tentacle", "elder"]

class Bag():

    def __init__(self, difficulty = "normal"):
        self.bag = []
        self.prepareBag(difficulty)

    def addCoin(self, coin='0'):
        newCoin = Token.Token(art=coin)
        self.bag.append(newCoin)
        return "Added Coin."

    def prepareBag(self, difficulty):
        diff = { "easy" : _easy, "normal" : _standard, "hard": _hard, "expert":_expert}
        if difficulty not in diff:
            return "Nothing to prepare"
        #print(diff[difficulty])

        for coinvalue in diff[difficulty]:
            self.addCoin(coin=coinvalue)

        return "prepared {} bag".format(difficulty)

    def removeCoin(self, coin=None):

        for token in self.bag:
            if token.getValueAsStr().lower()==coin.lower():
                self.bag.remove(token)
                break
        return "Removed Coin."

    def drawCoin(self):
        size = len(self.bag)
        rng = randint(0,size-1)
        return self.bag[rng]

    def bagSize(self):
        return len(self.bag)

    def getBag(self):
        return self.bag

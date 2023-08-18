import random
import numpy as np
class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return f'{self.suit}:{self.rank}'

class Value:
    def __init__(self,value,highest_rank,rest_rank=[]):
        self.value = value
        self.highest_rank = highest_rank
        self.rest_rank=rest_rank
    def __str__(self):

        return str(self.value)+","+str(self.highest_rank)+","+str(self.rest_rank)
class deck:
    def __init__(self):
        self.cards=[]
        for a in ['heart','spade','club','diamond']:
            for i in range(1,14):
                self.cards.append(Card(a,i))

    def shuffle(self):
        random.shuffle(self.cards)
    def pop(self):
        return self.cards.pop()

    def join(self,cards):
        self.cards.extend(cards)

class Hand:
    def __init__(self):
        self.cards=[]
    def __str__(self):
        all_card=""
        for card in self.cards:
            all_card=all_card+str(card)+" "
        return all_card

    def get(self,deck,num):
        for i in range(num):
            self.cards.append(deck.pop())

    def get_card(self,card):
        self.cards.append(card)

    def join(self,cards):
        self.cards.extend(cards)

    def getValue(self):
        martrix = np.zeros((4, 14))
        for card in self.cards:
            if card.suit == 'heart':
                martrix[0][card.rank - 1] += 1
            elif card.suit == 'spade':
                martrix[1][card.rank - 1] += 1
            elif card.suit == 'club':
                martrix[2][card.rank - 1] += 1
            elif card.suit == 'diamond':
                martrix[3][card.rank - 1] += 1
        martrix[:, 13] = martrix[:, 0]
        ##whether is straight flush
        column_sums = np.sum(martrix, axis=0)
        row_sums = np.sum(martrix[:, :13], axis=1)

        for r in range(0, 4):
            for i in range(13, 3,-1):
                if np.sum(martrix[r, i - 4:i + 1]) == 5:

                    return Value(8, i)
                    break
        ##whether is Four of a kind
        for i in range(13, -1,-1):
            if column_sums[i]==4:
                for j in range(13, -1, -1):
                    if column_sums[j]>0 and j!=i:
                        rest=[j]

                return Value(7,i,rest)
                break
        ##wether Full house or three of a kind
        for i in range(13, -1, -1):
            if column_sums[i] == 3:
                for n in range(13, -1, -1):
                    if  i!=n and column_sums[n] >= 2:
                        rest=[n]
                        return Value(6,i,rest)


        ##wether Flush
        for i in range(0,4):
            if row_sums[i]>=5:
                rest=[]
                while len(rest)<5:
                    for c in range(13, -1, -1):
                        if column_sums[c]==1:
                            rest.append(c)
                return Value(5,rest)


        ##wether Straight
        new_column_sums = np.where(column_sums >= 1, 1, 0)
        for i in range(13, 3, -1):
            if np.sum(new_column_sums[i - 4:i + 1]) == 5:
                return Value(4, i)
                break

        ## wether 3
        for i in range(13, -1, -1):
            if column_sums[i] == 3:
                rest = []
                while len(rest) < 2:
                    for c in range(13, -1, -1):
                        if column_sums[c] == 1 :
                            rest.append(c)
                return Value(3, i,rest)
        #wether two pair/pair
        for i in range(13, -1, -1):
            if column_sums[i] == 2:
                for c in range(i-1,-1,-1):
                    if column_sums[c] == 2:
                        rest = []
                        for c in range(13, -1, -1):
                            if mcolumn_sums[c] == 1:
                                rest.append(c)
                        return Value(2,i,rest)
                        break
        for i in range(13, -1, -1):
            if column_sums[i] == 2:
                rest = []
                while len(rest) < 3:
                    for d in range(13, -1, -1):
                        if column_sums[d] == 1:
                            rest.append(d)
                return Value(1,i,rest)
                break
        rest = []
        while len(rest) < 5:
            for d in range(13, -1, -1):
                if column_sums[d] == 1:
                    rest.append(d)

                return Value(0,max(rest),rest)






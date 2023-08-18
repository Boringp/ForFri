from card import *
class Game:
    def __init__(self,playerList,bigblind):
        self.playerList=playerList
        self.bigblind=bigblind
        self.round_num = 1
    def round_start(self):
        deck1 = deck()
        deck1.shuffle()
        for player in self.playerList:
            if player.status==True and player.round_status==True:
                print("Name: " +player.name+"\nCurrent Stake: "+str(player.stake)+"\n")
        

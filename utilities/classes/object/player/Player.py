from utilities.classes.game import Game
class Player:
    def _init_(self, ID):
        self.ID = ID
        self.hand = []
        self.handCardinal = 7
        self.score = 0
        self.hasUno == False
        self.screamedUno == False
    def isActive(self, Game):
        if Game.state.["activePlayer"] == self.ID:
            return True
        else:
            return False
        """compare self player id with active id in state returns true or false"""
    def compareSingleCard(
    def throwCard(self, playedCards, cardToPlay, Game):
        if isActive(self, game) == True:
            card = self.hand.pop(hand.index(cardToPlay)) #temporary variable to hold the popped card
            playedCards.append(card)
            Game.state.["activePlayer"] = Game.players[Game.rotation+1].ID
            """changes playerActive to next player hence this player's to false"""
    def getHasUno(self):
        return self.hasUno
    def getScreamedUno(self):
        return self.screamedUno
    def screamUno(self, Game):
        if isActive(self) == True:
            if (Game.players[Game.rotation-1].hasUno == True) and (Game.players[Game.rotation-1].screamedUno == False):
                Game.players[Game.rotation-1].draw(2)
                self.screamUno = True
                print("player ", self.ID, "screamed UNO\n")
            elif self.hasUno == True:
                self.screamUno = True
                print("player ", self.ID, "screamed UNO\n")
            else:
                print("why'd you do that?")
                """I'm tempted to add a click counter and a while loop to make the comment more sarcastic everytime uno is clicked for no reason"""
    def getHand(self):
        return self.hand
        
            
            
            
        

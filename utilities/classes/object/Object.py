from turtle import position
import pygame
import utilities.classes.game.Game as Game_t
from utilities.functions.resize import getSize # to avoid circular imports

class Object():
    createdObjects=0
    def __init__(self,coordinates=[10, 10], dimensions=[10, 10], icon=None, callback=None):
        self.image = pygame.transform.scale(pygame.image.load(icon), getSize(icon, dimensions[0]))
        self.rect=self.image.get_rect()
        self.rect.center=coordinates
        self.dimensions=dimensions
        self.callback=callback
        # canMove will be used to test if we can drag the object with the mouse or not
        # it'll be False by default but here it's True just for testing purposes
        self.clicked=False
        self.objectId=Object.createdObjects
        Object.createdObjects+=1
        
    def update(self):
        # event= Game_t.Game.getState('event')
        pos = pygame.mouse.get_pos()
        # Game_t.Game.ifAiPlay()
        if self.rect.collidepoint(pos):  # testing if mouse hovering over Card
            if pygame.mouse.get_pressed()[0] == 1:  # testing if Card clicked
                if(self.callback):
                    self.callback()
        
        Game_t.Game.screen.blit(self.image, self.rect)
        self.updateCoord()
        
    def destroyObject(self):
        # this is more efficient than deleting an item of a list
        if(self.getId() in Game_t.Game.objectsGroup.keys()):
            Game_t.Game.objectsGroup.pop(self.getId())
        
    def add(self):
        Game_t.Game.objectsGroup[self.getId()]=self
            
    def updateCoord(self):
        # if(self.objectId>=len(Game_t.Game.objectsGroup)):
        #     Game_t.Game.objectsGroup.append(self)
        # else:
        Game_t.Game.objectsGroup[self.objectId]=self
    
    def triggerCallback(self, *args):
        if self.callback:
            if(args):
                self.callback(args)
            else:
                self.callback()
        
    def setCallback(self, callback):
        self.callback=callback
        
        
    def getId(self):
        return self.objectId
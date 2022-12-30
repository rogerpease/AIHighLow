#!/usr/bin/env python3 

from Decks import Decks
from brain import Brain
import numpy as np 


def DoDeckRun():
   cardsPerDeck = 100
   d = Decks(deckCount=100,cardsPerDeck=cardsPerDeck)
   # Discard one card 
   prevcard = d.draw
   trainingEntries = list()
   correctEntries = list() 
   
   brain = Brain(iS=(12,),outputs=1) 
   mymodel = brain.model 
   while d.AnyCardsInDraw:
     card = d.draw
     cardCountsRemaining = d.getCardCountsAboveBelow(card)
     if cardCountsRemaining["RemainingAbove"]  > cardCountsRemaining["RemainingBelow"]:
       correct = 1 
     else:
       correct = 0 
     trainingEntry = np.concatenate(([float(card/cardsPerDeck)], [d.getCardsDrawnFraction],  d.getCardsDrawnGroupPercentagesArray))
     trainingEntries.append(trainingEntry) 
     correctEntries.append(correct) 
     prevcard = card

   reshapedTraining = np.array(trainingEntries).reshape(-1,12,1)
   reshapedCorrect  = np.array(correctEntries).reshape(-1,1,1)
   mymodel.fit(reshapedTraining,reshapedCorrect,epochs=100,batch_size=100) 
	 
   mymodel.save("model.hd5") 
   return mymodel 

if __name__ == "__main__":
  mym = DoDeckRun()

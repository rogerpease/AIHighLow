#!/usr/bin/env python3 

import numpy as np


class Decks():
  def __init__(self,deckCount=1,cardsPerDeck=100,nGroups=10):
    self.nGroups = nGroups 
    self.deckCount = deckCount 
    self.cardsPerDeck = cardsPerDeck 
    self.arr = [(x%cardsPerDeck) for x in np.arange(self.numCardsDealt)]
    np.random.shuffle(self.arr)  
    self.drawnCounts = np.array([0.]*self.cardsPerDeck,dtype='int') 
  
  @property
  def numCardsDealt(self):  
    return self.deckCount * self.cardsPerDeck

  @property
  def _getarr(self):
    return self.arr 

  def getGroup(self,value):
    return int(value/self.nGroups)

  @property
  def getCardsDrawnFraction(self):
    return np.sum(self.drawnCounts)/self.numCardsDealt  
 
  def getCardCountsAboveBelow(self,cardNum):
    alreadyTakenAbove = 0 
    alreadyTakenBelow = 0 
    for i in range(0,cardNum):
      alreadyTakenBelow += self.drawnCounts[i]
    for i in range(cardNum+1,self.cardsPerDeck):
      alreadyTakenAbove += self.drawnCounts[i]
    remainingAbove = (self.cardsPerDeck-(cardNum+1))*self.deckCount  - alreadyTakenAbove
    remainingBelow = (cardNum)*self.deckCount                   - alreadyTakenBelow
    return {"RemainingAbove": remainingAbove,
            "RemainingSame": self.deckCount-self.drawnCounts[cardNum],
            "RemainingBelow": remainingBelow} 
 
  @property
  def getCardsDrawnCount(self):
    return np.sum(self.drawnCounts)  
 
  @property
  def getCardsDrawnGroupPercentagesArray(self):
    totaldrawn = self.getCardsDrawnCount
    results = np.array([0.]*self.nGroups,dtype='float') 
    for index,count in enumerate(self.drawnCounts):
      dgroup = self.getGroup(index) 
      results[dgroup] += count 
    results /= totaldrawn
    return results 
    
  @property 
  def AnyCardsInDraw(self):
    return True if len(self.arr) > 0 else False 
    
  @property 
  def draw(self):
    cardDrawn = self.arr.pop(0)
    self.drawnCounts[cardDrawn]  += 1
    return cardDrawn
 

if __name__ == "__main__":
  
  deckCount = 10
  cardsPerDeck = 100
  d = Decks(deckCount=deckCount,cardsPerDeck=cardsPerDeck)
  assert(d.getCardsDrawnFraction == 0)   
  count = {} 
  assert (len(d._getarr) == deckCount*cardsPerDeck)  
  assert(d.AnyCardsInDraw)   
  for c in d._getarr:
    count[c] = count.get(c,0) + 1
  for c in count:
    assert count[c] == 10
  
  assert (d.AnyCardsInDraw) 
  draw1 = d.draw 
  draw2 = d.draw 
  assert (d.getCardsDrawnCount == 2),d.getCardsDrawnCount 
  aboveBelow = d.getCardCountsAboveBelow(draw1)
  assert aboveBelow["RemainingAbove"] + aboveBelow["RemainingBelow"] + aboveBelow["RemainingSame"] == cardsPerDeck*deckCount-2,aboveBelow

  cdgpa = d.getCardsDrawnGroupPercentagesArray
  assert(np.sum(cdgpa) == 1)   

  for i in range(0,deckCount*cardsPerDeck-2):
    d.draw 
  cdgpa = d.getCardsDrawnGroupPercentagesArray
  assert(np.sum(cdgpa) == 1)   
  assert(not d.AnyCardsInDraw)   
  assert(d.getCardsDrawnFraction == 1)   


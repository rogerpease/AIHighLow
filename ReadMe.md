#Premise:
  Assume we are dealt N decks of cards and know our prior counts.  
  Will the next card drawn be higher or lower than previous card? 
 
#Inputs

  [ Current Card Value, 
    Fraction of deal remaining (1= no cards dealt,0=all cards dealt) 
    Fraction of previous cards drawn 1-10
    Fraction of previous cards drawn 11-20
    ... 
    Fraction of previous cards drawn 91-100 ] 

 
 So: [[0.14 0.1 0.5 0.5 0. 0. 0. 0. 0. 0. 0. 0. ]]  [1]  
   would mean a 14 (of 100) was drawn, 10% of our cards have been drawn, 
   and all of them were in the first or second 'group' (0-10,10-20)

#Outputs 
    1 output- 1 if we should assume next card is higher, 0 if we should assume next card is lower. 

#Running

 ./Train.py     # trains the model. It will deal itself several hundred cards, then 
                # make a prediction based on how many cards have already fallen above/below it. 

 ./Test.py      # Runs Predictions based on trained model. 


# Notes: 
  I originally did this with the 'output' being the *actual* comparison. 
  That is: 

      if card > nextCard:
       result = 1  
      else 
       result = 0  

   but realized that wasn't fair to the model. I should be training it to provide the proper prediction, 
   which may not necessarily be the right answer. If I flip a coin I expect it to be heads or tails. 
   If I flip ten coins, I expect *about* 5 to be heads and 5 to be tails and that is what I should predict. 
   I should not "penalize" the model if I just happen to land on the case where all 10 coins are tails. 

   I want it to tell me that it predicts 5 heads/5 tails, not confuse it with the fact that sometimes it wasn't. 

   So I changed to:

    if numOfCardsAboveMyCardStillInDeck > numOfCardsBelowMyCardStillInDeck: 
      result = 1  
    else 
      result = 0  



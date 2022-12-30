#!/usr/bin/env python3 

from keras.models import Sequential, load_model

from Decks import Decks
from brain import Brain
import numpy as np 

if __name__ == "__main__":
  mymodel = load_model('model.hd5') 
  # Comparing against highest card, one card has been drawn
  print ("Should be 0-ish", mymodel.predict([[  1,0,1,0,0,0,0,0,0,0,0,0]]))
  # Comparing against lowest card, one card has been drawn
  print ("Should be 1-ish", mymodel.predict([[  0,0,1,0,0,0,0,0,0,0,0,0]]))

  # Comparing against highest/lowest card, all cards have been drawn
  print ("Should be 0-ish", mymodel.predict([[  1,1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]]))
  print ("Should be 1-ish", mymodel.predict([[  0,1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]]))

  # Compare against middle card, but all the low cards have been drawn. So expect high. 
  print ("Should be closer to 1", mymodel.predict([[  0.5,0.5,0.2,0.2,0.2,0.2,0.2,0.0,0.0,0.0,0.0,0.0]]))
  # Compare against middle card, but all the high cards have been drawn. So expect low. 
  print ("Should be closer to 0", mymodel.predict([[  0.5,0.5,0,0,0,0,0,0.2,0.2,0.2,0.2,0.2]])) 
  # Compare against 90 (of 100) card, but 0-10 and 90-100 cards have been drawn. So expect low. 
  print ("Should be closer to 0", mymodel.predict([[ 0.90,0.2,0.5,0,0,0,0,0.0,0.0,0.0,0.0,0.5]])) 

  # Compare against 80 (of 100) card, but all 80-100 cards have been drawn. So expect low. 
  print ("Should be closer to 0", mymodel.predict([[ 0.80,0.2,0.0,0,0,0,0,0.0,0.0,0.0,0.5,0.5]])) 

  # Compare against 0 (of 100) card, but 80-100 cards have been drawn. So expect high. 
  print ("Should be closer to 1", mymodel.predict([[ 0.00,0.2,0.0,0,0,0,0,0.0,0.0,0.0,0.5,0.5]])) 

  # Compare against 80 (of 100) card, but all 0-10, 80-100 cards have been drawn. So expect Low. 
  print ("Should be closer to 0", mymodel.predict([[ 0.80,0.3,0.33,0,0,0,0,0.0,0.0,0.0,0.33,0.33]])) 

  # Compare against 10 (of 100) card, but all 0-10, 80-100 cards have been drawn. So expect high. 
  print ("Should be closer to 1", mymodel.predict([[ 0.10,0.3,0.33,0,0,0,0,0.0,0.0,0.0,0.33,0.33]])) 

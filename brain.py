#!/usr/bin/env python3 

import numpy as np
import keras
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Conv2D,MaxPooling2D, Flatten
from keras.optimizers import Adam

class Brain():
  def __init__(self, iS = None,outputs=1,lr=0.01):
    self.learningRate = lr 
    self.inputShape = iS 
    self.model = Sequential() 
    self.model.add(Dense(units=250,activation='relu',input_shape=iS))
    self.model.add(Dense(units=outputs))
    self.model.compile(loss='mean_squared_error',optimizer=Adam(learning_rate=self.learningRate)) 
  
  def loadModel(self,filepath):
    self.model = load_model(filepath)
    return self.model

if __name__ == "__main__": 
  d = Brain(iS=(1,),lr=0.1,outputs=1)
  fs = np.array(range(1,1000)).reshape(-1,1,1) 
  labels = fs * 2 
  print (fs,labels) 
  d.model.fit(fs,labels,epochs=25,batch_size=40) 
  p = d.model.predict([[10]])
  assert (p[0][0] < 21)  
  assert (p[0][0] > 19)  

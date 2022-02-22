import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow import keras
import numpy as np
import os
import pickle
DATADIR = ''
VECTOR_SIZE = 5
X = pickle.load( open( "trainingX.p", "rb" ) )
Y = pickle.load( open("trainingY.p", "rb"  ) )

#apply the normalization formula given min, max, and a data point "value"
def applyNormalization(value,min,max):
  dif = max - min
  if dif ==0 or value>max:
    return 1
  else:
    return (value-min)/dif


#[normalize lst] is the list where all the elements of each column are
#mapped into the range [0,1] from their respective domains.
#Each data point is mapped using new=(old-min)/(max-min) where max and min
#are the maxes and mins of all the data of their column
def normalize(featureList):
  mins=np.amin(featureList, axis=0)
  maxs=np.amax(featureList, axis=0)
  finArray=None
  for row in range(len(X)):
    array=None
    for column in range(VECTOR_SIZE):
      if column==0:
        array=np.asarray(applyNormalization(featureList[row][column],mins[column],maxs[column]).astype('float32'))
      else:
        array=np.append(array,(applyNormalization(featureList[row][column],mins[column],maxs[column])))
    if row==0:
      finArray=np.asarray(array).astype('float32')
    else:
      finArray=np.vstack([finArray,array])
  return finArray

#mins and maxes of data. [mins] is a list of 5 elements which are the mins and
#maxes of their respective columns
mins=np.amin(X, axis=0)
maxs=np.amax(X, axis=0)

val_fea=np.array([[0.33,5.,32.5,15.2,305]])

predict_vector=np.asarray(applyNormalization(val_fea[0][0],mins[0],maxs[0]).astype('float32'))


#making vector to predict
for x in range(1,5):
  predict_vector=np.append(predict_vector,(applyNormalization(val_fea[0][x],mins[x],maxs[x])))
predict_vector=np.reshape(predict_vector,(-1,5))
print(predict_vector)

#predicted output for test vector
predict_labels=np.array([[251.3, 342.55, 484.87, 538.35, 127.11]])

#training labels
y = np.asarray(Y).astype('float32')

#normalizing input features
x=normalize(X)
print(x)



model = Sequential()

model.add(Dense(5))
model.add(Dense(64))
model.add(Dense(64))
model.add(Dense(64))
model.add(Dense(5))



model.add(Activation("relu"))

model.compile(loss='mean_squared_error',optimizer=tf.optimizers.Adam(learning_rate=0.1),metrics=[tf.keras.metrics.MeanAbsoluteError()])

history=model.fit(x, y, epochs=100)

model.predict(predict_vector)

model.save("trained_model.h5")

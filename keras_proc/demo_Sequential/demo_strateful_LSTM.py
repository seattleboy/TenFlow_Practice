from keras.models import Sequential
from keras.layers import Dense,Dropout,LSTM
import numpy as np

data_dim=16
timesteps=8
num_classes=10
batch_size=32

#expected input data shape:(batch_size,timessteps,data_dim)
model=Sequential()
model.add(LSTM(32,return_sequences=True,stateful=True,batch_input_shape=(batch_size,timesteps,data_dim)))
model.add(LSTM(32,return_sequences=True,stateful=True))
model.add(LSTM(32,stateful=True))
model.add(Dense(10,activation='softmax'))

model.compile(loss='categorical_crossentropy',optimizer='rmsprop',metrics=['accuracy'])



#Generate dummy training data
x_train=np.random.random((batch_size*10,timesteps,data_dim))
y_train=np.random.random((batch_size*10,num_classes))

##Generate dummy validation data
x_val=np.random.random((batch_size*3,timesteps,data_dim))
y_val=np.random.random((batch_size*3,num_classes))

model.fit(x_train,y_train,batch_size=batch_size,epochs=10,validation_data=(x_val,y_val))


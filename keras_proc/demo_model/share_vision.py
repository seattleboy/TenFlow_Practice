from keras.layers import Conv2D,MaxPool2D,Input,Dense,Flatten,concatenate
from keras.models import Model
import keras
#First,define the vision modules
digit_input=Input(shape=(27,27,1))
x=Conv2D(64,(3,3))(digit_input)
x=Conv2D(64,(3,3))(x)
x=MaxPool2D((2,2))(x)
out=Flatten()(x)

vision_model=Model(digit_input,out)

#Then define the tell-digits-apart model
digit_a=Input(shape=(27,27,1))
digit_b=Input(shape=(27,27,1))

#The vision model will be shared,weights and all
out_a=vision_model(digit_a)
out_b=vision_model(digit_b)

concatenated_result=concatenate([out_a,out_b])

out=Dense(1,activation='sigmoid')(concatenated_result)

classifition_model=Model([digit_a,digit_b],out)
print("All set,reday to go")
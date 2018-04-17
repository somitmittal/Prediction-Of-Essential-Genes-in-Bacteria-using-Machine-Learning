from keras.models import Sequential
from keras.layers import Dense
import numpy
import pandas as pd
from sklearn import svm


# fix random seed for reproducibility
numpy.random.seed(7)
# load pima indians dataset
dataset = pd.read_csv("/home/somit/Desktop/BTP/deg-p-13.3/EcoliMG1655/EcoliGenes.csv")

#dataset = numpy.loadtxt("/home/somit/Desktop/BTP/deg-p-13.3/EcoliMG1655/EcoliGenes.csv", delimiter=",")
# split into input (X) and output (Y) variables
#features=['H1','H2','H3','H4','H5','DC','BC','CAI','CBI','Fop','GC','Nc','GC3S','L-sym','L-aa','Gravy','Aromo']
features=['CAI','CBI','Fop','GC','Nc']
#features=['#DEG','#DEG_AC','#Gene_Name','#Function','#Organism','#Condition','H1','H2','H3','H4','H5','DC','BC','GC3S','L-sym','L-aa','Gravy','Aromo']
X=dataset[features]
Y=dataset['Essentiality']
clf=svm.SVC()
clf.fit(X,Y)

#dataset.to_csv('data.csv')
#X = dataset[:,0:5]
#Y = dataset[:,5]

# create model
# model = Sequential()
# model.add(Dense(5, input_dim=5, activation='relu'))
# model.add(Dense(3, activation='relu'))
# model.add(Dense(1, activation='sigmoid'))
# # Compile model
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# # Fit the model
# model.fit(X, Y, nb_epoch=1, batch_size=100)
# # evaluate the model
# #scores = model.evaluate(X, Y)
# #print "\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100)
# predictions = model.predict(X)
# # round predictions
# rounded = [round(x[0]) for x in predictions]
# print rounded

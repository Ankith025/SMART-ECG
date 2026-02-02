import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import random
##import warnings
##warnings.filterwarnings('ígnore')
from PIL import ImageTk, Image  


df = pd.read_csv('test.csv')

features = df[["age","sex","height","Weight","qrs","q-t","t"]]
target = df["diagnosis"]

X_train , X_test , y_train , y_test = train_test_split(features,target,test_size=0.2,random_state=100)

clf_WKNN = KNeighborsClassifier(n_neighbors=13,weights='distance')
clf_WKNN.fit(X_train, y_train)
y_pred_WKNN = clf_WKNN.predict(X_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(y_pred_WKNN,y_test))
import pickle
with open('model.pkl', 'wb') as file:
   pickle.dump(clf_WKNN,file)

import pickle
pickle.load(open("model.pkl","rb"))

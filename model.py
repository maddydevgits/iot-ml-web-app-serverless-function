import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pickle

data=pd.read_csv('iot.csv')

X=data.iloc[:,1:-1].values
Y=data.iloc[:,-1].values

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)
classifier=KNeighborsClassifier()
classifier.fit(X_train,Y_train)

Y_pred=classifier.predict(X_test)
print(accuracy_score(Y_pred,Y_test))
model=open('model.pkl','wb')
pickle.dump(classifier,model)
model.close()
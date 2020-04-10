import pandas as pd
import numpy as np
print('This is model Training File')

from sklearn.datasets import load_iris
iris = load_iris()
x =  iris.data
y = iris.target
print(x.shape)
print(y.shape)

from sklearn.ensemble import RandomForestClassifier
model= RandomForestClassifier()
model.fit(x,y)
yhat = model.predict(x)
from sklearn.metrics import accuracy_score
a = accuracy_score(yhat ,y)
print(a)
print('model training over')
import pickle
#pickle.dump(regressor, open('model.pkl','wb'))
pickle.dump(model, open('model.pkl', 'wb'))

r = model.predict([np.array([2.2,3.1,2.4, 1,3])])
print(r)
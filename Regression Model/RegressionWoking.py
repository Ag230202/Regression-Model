import tensorflow as tf
import  pandas as pd
import  sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import  numpy as np

data=pd.read_csv("C:\\Users\\ANIMESH GARTIA\\OneDrive\\Desktop\\python tutorial\\ML\\student-mat.csv",sep=";")

data=data[["G1","G2","G3","studytime","absences"]]
predict="G3"

X=np.array(data.drop([predict],axis=1))
Y=np.array(data[predict])

x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(X,Y,test_size=0.1)
linear=linear_model.LinearRegression()
linear.fit(x_train,y_train)
acc=linear.score(x_test,y_test)
print("Accuracy-> ",acc)
print("Coefficient:",linear.coef_)
print("Intercept",linear.intercept_)

predictions=linear.predict(x_test)

for x in range(len(predictions)):
    print((int)(predictions[x]),y_test[x])


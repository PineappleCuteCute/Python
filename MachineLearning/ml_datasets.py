from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import MachineLearning.numpy as np

iris_dataset = load_iris()
#print(iris_dataset.data)
#print(iris_dataset.target)
#print(len(iris_dataset.target))

X_train, X_test, Y_train, Y_test = train_test_split(iris_dataset.data, iris_dataset.target, random_state=0)
'''
print(X_train)
print(X_test)
print(Y_train)
print(Y_test)
'''
#print(type(X_train))

model = DecisionTreeClassifier()
mymodel = model.fit(X_train, Y_train)
X_new = np.array([[6.0, 3.23, 4.5, 2.0]])
print(mymodel.predict(X_test))
print(mymodel.predict(X_new))
print(mymodel.score(X_test, Y_test))

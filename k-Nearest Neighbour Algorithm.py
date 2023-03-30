from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
iris=datasets.load_iris()
print("Iris Data set loaded...")
xtrain, xtest, ytrain, ytest = train_test_split(iris.data,iris.target)
a = KNeighborsClassifier(3).fit(xtrain, ytrain)
b=a.predict(xtest)
print("Results of Classification using K-nn with K=1 ")
for r in range(0,len(xtest)):
  print(" Sample:", str(xtest[r]), " Actual-label:", str(ytest[r])," Predicted-label:",str(b[r]))
print("Classification Accuracy :" , a.score(xtest,ytest));

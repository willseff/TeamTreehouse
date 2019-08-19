from sklearn.datasets import load_iris
iris = load_iris()

print(list(iris.target_names))

from sklearn import tree
classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(iris.data, iris.target)

#two square brackets because we have an array of samples
print(classifier.predict([[5.1,3.5,1.4,0.2]]))

tree.plot_tree(classifier.fit(iris.data, iris.target)) 
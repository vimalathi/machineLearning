from sklearn.datasets import load_iris
#load sample data and test
iris = load_iris()
print(iris.feature_names)
print(iris.target_names)
print(iris.data[0])
print(iris.target[0])

#removing few entries to test and train the data
import numpy as np
test_idx = [0, 50, 100]
#training data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)
#testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

#writing classifier
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)
print(test_target)
print(clf.predict(test_data))

#visualizing the code
from sklearn.externals.six import StringIO
import pydot
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data, feature_names=iris.feature_names, class_names=iris.target_names, filled=True, rounded=True, impurity=False)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
#Image(graph.create_png('iris.png'))

print(test_data[0], test_target[0])
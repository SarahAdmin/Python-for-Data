from sklearn.datasets import load_iris # load the iris function
# run the load_iris()function and save the return value in an object called # iris
iris = load_iris() 

x = iris.data
y = iris.target 

print(iris.data.shape)
print(iris.target.shape)

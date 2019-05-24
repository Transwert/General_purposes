#implementation of linear regression( single variable ) with gradient descent:

import numpy as np
import random
from matplotlib import pyplot as plt

def line ( theta0 , theta1, x):
	return (theta0 + theta1 * x)

def gradient_des ( theta0, theta1, x, y):
	result = 0;
	sumed = 0;
	if len(x) == len(y):
		for i in range(len(x)):
			#print(sum,"+",line(theta0,theta1,x[i]) - y[i])
			sumed = sumed + ( line(theta0,theta1,x[i]) - y[i])**2
		result = sumed / (2 * len(x))
		return result
	else:
		printf("x and y are of inequal length")

def summed_lin ( theta0, theta1, x, y):
	result = 0;
	sumed = 0;
	if len(x) == len(y):
		for i in range(len(x)):
			sumed = sumed + ( line(theta0,theta1,x[i]) - y[i])
		result = sumed /  len(x)
		return result
	else:
		printf("x and y are of inequal length")

def summed_lin_weighted ( theta0, theta1, x, y):
	result = 0;
	sumed = 0;
	if len(x) == len(y):
		for i in range(len(x)):
			sumed = sumed + ( line(theta0,theta1,x[i]) - y[i])*x[i]
		result = sumed / len(x)
		return result
	else:
		printf("x and y are of inequal length")


def linear_reg (x,y):
	if len(x) == len(y):
		theta0 = random.randint(-10,10)
		theta1 = random.randint(-10,10)
		alpha = 0.1 # problem in how to decide the the factor to be smal or large

		while gradient_des(theta0,theta1,x,y) != 0 : # probably error in this converging condition
			temp0 = theta0 - alpha * summed_lin(theta0,theta1,x,y)
			temp1 = theta1 - alpha * summed_lin_weighted(theta0,theta1,x,y)
			# print(temp0)
			# print(temp1)
			if theta0 != temp0 and theta1 != temp1:
				theta0 = temp0
				theta1 = temp1
			else:
				break;
		return [theta0,theta1]
	else:
		printf("x and y are of inequal length")

x = []
for i in range(10):
	x = x + [i]
print(x)
#x = [1,2,3,4,5,6]
y = [ 0 for _  in range(len(x))]
for i in range(len(y)):
	y[i] = random.randint(-100,100)
print(y)
# y = [13,10,8.75,4,5.5,2]
x_range = np.linspace(-1, 10, 1000)

parameters = linear_reg(x,y)
fig, yfunc = plt.subplots()
yfunc.plot(x_range, parameters[0] + parameters[1] * x_range, color='purple')
yfunc.axhline(0, color='black', lw=2)
yfunc.axvline(0, color='black', lw=2)
plt.scatter(x,y)
plt.show()
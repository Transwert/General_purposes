#implementation of linear regression( single variable ) with gradient descent and cost function:
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math
import scipy.stats as stats
import pandas as pd
from scipy import optimize
import random

A=pd.read_csv("testfile.csv")
x = A['x']
y = A['y']

# FUNCTION TO TAKE A x-coordinate, and return y-coordinate, with given parameters:
def line ( theta0 , theta1, x):
 	return (theta0 + theta1 * x)

# FUNCTION TO TAKE coeficients of polynomial function and calculation cost function: 
# ( in this case, the function is linear )
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
 
# FUNCTION to calculate partial derivative of cost function
#  w.r.t first parameter. (theta0 in this case.)
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

# FUNCTION to calculate partial derivative of cost function
#  w.r.t first parameter. (theta1 in this case.)
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

# FUNCTION for step wise calculation of gradient descent for linear polynomial in one variable,
# which involves running for the loop, until gradient descent converges
# i.e. (cost function with updated values tends to zero { very small value in our case.})
def linear_reg (x,y):
	if len(x) == len(y):
		theta0 = random.randint(-10,10)
		theta1 = random.randint(-10,10)
		alpha = 1 

		if gradient_des(theta0,theta1,x,y) > 10**(-16) :
			while gradient_des(theta0,theta1,x,y) > 10**(-16) : 
				temp0 = theta0 - alpha * summed_lin(theta0,theta1,x,y)
				temp1 = theta1 - alpha * summed_lin_weighted(theta0,theta1,x,y)
				# to see how parameters are changing for the simultaneous gradient descent, we are printing 
				# parameters
				# print(temp0)
				# print(temp1)
				if theta0 != temp0 and theta1 != temp1 :
					theta0 = temp0
					theta1 = temp1
				else:
					break;
			return [theta0,theta1]
		else :
			print([theta0,theta1])
	else:
		printf("x and y are of inequal length")

# --------------------------------------------------------------------------------------------------
# THE BELOW PART OF ENTERING x AND y AS INPUT, WAS LOGICALLY WRONG ( assuming ),
# AS I ASSUMMED THAT DUE TO RANDOM GENERATION, THERE IS A LOT OF DIFFERENCE IN DATA,
# WHICH RESULTS IN CAUSING OVERFLOW IN SQUARE FUNCTION ( IN GRADIENT DESCENT FUNCTION):

# x = []
# for i in range(25):
# 	x = x + [i]
# print(x)
# #x = [1,2,3,4,5,6]
# y = [ 0 for _  in range(len(x))]
# for i in range(len(y)):
# 	y[i] = random.randint(-100,100)
# print(y)
# y = [13,10,8.75,4,5.5,2]

#---------------------------------------------------------------------------------------------------

# below part for plotting of linear hypothesis we get after linear regression
# along with data points. 
x_range = np.linspace(0, 1, 1000)
parameters = linear_reg(x,y)
fig, yfunc = plt.subplots()
yfunc.plot(x_range, parameters[0] + parameters[1] * x_range, color='purple')
yfunc.axhline(0, color='black', lw=2)
yfunc.axvline(0, color='black', lw=2)
plt.scatter(x,y)
plt.show()

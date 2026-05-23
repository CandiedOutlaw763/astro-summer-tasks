import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d

n=int(input("Enter the number of data points:"))
m=int(input("Enter the degree of polynomial regression:"))
m=m+1
x=[]
y=[]
for i in range(n):
    xi=float(input(f"Enter x[{i+1}]: "))
    yi=float(input(f"Enter y[{i+1}]: "))
    x.append(xi)
    y.append(yi)
df=pd.DataFrame({
    "x":x,
    "y":y
    })

X=np.zeros((n,m),dtype=float)
for i in range(n):
  for j in range(m):
    X[i][j]=x[i]**(j)

print(X) 

Y=np.array(df['y']).reshape(n,1)
print(Y)

XT=X.T
XTX=np.dot(XT, X)
XTX_inv=np.linalg.inv(XTX)
XTy=np.dot(XT, Y)
a= np.dot(XTX_inv, XTy)
print(f"Co-efficients are:\n{a}")

Y_pred=np.array([])
for i in range(n):
    Y_pred=np.append(Y_pred, sum(a[j]*x[i]**j for j in range(m)))

plt.scatter(x,y,color='red')
plt.plot(x, Y_pred,color='blue')
plt.legend(["Fitted line","Data points"])

y_smooth=gaussian_filter1d(Y_pred,sigma=1)
plt.plot(x,y_smooth,color='green')
plt.scatter(x,y,color='red')


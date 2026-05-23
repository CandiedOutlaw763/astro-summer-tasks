import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("Enter no of data points:")
n=int(input())
x=[]
y=[]
for i in range(n):
    a=float((input("enter x value:")))
    b=float((input("enter y value:")))
    x.append(a)
    y.append(b)
df=pd.DataFrame({
    "x":x,
    "y":y
})

plt.scatter(df["x"],df["y"],color="blue")

Y=np.log10(df['y'])
X=np.log10(df['x'])

a00=np.sum(X**2)
a01=np.sum(X)
a10=np.sum(X)
a11=n
b0=np.sum(X*Y)
b1=np.sum(Y)

co_ef_matrix=np.array([[a00,a01],[a10,a11]])
const_matrix=np.array([b0,b1])
co_ef_matrix=np.linalg.inv(co_ef_matrix)
result=np.dot(co_ef_matrix,const_matrix)

m=result[0]
c=10**(result[1])
print(m,c)

plt.plot(df["x"],c*df['x']**m,color="red")
plt.scatter(df["x"],df["y"],color="blue")
plt.legend(["Fitted line","Data points"])

from sklearn.metrics import mean_squared_error,r2_score
y_pred=c*df['x']**m
mse=mean_squared_error(df["y"],y_pred)
print("MSE: " + str(mse))

r2=r2_score(df["y"],y_pred)
print("R2: " + str(r2))
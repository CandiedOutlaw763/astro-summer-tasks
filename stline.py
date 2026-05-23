import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error,r2_score

print("Enter no of data points:")
n=int(input())
x=[]
y=[]
for i in range(n):
    a=int((input("enter x value:")))
    b=int((input("enter y value:")))
    x.append(a)
    y.append(b)
df=pd.DataFrame({
    "x":x,
    "y":y
})

plt.scatter(df["x"],df["y"],color="blue")

a00=np.sum(df["x"]**2)
a01=np.sum(df["x"])
a10=np.sum(df["x"])
a11=n
b0=np.sum(df["x"]*df["y"])
b1=np.sum(df["y"])

co_ef_matrix=np.array([[a00,a01],[a10,a11]])
const_matrix=np.array([b0,b1])
co_ef_matrix=np.linalg.inv(co_ef_matrix)
result=np.dot(co_ef_matrix,const_matrix)

plt.plot(df["x"],result[0]*df["x"]+result[1],color="red")
plt.scatter(df["x"],df["y"],color="blue")
plt.legend(["Fitted line","Data points"])

y_pred=result[0]*df["x"]+result[1]
mse=mean_squared_error(df["y"],y_pred)
print("MSE: " + str(mse))
r2=r2_score(df["y"],y_pred)
print("R2:" + str(r2))

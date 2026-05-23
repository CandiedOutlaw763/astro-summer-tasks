import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error,r2_score

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

a00=np.sum(df["x"]**2)
a01=np.sum(df["x"])
a02=n
a10=np.sum(df["x"]**3)
a11=np.sum(df["x"]**2)
a12=np.sum(df["x"])
a20=np.sum(df["x"]**4)
a21=np.sum(df["x"]**3)
a22=np.sum(df["x"]**2)
b0=np.sum(df['y'])
b1=np.sum(df["x"]*df["y"])
b2=np.sum(df["y"]*(df["x"]**2))

co_ef_matrix=np.array([[a00,a01,a02],[a10,a11,a12],[a20,a21,a22]])
const_matrix=np.array([b0,b1,b2])
co_ef_matrix=np.linalg.inv(co_ef_matrix)
result=np.dot(co_ef_matrix,const_matrix)
result

plt.plot(df["x"],result[0]*df["x"]**2+result[1]*df["x"]+result[2],color="red")
plt.scatter(df["x"],df["y"],color="blue")
plt.legend(["Fitted line","Data points"])

y_pred=result[0]*df["x"]**2+result[1]*df["x"]+result[2]
mse=mean_squared_error(df["y"],y_pred)
print("MSE: " + str(mse))
r2=r2_score(df["y"],y_pred)
print("R2:" + str(r2))
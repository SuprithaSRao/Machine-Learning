import matplotlib.pyplot as a
import pandas as pd
import numpy as np
def localWeight(point,p,ymat,k):
  m,n = np.shape(p)
  weights = np.mat(np.eye(m))
  for i in range(m):
    diff = point - p[i]
    weights[i,i] = np.exp(diff*diff.T/(-2.0*k**2))
  W = (p.T *(weights*p)).I * (p.T*(weights*ymat.T))
  return W

def localWeightReg(p,ymat,k):
  m,n = np.shape(p)
  ypred = np.zeros(m)
  for i in range(m):
    ypred[i] = p[i] * localWeight(p[i],p,ymat,k)
  return ypred

def plott(p,pred):
  sort = p[:,1].argsort(0)
  xsort = p[sort][:,0][:,1]
  ysort = pred[sort]
  a.scatter(x,y,color='green')
  a.plot(xsort,ysort,color='red',linewidth=4)
  a.xlabel('Total bill')
  a.ylabel('Tips')
  a.show()
  
data = pd.read_csv('ds10.csv')
x=data['total_bill']
y = data['tip']
xmat = np.mat(x)
ymat = np.mat(y)
size = np.shape(xmat)[1]
ones = np.mat(np.ones(size))
p=np.hstack((ones.T,xmat.T))
pred = localWeightReg(p,ymat,3)
plott(p,pred)

 #Dataset
 total_bill,tip,sex,smoker,day,time,size,fraction
16.99,1.01,Female,No,Sun,Dinner,2,0.059446733
10.34,1.66,Male,No,Sun,Dinner,3,0.160541586
21.01,3.5,Male,No,Sun,Dinner,3,0.166587339
23.68,3.31,Male,No,Sun,Dinner,2,0.139780405
24.59,3.61,Female,No,Sun,Dinner,4,0.146807645
25.29,4.71,Male,No,Sun,Dinner,4,0.18623962
8.77,4,Male,No,Sun,Dinner,2,0.228050171
26.88,3.14,Male,No,Sun,Dinner,4,0.116071429
15.04,1.96,Male,No,Sun,Dinner,2,0.130319149
14.48,3.23,Male,No,Sun,Dinner,2,0.218538566
13.99,1.01,Female,No,Sun,Dinner,2,0.059336733
40.34,1.66,Male,No,Sun,Dinner,3,0.160541586
23.01,4.3,Male,No,Sun,Dinner,3,0.166587339
33.68,3.31,Male,No,Sun,Dinner,2,0.139780405
24.59,3.41,Female,No,Sun,Dinner,4,0.133807645
25.29,4.71,Male,No,Sun,Dinner,4,0.18623962
8.77,2,Male,No,Sun,Dinner,2,0.228050171
36.88,3.12,Male,No,Sun,Dinner,4,0.113071429
15.44,1.46,Male,No,Sun,Dinner,2,0.130319349
13.78,3.23,Male,No,Sun,Dinner,2,0.218533366

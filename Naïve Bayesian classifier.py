import pandas as pd
data = pd.read_csv('ds55.csv')
target = 'class'
classes = data[target].unique()
features = data.columns[data.columns!=target]
testdata = data.sample(frac=0.3)
data.drop(testdata.index,inplace = True)
first ={}
fourth ={}
for x in classes:
  datacl = data[data[target]==x][features]
  tot = len(datacl)
  second={}
  for col in datacl.columns:
    third={}
    for val,cnt in datacl[col].value_counts().iteritems():
      prob = cnt/tot
      third[val]=prob
      second[col]=third
  first[x]=second
  fourth[x]=len(datacl)/len(data)
def proabl(params):
  proab={}
  for x in classes:
    calc = fourth[x]
  for col, val in params.iteritems():
    try:
      calc = first[x][col][val]
    except KeyError:
      calc =0
  proab[x]=calc
  return proab
def maxx(params):
  proab = proabl(params)
  maxcl =''
  maxv=0
  for col,val in proab.items():
    if(val>maxv):
      maxv=val
      maxcl=col
   return maxcl

b=[]
for i in data.index:
  b.append(maxx(data.loc[i,features]) == data.loc[i,target])
print(sum(b),'correct of',len(b))
print('Accuracy =',sum(b)/len(b))

b=[]
for i in testdata.index:
  b.append(maxx(testdata.loc[i,features]) == testdata.loc[i,target])
print(sum(b),'correct of',len(b))
print('Accuracy =',sum(b)/len(b))


#Dataset
class,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp,qq,rr,ss,tt,uu,vv
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w
b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,a
c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,a,b
d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,a,b,c
e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,a,b,c,d
f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,a,b,c,d,e
g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,a,b,c,d,e,f
a,b,d,c,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w
b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,a
c,a,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,d,b
d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,a,b,c
f,e,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,a,b,c,d
g,f,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,a,b,c,d,e
i,h,g,j,k,l,m,n,o,p,q,r,s,t,u,v,w,a,b,c,d,e,f

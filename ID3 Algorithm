import pandas as pd
from collections import Counter
import math

data = pd.read_csv('ds3.csv')
print("\n Given Play Tennis Data Set:\n\n", data)

def entropy(e):
  c = Counter(x for x in e)
  instances = len(e)
  prob = [x / instances for x in c.values()]
  return sum( [-p*math.log(p, 2) for p in prob] )

def information_gain(d, split, target):
  splitting = d.groupby(split)
  n = len(d.index)
  agent = splitting.agg({target : [entropy, lambda x: len(x)/n] })[target] #aggregating
  agent.columns = ['Entropy', 'observations']
  newentropy = sum( agent['Entropy'] * agent['observations'] )
  oldentropy = entropy(d[target])
  return oldentropy - newentropy
def id3(sub, target, a):
  count = Counter(x for x in sub[target])# class of YES /NO
  if len(count) == 1:
    return next(iter(count)) # next input data set, or raises Stop Iteration when EOF is hit
  else:
    gain = [information_gain(sub, attr, target) for attr in a]
    print("Gain=",gain)
    maximum = gain.index(max(gain))
    best = a[maximum]
    print("Best Attribute:",best)
    tree = {best:{}}
    remaining = [i for i in a if i != best]
  for val, subset in sub.groupby(best):
    subtree = id3(subset,target,remaining)
    tree[best][val] = subtree
  return tree
names = list(data.columns)
print("List of Attributes:", names)
names.remove('PlayTennis')
print("Predicting Attributes:", names)
tree = id3(data,'PlayTennis',names)
print("\n\nThe Resultant Decision Tree is :\n")
print(tree)

testdata = data.sample(frac = 0.1)
data.drop(testdata.index,inplace = True)
test = testdata.to_dict('records')[0]
print('\n',test,'=>', test['PlayTennis'])

#Dataset
Outlook,Temperature,Humidity,Windy,PlayTennis
Sunny,Hot,High,False,No
Sunny,Hot,High,True,No
Overcast,Hot,High,False,Yes
Rainy,Mild,High,False,Yes
Rainy,Cool,Normal,False,Yes
Rainy,Cool,Normal,True,No
Overcast,Cool,Normal,True,Yes
Sunny,Mild,High,False,No
Sunny,Cool,Normal,False,Yes
Rainy,Mild,Normal,False,Yes
Sunny,Mild,Normal,True,Yes
Overcast,Mild,High,True,Yes
Overcast,Hot,Normal,False,Yes
Rainy,Mild,High,True,No

Given Play Tennis Data Set:
Outlook Temperature Humidity Windy PlayTennis
0 Sunny Hot High False No
1 Sunny Hot High True No
2 Overcast Hot High False Yes
3 Rainy Mild High False Yes
4 Rainy Cool Normal False Yes
5 Rainy Cool Normal True No
6 Overcast Cool Normal True Yes
7 Sunny Mild High False No
8 Sunny Cool Normal False Yes
9 Rainy Mild Normal False Yes
10 Sunny Mild Normal True Yes
11 Overcast Mild High True Yes
12 Overcast Hot Normal False Yes
13 Rainy Mild High True No

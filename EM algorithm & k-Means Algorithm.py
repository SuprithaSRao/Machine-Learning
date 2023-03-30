from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
import pandas as pd
import numpy as np
import matplotlib.pyplot as a
data = pd.read_csv('ds8.csv')
f1 =data['Distance_Feature']
f2=data['Speeding_Feature']
x =np.array(list(zip(f1,f2)))
a.scatter(f1,f2,color='black')
a.title('Real')
a.ylabel('speeding_feature')
a.xlabel('distance_feature')
a.show()
kmeans = KMeans(3).fit(x)
labels = kmeans.predict(x)
a.scatter(f1,f2,c=labels)
a.title('KMeans')
a.ylabel('speeding_feature')
a.xlabel('distance_feature')
a.show()
gm = GaussianMixture(3).fit(x)
labels = gm.predict(x)
a.scatter(f1,f2,c=labels)
a.title('GMM Classification')
a.ylabel('speeding_feature')
a.xlabel('distance_feature')
a.show()


#Dataset
Driver_ID,Distance_Feature,Speeding_Feature
3423311935,71.24,28.0
3423313212,52.53,25.0
3423313724,64.54,78.0
3423311373,55.69,22.0
3423310999,54.58,25.0
3423319935,90.24,28.0
3423318212,82.53,25.0
3423317724,6.54,26.0
3423311363,65.69,32.0
3423310929,44.58,25.0

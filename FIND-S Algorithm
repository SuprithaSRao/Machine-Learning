f = open('ds1.csv','r')
length = len(f.readline().split(','))
hypo = ['0']*(length-1)
print('Intital Hypo = ',hypo)
f.close()
f = open('ds1.csv','r')
count =1
for line in f:
  lst = line.split(',')
  for i in range(length-1):
     if(lst[-1] == 'y\n'):
       if(hypo[i]!='0' and hypo[i]!=lst[i]):
       hypo[i]='?'
     else:
        hypo[i] = lst[i]
  print('Hypo ',hypo)
print('final hypo ',hypo)

sunny,warm,normal,strong,warm,same,y
sunny,warm,high,strong,warm,same,y
rainy,cold,high,strong,warm,change,n
sunny,warm,high,strong,cool,change,y

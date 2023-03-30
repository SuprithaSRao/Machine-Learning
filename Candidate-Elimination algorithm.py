f = open('ds2.csv','r')
length = len(f.readline().split(','))-1
f.close()
f = open('ds2.csv','r')
shypo = ['0']*(length)
ghypo =['?']*(length)
print('Intital Specific hypothesis',shypo)
count = 1
print('Intital General hypothesis',ghypo)
ghypo.clear()
for line in f:
  lst = line.split(',')
  for i in range(length):
    if(lst[-1] == 'y\n'):
      if (shypo[i]!='0' and shypo[i]!=lst[i]):
      shypo[i] ='?'
    else:
      shypo[i] = lst[i]
    elif (lst[-1] == 'n\n'):
      if '0' in shypo:
        temp = ['?']*i
        temp += [lst[i]]
        temp += ['?'] * (length-1-i)
        ghypo.append(temp)
      elif (shypo[i]!='?' and shypo[i]!=lst[i]):
        temp = ['?']*i
        temp +=[shypo[i]]
        temp += ['?'] * (length-1-i)
        if(temp not in ghypo):
          ghypo.append(temp)
  print('SHYPO ',count ," ",shypo)
  print('GHYPO ',count ," ",ghypo)
  count+=1
f_ghypo = list()
for i in range(len(ghypo)):
  for j in range(len(ghypo[i])):
    if(ghypo[i][j]!='?' and ghypo[i][j]==shypo[j]):
      f_ghypo.append(ghypo[i])
print(f_ghypo)

sunny,warm,normal,strong,warm,same,y
sunny,warm,High,strong,warm,same,y
rainy,cold,High,strong,warm,change,n
sunny,warm,High,strong,cool,change,y

import numpy as np # numpy is commonly used to process number array
x = np.array([[2,9], [3,6], [4,8]]) # Features ( Hrs Slept, Hrs Studied)
y = np.array([[92], [86], [89]]) # Labels(Marks obtained)
x = x/np.amax(x,axis=0) # Normalize
y = y/100
def sigmoid(x):
  return 1/(1 + np.exp(-x))
def sigmoid_grad(x):
  return x * (1 - x)

# Variable initialization
epoch=1000 #Setting training iterations
eta =0.1 #Setting learning rate (eta)
input_neurons = 2 #number of features in data set
hidden_neurons = 3 #number of hidden layers neurons
output_neurons = 1 #number of neurons at output layer

# Weight and bias - Random initialization
winp=np.random.uniform(size=(input_neurons,hidden_neurons)) # 2x3
binp=np.random.uniform(size=(1,hidden_neurons)) # 1x3
wout=np.random.uniform(size=(hidden_neurons,output_neurons)) # 1x1
bout=np.random.uniform(size=(1,output_neurons))
for i in range(epoch):
  #Forward Propogation
  finp=np.dot(x,winp) + binp # Dot product + bias
  fact = sigmoid(finp) # Activation function
  fout=np.dot(fact,wout) + bout
  output = sigmoid(fout)
  # Error at Output layer
  Eo = y-output # Error at o/p
  outgrad = sigmoid_grad(output)
  e_output = Eo* outgrad # Errj=Oj(1-Oj)(Tj-Oj)
  # Error at Hidden later
  Eh = np.dot(e_output,wout.T) # .T means transpose
  hidgrad = sigmoid_grad(fact) # How much hidden layer wts contribu
  ted to error
  e_hidden = Eh * hidgrad
  wout += np.dot(fact.T,e_output) *eta # Dotproduct of nextlayererr
  or and currentlayerop
  winp += np.dot(x.T,e_hidden) *eta

print("Normalized Input: \n" ,x)
print("Actual Output: \n" ,y)
print("Predicted Output: \n" ,output)

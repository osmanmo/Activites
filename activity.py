
import numpy
def running_mean(x, N):
    cumsum = numpy.cumsum(numpy.insert(x, 0, 0)) 
    return (cumsum[N:] - cumsum[:-N]) / float(N)










text_file = open("y_train.txt", "r")
lines = text_file.readlines()
for i in range(len(lines)):
	lines[i]=int(lines[i][0])

s=[]
for i in range(len(lines)):
    if lines[i]==3:
        s.append(i)


text_file = open("body_acc_z_train.txt", "r")
x = text_file.readlines()

q=[]
for i in range(7294,7321):
    z=x[i].split(' ')
    z=z[2:]
    k=[]
    for i in range(len(z)):
        if z[i]!='':
            k.append(float(z[i]))
    q=q+k      
    

from matplotlib import pyplot as plt

q=running_mean(q,10)
v=list(range(len(q)))
for i in range(len(v)):
    v[i]=.01*v[i]
from numpy import fft
tran=fft.fft(q)
w=list(range(len(tran)))


plt.plot(tran)
plt.ylabel('y - axis')
plt.show()





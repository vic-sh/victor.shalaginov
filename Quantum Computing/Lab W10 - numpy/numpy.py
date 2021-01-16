import numpy as np

ar_1 = np.array([[1,2,3,4j]])
#dim 1
#print(ar_1)

ar_2 = np.array([[1,2,3],[4,5,6]])

#print(ar_1.shape)
#print(ar_2.shape)

a = np.array([[0,1]])
b = np.array([[1,0]])

m = 1/np.sqrt(2)

c = (a+b)*m
d = (a-b)*m

#print(c)
#print(d)

#print(a)
#print(a.T)
#print(np.transpose(a))

print(ar_1)

new_ar_1 = ar_1.conj()
print(new_ar_1)

print(np.kron(a,b))
# * - simple multiplixation
# @ - Matrix multiplication
g = a @ b.T

print(g)

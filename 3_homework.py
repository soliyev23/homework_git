import math as m
a = input("--->")
for i in a.split():
    if len(i)==len(set(i)):
        x = m.ceil(len(i)/2)
        print(i[x::]+i[:x:])

# qisqa usuli
# print(' '.join([i[m.ceil(len(i)/2)::] + i[:m.ceil(len(i)/2):]  for i in a.split() if len(i)==len(set(i))]))
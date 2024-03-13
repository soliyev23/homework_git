a = input("Nmadur kiriting--->")
# a = 'ffgabnnkmm'
# a = 'farrabennlakot'
a = list(a)
natija,lst = [],[]
for i in range(1,len(a)):
    if i==len(a)-1 and a[i] != a[i-1]:
        lst.append(a[i-1])
        lst.append(a[i])
        natija.extend([''.join([i for i in lst])])
    if a[i] != a[i-1]:
        lst.append(a[i-1])
    else:
        lst.append(a[i-1])
        natija.extend([''.join([i for i in lst])])
        lst = []
c = max(natija,key=lambda x: len(x))
print(c)        
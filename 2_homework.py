import math
a = input("Nmadur kiriting--->")
c = math.ceil(len(a)/2)
a = a[c::]+a[:c:]
print(a)
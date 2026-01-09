a=10
b=5
temp = a
a = b
b = temp
print("a =",a)
print("b =",b)
#Without using temp variable
a=10
b=20
a,b = b,a
print("a =",a)
print("b =",b)
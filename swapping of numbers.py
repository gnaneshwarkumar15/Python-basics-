a=2
b=3
c=b
b=a
a=c
print('a',a)
print('b',b)


a=10
b=20
a,b=b,a
print('a',a)
print('b',b)


a=10
b=20
a=a+b
b=a-b
a=a-b
print('a',a)
print('b',b)


a=10
b=20
a=a+b
b=a-b
a=a-b
print('after swapping a=%d,b=%d'%(a,b))


a=1.5
b=1.5
a=a+b
b=a-b
a=a-b
print('after swapping a=%f,b=%f' %(a,b))


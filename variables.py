Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
print(a)
10
x=40
print(X)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
a=b,b=9
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a=b,b=9
TypeError: cannot unpack non-iterable int object
a=9,b=9
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=9;b=9
print(a,b)
9 9
a,b=3,4
print(a,b)
3 4
>>> a=1,2,3
>>> print(a)
(1, 2, 3)
>>> a,b,c=10
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a,b,c=10
TypeError: cannot unpack non-iterable int object
>>> a=b=c=10
>>> print(a,b,c)
10 10 10
>>> print(a)
10
>>> a,b,c=1,2,3,4,5,6
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a,b,c=1,2,3,4,5,6
ValueError: too many values to unpack (expected 3, got 6)
>>> first name='gnani'
SyntaxError: invalid syntax
>>> first_name='gnani'
>>> print(first_name)
gnani
>>> fname='gnani'
>>> lname='hi'
>>> print(fname+lname)
gnanihi
>>> print(fname+" "+lname)
gnani hi
>>> name="gnani"
>>> print(name)
gnani
>>> a=5
>>> print(a)
5
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined

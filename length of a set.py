Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a={4,5,6,7,8}
>>> len(a)
5
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a.count()
AttributeError: 'set' object has no attribute 'count'
>>> #error have occured because sets does not allow repeated numbers
>>> a.index(2)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a.index(2)
AttributeError: 'set' object has no attribute 'index'

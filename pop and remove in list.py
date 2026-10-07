Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=['black','white','blue','red','pink']
>>> a.pop()
'pink'
>>> a.pop(2)
'blue'
>>> a.pop('red')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a.pop('red')
TypeError: 'str' object cannot be interpreted as an integer
>>> a
['black', 'white', 'red']
>>> a.remove('black')
>>> a
['white', 'red']

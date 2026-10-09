Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a={5,6,7,8,9}
>>> a.pop()
5
>>> a.pop(7)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a.pop(7)
TypeError: set.pop() takes no arguments (1 given)
>>> #so we use remove
>>> a.remove(7)
>>> a
{6, 8, 9}

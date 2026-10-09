Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a={2,3,4,5,6}
>>> b={4,5,6,7}
>>> c={8,9,10,11}
>>> b.isdisjoint(a)
False
>>> b.isdisjoint(c)
True

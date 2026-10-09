Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a={10,11,12,13,14,15,16}
>>> b={6,7,8,12,13,14,15,16,17}
>>> a.difference(b)
{10, 11}
>>> b.difference(a)
{8, 17, 6, 7}

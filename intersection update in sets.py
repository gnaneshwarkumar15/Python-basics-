Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a={1,3,5,7,8,9,10}
>>> b={2,4,6,7,10,11,12}
>>> a.intersection_update(b)
>>> a
{10, 7}
>>> b
{2, 4, 6, 7, 10, 11, 12}
>>> b.intersection_update(a)
>>> b
{10, 7}

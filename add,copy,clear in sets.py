Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a={1,2,3,4,5}
>>> a.add(30)
>>> a
{1, 2, 3, 4, 5, 30}
>>> b=a.copy()
>>> b
{1, 2, 3, 4, 5, 30}
>>> b.clear()
>>> b
set()
>>> b.add(20)
>>> b
{20}

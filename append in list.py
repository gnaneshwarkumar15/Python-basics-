Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=['python','java','c']
>>> a.append('c++')
>>> a
['python', 'java', 'c', 'c++']
>>> a.append('ai','ml')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a.append('ai','ml')
TypeError: list.append() takes exactly one argument (2 given)
>>> a.append(['ai','ml'])
>>> a
['python', 'java', 'c', 'c++', ['ai', 'ml']]

Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a={'city':'vij','state':'ap','country':'india'}
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
>>> a.pop('city')
'vij'
>>> a
{'state': 'ap', 'country': 'india'}
>>> a.popitem()
('country', 'india')
>>> a
{'state': 'ap'}

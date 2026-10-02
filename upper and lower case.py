Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a='hello'
>>> a.upper()
'HELLO'
>>> a='HI'
>>> a.lower()
'hi'
>>> c='python'
>>> a.capitalize()
'Hi'
>>> d='puthon course'
>>> d.title()
'Puthon Course'
>>> a='python'
>>> a.isupper()
False
>>> a.islower()
True
>>> a.isalpha()
True
>>> b='python course'
>>> b.isalpha()
False
>>> d=1234
>>> d.isdigit()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
>>> e='1234'
>>> e.isdigit()
True
>>> f='ganani'
>>> f.isalnum()
True
>>> g='gnani'
>>> g.isalnum()
True
>>> h='gnani@123'
>>> h.isalnum()
False

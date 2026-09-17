Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
int(8.4)
8
int('code')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    int('code')
ValueError: invalid literal for int() with base 10: 'code'
int(6+7j)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    int(6+7j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
float(6)
6.0
float(2+3j)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    float(2+3j)
TypeError: float() argument must be a string or a real number, not 'complex'
float('code')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    float('code')
ValueError: could not convert string to float: 'code'
float('True')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    float('True')
ValueError: could not convert string to float: 'True'
>>> float(True)
1.0
>>> str('1')
'1'
>>> str(9)
'9'
>>> str(2.3)
'2.3'
>>> str(3+4j)
'(3+4j)'
>>> str(True)
'True'
>>> complex(9)
(9+0j)
>>> complex(9.2)
(9.2+0j)
>>> complex('code')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    complex('code')
ValueError: complex() arg is a malformed string
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> bool(9)
True
>>> bool(9.1)
True
>>> bool('code')
True
>>> bool(2+7j)
True
>>> bool(True)
True
>>> bool(False)
False

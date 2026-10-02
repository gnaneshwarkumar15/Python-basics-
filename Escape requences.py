Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #\n-new line
>>> #\t-tab space
>>> a="name \n mobileno\t mailid\n college\t branch"
>>> print(a)
name 
 mobileno	 mailid
 college	 branch
>>> b='name:Gnaneshwar \n mobile:9090999909 \t mailid:ganaeshwar@gmail.com \n college:VRSEC \t branch:ECE
SyntaxError: unterminated string literal (detected at line 1)
>>> b='name:Gnaneshwar \n mobile:9090999909 \t mailid:ganaeshwar@gmail.com \n college:VRSEC \t branch:ECE'
>>> print(b)
name:Gnaneshwar 
 mobile:9090999909 	 mailid:ganaeshwar@gmail.com 
 college:VRSEC 	 branch:ECE

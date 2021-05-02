Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> import math as m
>>> print(m.sqrt(36))
6.0
>>> from math import sqrt as s
>>> print(m.s(144))
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(m.s(144))
AttributeError: module 'math' has no attribute 's'
>>> print(s(144))
12.0
>>> 

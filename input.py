Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: /Users/abhishekbodapati/Desktop/Python/a.py ============
10
>>> a="37"
>>> type(a)
<class 'str'>
>>> input a
SyntaxError: invalid syntax
>>> input
<built-in function input>

>>> input(b)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    input(b)
NameError: name 'b' is not defined
>>> input(a)
371
'1'
>>> print(a)
37
>>> input(a)
37
''
>>> input
<built-in function input>
>>> x=input()
34
>>> print(x)
34
>>> 
x+6
Traceback (most recent call last):
  File "<pyshell#11>", line 2, in <module>
    x+6
TypeError: can only concatenate str (not "int") to str
>>> 

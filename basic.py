Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x=321231312.2313211
type(x)
<class 'float'>

x=[1,2,3,4,5]

type(x)
<class 'list'>
s=(1,2,3)
type(x)
<class 'list'>
x=(1,2,3)
type(x)
<class 'tuple'>
x={1,2,3}
type(x)
<class 'set'>
import keyword
keyword kwlist
SyntaxError: invalid syntax. Perhaps you forgot a comma?
keyword
<module 'keyword' from 'C:\\Users\\Saksham Tambe\\AppData\\Local\\Programs\\Python\\Python310\\lib\\keyword.py'>
kwlist
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    kwlist
NameError: name 'kwlist' is not defined. Did you mean: 'list'?
name="engineer"
name
'engineer'
name[-1]
'r'
name[0]
'e'
name[-5]
'i'
name[0:-1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
name[0:-1]
'enginee'
name[0:-1:2]
'egne'
name[::]
'engineer'
name = "ENgineer"
name[::-1]
'reenigNE'
name="jal"
name*3
'jaljaljal'
len(name)
3

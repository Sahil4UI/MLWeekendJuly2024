Python 3.12.3 (v3.12.3:f6650f9ad7, Apr  9 2024, 08:18:47) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#String
#String is python's immutable and ordered data type
#immutable-which cannnot be changed
x = "Welcome to Python Programming"
x[0]="w"
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    x[0]="w"
TypeError: 'str' object does not support item assignment
len(x)
29
x.upper()
'WELCOME TO PYTHON PROGRAMMING'
x
'Welcome to Python Programming'
x = x.upper()
x
'WELCOME TO PYTHON PROGRAMMING'
x = "Welcome to Python Programming"
x.lower()
'welcome to python programming'
x.capitalize()#first letter of String will be capital
'Welcome to python programming'
x.title()
'Welcome To Python Programming'
x.swapcase()
'wELCOME TO pYTHON pROGRAMMING'
X
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    X
NameError: name 'X' is not defined. Did you mean: 'x'?
x
'Welcome to Python Programming'
x.count("o")
4
x.count("X")
0
x
'Welcome to Python Programming'
x.find("o")#first occurance
4
x.rfind("o")
20
x.find("o",0)
4
x.find("o",5)
9
x
'Welcome to Python Programming'
x[0:6]#here ending range is n-1
'Welcom'
x[0:7]
'Welcome'
x[18:]
'Programming'
x[:18]
'Welcome to Python '
x[:]
'Welcome to Python Programming'
x[0:18]
'Welcome to Python '
x[0:18:1]
'Welcome to Python '
x[0:18:2]
'Wloet yhn'
x[-3]
'i'
x.find("o",0)
4
x.index("o",0)
4
x.find("X")#-1 means substring not found
-1
x.index("X")
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    x.index("X")
ValueError: substring not found
x
'Welcome to Python Programming'
x = "Machine Learning"
len(x)
16
x.center(16)
'Machine Learning'
x.center(17)
' Machine Learning'
x.center(18)
' Machine Learning '
x.center(32)
'        Machine Learning        '
x.center(31,"*")
'********Machine Learning*******'
x = x.center(31,"*")
x
'********Machine Learning*******'
x.lstrip("*")
'Machine Learning*******'
x.rstrip("*")
'********Machine Learning'
x.strip("*")
'Machine Learning'
x = '********Machine******Learning*******
SyntaxError: unterminated string literal (detected at line 1)
x = '********Machine******Learning*******'
x.strip("*")
'Machine******Learning'
x
'********Machine******Learning*******'
x.replace("*"," ")
'        Machine      Learning       '
x.replace("*","")
'MachineLearning'
x = 'Welcome to Python Programming'
x.replace("Python","Dart")
'Welcome to Dart Programming'
x
'Welcome to Python Programming'
x.split()
['Welcome', 'to', 'Python', 'Programming']
len(x.split())
4
x
'Welcome to Python Programming'
x.split("o")
['Welc', 'me t', ' Pyth', 'n Pr', 'gramming']
x = ['Welcome', 'to', 'Python', 'Programming']
x
['Welcome', 'to', 'Python', 'Programming']
" ".join(x)
'Welcome to Python Programming'
"#".join(x)
'Welcome#to#Python#Programming'
x = "ML"
x.zfill(5)
'000ML'
x
'ML'
>>> x.isalpha()
True
>>> x = "32456trgdfsc"
>>> x.isalnum()
True
>>> x="4567823"
>>> x.isdigit()
True
>>> x = "hey"
>>> x.islower()
True
>>> x
'hey'
>>> x.startswith("h")
True
>>> x.endswith("h")
False

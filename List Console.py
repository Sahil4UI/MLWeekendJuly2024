Python 3.12.4 (v3.12.4:8e8a4baf65, Jun  6 2024, 17:33:18) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#List=>Python's Ordered And Mutable Data Collection
x = [1,2,3]
x[0]
1
x[-1]
3
x = [1,2,3,[4,5,6,[7,8,9,10]]]
x[-1][-1][2]
9
x = [1,2,3]
x.append(90)
x
[1, 2, 3, 90]
x.append(100)
x
[1, 2, 3, 90, 100]
x.insert(150,0)
x
[1, 2, 3, 90, 100, 0]
x.insert(0,150)
x
[150, 1, 2, 3, 90, 100, 0]
x.pop()#it will remove&return the last value
0
x
[150, 1, 2, 3, 90, 100]
x.pop(3)
3
x
[150, 1, 2, 90, 100]
x.remove(150)
x
[1, 2, 90, 100]
x.append(1)
x
[1, 2, 90, 100, 1]
x.remove(1)
x
[2, 90, 100, 1]
del x[0]
x
[90, 100, 1]
len(x)
3
x
[90, 100, 1]
x[1]=200
x
[90, 200, 1]
x[x.index(200)]=900
x
[90, 900, 1]
x.clear()
x
[]
del x
x
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    x
NameError: name 'x' is not defined
#List Comprehension
x = [i for i in range(1,11)]
x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
import random
random.randint(1,11)
7
random.randint(1,11)
4
random.randint(1,11)
1
random.Random()
<random.Random object at 0x143146e20>
random.choice(x)
5
random.choice(x)
3
x = [1,11,22,334,55]
random.choice(x)
1
x
[1, 11, 22, 334, 55]
random.choice(x)
55
x
[1, 11, 22, 334, 55]
x.insert(0,-100)
x
[-100, 1, 11, 22, 334, 55]
x.insert(0,9999999)
x
[9999999, -100, 1, 11, 22, 334, 55]
x.sort()
x
[-100, 1, 11, 22, 55, 334, 9999999]
x.reverse()
x
[9999999, 334, 55, 22, 11, 1, -100]
x = [9999999, -100, 1, 11, 22, 334, 55]
x.sort(reverse=True)
x
[9999999, 334, 55, 22, 11, 1, -100]
x
[9999999, 334, 55, 22, 11, 1, -100]
min(x)
-100
max(x)
9999999
sum(x)
10000322
x = [1,2,3,4,5]
y = ["ram","ankit","ishika","rohit","himanshu"]
list(zip(x,y))
[(1, 'ram'), (2, 'ankit'), (3, 'ishika'), (4, 'rohit'), (5, 'himanshu')]
x = [1,2,3]
y
['ram', 'ankit', 'ishika', 'rohit', 'himanshu']
list(zip(x,y))
[(1, 'ram'), (2, 'ankit'), (3, 'ishika')]
x
[1, 2, 3]
y
['ram', 'ankit', 'ishika', 'rohit', 'himanshu']
x.extend(y)
x
[1, 2, 3, 'ram', 'ankit', 'ishika', 'rohit', 'himanshu']
x = [1,2,3,4,5]
y = [6,7,8,9,10]
x+y
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x
[1, 2, 3, 4, 5]
y = x
x
[1, 2, 3, 4, 5]
y
[1, 2, 3, 4, 5]
del x[0]
x
[2, 3, 4, 5]
y
[2, 3, 4, 5]
id(x)
4379619008
id(y)
4379619008
#shallow copy
x
[2, 3, 4, 5]
y = x.copy()
del x[0]
x
[3, 4, 5]
y
[2, 3, 4, 5]
id(x)
4379619008
id(y)
4390176832

x = [1,2,3,[4,5,6,7]]
y = x.copy()
del x[-1][-1]
x
[1, 2, 3, [4, 5, 6]]
y
[1, 2, 3, [4, 5, 6]]
del x[0]
>>> x
[2, 3, [4, 5, 6]]
>>> y
[1, 2, 3, [4, 5, 6]]
>>> from copy import deepcopy
>>> y = deepcopy(x)
>>> x
[2, 3, [4, 5, 6]]
>>> y
[2, 3, [4, 5, 6]]
>>> del x[-1][-2]
>>> x
[2, 3, [4, 6]]
>>> y
[2, 3, [4, 5, 6]]
>>> x = [1,2,3,4]
>>> x*3
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
>>> x
[1, 2, 3, 4]
>>> x.index(4)
3

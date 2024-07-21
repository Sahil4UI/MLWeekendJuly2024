Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Tuple - Tuple is python's ordered and immutable Data Collection
>>> x = [1,2,3,4,5]
>>> y = (1,2,3,4,5)
>>> type(x)
<class 'list'>
>>> type(y)
<class 'tuple'>
>>> x.pop()
5
>>> y.pop()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    y.pop()
AttributeError: 'tuple' object has no attribute 'pop'
>>> x
[1, 2, 3, 4]
>>> x[0]=100
>>> x
[100, 2, 3, 4]
>>> y[0]=100
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    y[0]=100
TypeError: 'tuple' object does not support item assignment
x
[100, 2, 3, 4]
y
(1, 2, 3, 4, 5)
len(x)
4
max(y)
5
len(y)
5
min(y)
1
y
(1, 2, 3, 4, 5)
x = (1,1,2,2,32,3,3,4)
x.count(1)
2
x.index(4)
7
#list Comprehension
x = [i for i in range(1,11)]
x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

y = (i for i in range(1,11))
y
<generator object <genexpr> at 0x0000013D5D95FC40>
for value in y:
    print(value)

1
2
3
4
5
6
7
8
9
10

names = ["Ravi","Ruchi","Ishika"]
marks = [90,54,78]
list(zip(names,marks))
[('Ravi', 90), ('Ruchi', 54), ('Ishika', 78)]
roll = [1,2,3]
list(zip(roll,names,marks))
[(1, 'Ravi', 90), (2, 'Ruchi', 54), (3, 'Ishika', 78)]

#Dictionary
#dictionary is python's unordered and mutable data collection
#Dictionary consists of key value pairs enclosed inside curly braces separated by comma's
data = {"roll":101,"name":"ritu","marks":98}
data.keys
<built-in method keys of dict object at 0x0000013D5DEF7840>
data.keys()
dict_keys(['roll', 'name', 'marks'])
data.values()
dict_values([101, 'ritu', 98])
data
{'roll': 101, 'name': 'ritu', 'marks': 98}
data["contact"] = "9876543210"
data
{'roll': 101, 'name': 'ritu', 'marks': 98, 'contact': '9876543210'}
#Dictionary cannot contain duplicate keys
data["name"]="Ishika"
data
{'roll': 101, 'name': 'Ishika', 'marks': 98, 'contact': '9876543210'}
data.pop('contact')
'9876543210'
data
{'roll': 101, 'name': 'Ishika', 'marks': 98}
data.popitem()#It will Remove Last Key value pair
('marks', 98)
data
{'roll': 101, 'name': 'Ishika'}
del data['roll']
data
{'name': 'Ishika'}
data.clear()
data
{}
data = {'roll': 101, 'name': 'Ishika', 'marks': 98, 'contact': '9876543210'}
len(data)
4
data.items()#how many key value pairs
dict_items([('roll', 101), ('name', 'Ishika'), ('marks', 98), ('contact', '9876543210')])
data
{'roll': 101, 'name': 'Ishika', 'marks': 98, 'contact': '9876543210'}
data['roll']
101
data.get('name')
'Ishika'

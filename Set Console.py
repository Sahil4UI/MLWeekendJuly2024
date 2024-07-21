Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Set - Set is Pythons unordered and mutable data collection
>>> #Set cannot store duplicate values
>>> x = {1,2,3,4,5,1,1,1,1,2,2,2,3,3,3,4,4,4}
>>> x
{1, 2, 3, 4, 5}
>>> type(x)
<class 'set'>
>>> x
{1, 2, 3, 4, 5}
>>> x.add(100)
>>> x.add(99)
>>> x
{1, 2, 3, 4, 5, 100, 99}
>>> x.discard(99)
>>> x
{1, 2, 3, 4, 5, 100}
>>> x.discard(5)
>>> x
{1, 2, 3, 4, 100}
>>> x.add('a')
>>> x
{1, 2, 3, 4, 100, 'a'}
>>> x.add('b')
>>> x
{1, 2, 3, 4, 'b', 100, 'a'}
x = {1,2,3,4,5}
y = {4,5,6,7,8}
x.union(y)#all but without repetition
{1, 2, 3, 4, 5, 6, 7, 8}
x.intersection(y)#common
{4, 5}
x.difference(y)
{1, 2, 3}
x-y
{1, 2, 3}
x
{1, 2, 3, 4, 5}
y
{4, 5, 6, 7, 8}
x.update(y)
x
{1, 2, 3, 4, 5, 6, 7, 8}
x = {1,2,3,4,5}
y
{4, 5, 6, 7, 8}
x.intersection_update(y)
x
{4, 5}
x = {1, 2, 3, 4, 5}
y
{4, 5, 6, 7, 8}
x.difference_update(y)
x
{1, 2, 3}

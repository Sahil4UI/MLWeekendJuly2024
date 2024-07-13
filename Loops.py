#Reverse of No?
'''
x = int(input("Enter No1:"))
res = 0
for i in range(len(str(x))):
    rem = x%10
    res=res*10+rem
    x=x//10
print(res)
'''
#Check whether a number is prime or not
'''
x = int(input("Enter No:"))

for i in range(2,x):
    if x%i==0:
        print("Not Prime")
        break
else:
    print("Prime")
'''
#contiue statement is used to transfer the control flow
#of program to the starting of the loop
'''
for i in range(1,11):
    if i%2==0:
        continue
    print(i)
'''
'''
    *
   **
  ***
 ****
*****
'''
'''
for i in range(1,6):
    print(" "*(5-i),end="")
    for j in range(0,i):
        print("*",end="")
    print()
'''
'''
1
12
123
1234
12345

1
22
333
4444
55555

1
01
010
1010
10101
'''
'''
x = 1
for i in range(1,6):
    for j in range(i):
        if x%2==0:
            print(0,end="")
        else:
            print(1,end="")
        x+=1
    print()
'''
'''

*****
*   *
*****
*   *
*   *

'''
'''
for i in range(1,6):
    for j in range(1,6):
        if j in (1,5) or i in (1,3):
            print("*",end="")
        else:
            print(" ",end="")
    print()
'''
'''
for i in range(1,6):
    for j in range(1,6):
        if j in (1,5) or i==j:
            print("*",end="")
        else:
            print(" ",end="")
    print()
'''
'''
#While Loop
x = 1
while x<=10:
    print(x)
    x+=1
'''
#print All prime nos b/w 1 to 100
'''
for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
'''
'''
x = "hello Python"
for i in range(len(x)):
    print(x[i])
'''
'''
x = "hello Python"
for i in x:
    print(i)
'''
#count no of vowels and consonants in Given String
count_vowels= 0
count_cons = 0
x = "welcome to Python and ML".lower()
for i in x:
    if i>="a" and i<="z":
        if i in ["a","e","i","o","u"]:
            count_vowels+=1
        else:
            count_cons+=1
print("Vowels Count=>",count_vowels)
print("Consonant Count=>",count_cons)




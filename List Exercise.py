#find the largest no from the list without using max or sort
'''
x = [33,55,77,89,454]
max1=-99999999999999
max2=-88888888888888
for i in range(0,len(x)):
    if x[i]>max1:
        max2 = max1
        max1 =x[i]
    elif x[i]>max2:
        max2=x[i]
        
print(max1,max2)
#find second largest
'''
#Sorting->Ascending Order
x = [1,2,34,-100,34,5436,0]

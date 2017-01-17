from __future__ import print_function

import sys
#determining the number of rows and columns required for making the rectangle
def detmn(num):
    for i in xrange(2,num/2+1):
        if i*(i+1) >= num:
            return(i,i+1)
            break


#inputting the string and remove spaces
str1 = raw_input("Enter the string to encoded as per crypto-square: ")
for i in str1:
    if ((ord(i)<97 and ord(i)>90) or ord(i)<65 or ord(i)>122):
        str1 = str1.replace(i,'')
str1 = str1.replace(' ','')


#print the original string and number of rows and columns
print(str1)
num = len(str1)
print("length: ",num)
m,n = detmn(num)
print("Number of rows: ",m)
print("Number of columns: ",n)
    

#printing the rectangle
for i in xrange(len(str1)):
        if (i+1) % n == 0:
            print(str1[i])
        else:
            print(str1[i],end="")
print("")


#encoding using the rectangle
print("The encoded message is: ")
for i in xrange(n):
    j = i
    while j<len(str1):
        print(str1[j],end="")
        j += n

print("")

    
    



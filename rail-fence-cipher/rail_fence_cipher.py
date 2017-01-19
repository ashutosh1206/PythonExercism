from __future__ import print_function
import sys


def encode(str1):
    str2 = ""
    for i in xrange(3):
        j = i
        if i != 0:
            if i == 1:
                print(".",end=" ") 
            else:
                print(". .",end=" ")
        while j < len(str1):
            print(str1[j],end=" ")
            str2 += str1[j]
            if i == 1:
                j += 2
                print(".",end=" ")
            else:
                j += 4
                print(". . .",end=" ")
        print("")
    return str2

def decode(str1):
    rownum = 1
    pos = 0
    for rownum in xrange(1,4):
        temp = 0
        if rownum != 1:
            if rownum == 2:
                print(".",end=" ")
                temp += 1
            else:
                print(". .",end=" ")
                temp += 2
        i = temp
        while i < len(str1):
            print(str1[pos],end=" ")
            pos += 1
            if rownum == 2:
                i += 2
                print(".",end=" ")
            else:
                i += 4
                print(". . .",end=" ")
        print("")
            
    
print("1. Encode")
print("2. Decode")
c =  input("Enter Choice: ")
if c ==1:
    str1 = raw_input("Enter the string to be encoded: ")
    str1 = str1.replace(' ','')
    encoded = encode(str1)
    print("The encoded form of the string is: ",encoded)
elif c == 2:
    str1 = raw_input("Enter the string to be decoded: ")
    str1 = str1.replace(' ','')
    decode(str1)
else:
    raise AssertionError


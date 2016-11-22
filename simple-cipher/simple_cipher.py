encstr = []
decstr = raw_input("Enter the string to be encoded: ")
key = input("Enter the length upto which you want to shift the alphabets: ")
decstr = list(decstr)
for i in decstr:
    if (ord(i)+key)>122:
        newkey = key - (122 - ord(i))
        i = chr(97 + (newkey-1))
        encstr.append(i)
    else:
        i = chr(ord(i)+key)
        encstr.append(i)
encstr = ''.join(encstr)
print "The encoded form of the string is: ",encstr

    

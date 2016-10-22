str1 = raw_input("Enter a string of digits: ")
cnt = len(str1)
leng = input("Enter the length of the possible substring: ")
i = 0
if leng < cnt:
    while i + leng <= cnt:
        j = i
        while j != i + leng:
            print str1[j],
            j += 1
        print '\n'
        i += 1
elif leng == cnt:
    print str1
    
    
    

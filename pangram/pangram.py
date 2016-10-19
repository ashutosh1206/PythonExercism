str1 = raw_input("Enter the string to be checked as pangram: ")
list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
while str1[i]!='\0':
    while j in list1:
        if list1[j]==str1[i]:
            del list1[j]
        else:
            j=j+1
if not list1:
    print "The string entered is a pangram"
else:
    print "The string entered is not a pangram"

    
        
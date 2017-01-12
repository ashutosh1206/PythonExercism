str1 = raw_input("Enter the string to be encoded in PigLatin: ")
list1 = list(str1)
vowel = ['a','e','i','o','u']
i = 0
while i in xrange(len(list1)):
    if list1[i] in vowel:
        list1.append("way")
        str1 = ''.join(list1)
        break
    else:
        temp = list1[i]
        list1.remove(list1[i])
        list1.append(temp)
print str1
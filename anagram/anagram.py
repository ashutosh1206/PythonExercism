str1 = raw_input("Enter a string to be checked as anagram: ")
lim = input("Enter the number of strings to be checked with the base string: ")
i=0
list1 = []
while i < lim:
    ins = raw_input("Enter the string: ")
    list1.append(ins)
    i = i + 1
num=0
while num < lim:
    for ch in str1:
        if ch not in list1[num]:
            del list1[num]
    num = num + 1
print list1





    
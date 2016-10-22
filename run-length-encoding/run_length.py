str1 = raw_input("Enter the string to be used for applying run-length-encoding")
n = len(str1)
list1 = []
i=0
while i < n:
    cnt = 0
    for j in range(i,n):
        if str1[i] == str1[j]:
            cnt += 1
            add = j
        else:
            break
    list1.append(cnt)
    list1.append(str1[i])
    i = i + add + 1
print list1


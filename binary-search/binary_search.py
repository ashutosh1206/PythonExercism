lim = input("Enter the number of elements to be entered: ")
list1 = []
i=0
while i < lim:
    c = raw_input("Enter the numbers in ascending order: ")
    list1.append(c)
    i = i + 1
srch = input("Enter the element to be searched: ")
high = lim - 1
low = 0
while low <= high:
    mid = (low + high)/2
    if(srch < list1[mid]):
        high = mid - 1
    elif(srch > list1[mid]):
        low = mid + 1
    elif(srch == list1[mid]):
        print "Element found at position ", mid
        break
print high
print low
print mid




    
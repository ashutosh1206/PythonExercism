def chknum(num):
    list1 = list(str(num))
    i = len(str(num)) - 1
    cnt = 0
    # converting the number as per the conditions of luhn number
    while i >= 0:
        if cnt%2 != 0:
            temp  = int(list1[i])
            temp *= 2
            if temp > 10: 
                temp-= 9
            list1[i] = str(temp)
        i -= 1
        cnt += 1
    sum = 0
    # checking if the number is luhn number
    for i in xrange(len(list1)):
        tmp = list1[i]
        sum += int(tmp)
    return sum

num = input("Enter a number: ")
chksum = chknum(num)
print "The check sum is:",chksum
if chksum%10==0:
    print "Clearly, the number is a Luhn Number"
    c = 1
else:
    print "THe number is not a Luhn Number"
    c = 0

    

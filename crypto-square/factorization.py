import math
list1 = []
num = input("Enter a number: ")
#c = math.sqrt(num)
#c = int(math.floor(c))
#print c

for i in xrange(2,num/2+1):
    if i*(i+1) >= num:
        list1.append(i)
        list1.append(i+1)
        break
print list1

#for i in xrange(pow(num,1/2)):
    #print i
    
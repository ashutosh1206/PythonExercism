marklist=[]
def mark(n,lim):
    i = n
    while n * i <= lim:
        marklist.append(n * i)
        i += 1
    
lim = input("Enter the limit upto which you want to print the prime numbers: ")
listev = []
listod = []
for i in range(2,lim + 1):
    if i in marklist:
        continue
    else:
        j = 2
        cnt = 0
        while j <= i/2:
            if i % j == 0:
                listev.append(i)
                cnt += 1
                break
            j += 1
        if(cnt == 0):
            listod.append(i)
            mark(i,lim)
print "The list of prime numbers is: ",listod

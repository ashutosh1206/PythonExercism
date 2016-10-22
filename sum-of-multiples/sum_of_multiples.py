lim = input("Enter the limit of numbers upto which you want to find the multiples and thus their sum: ")
ans = 'Y'
nummul = []

while ans == 'y' or ans == 'Y':
    c = input("Enter the number you wish to use for getting the sum of multiples: ")
    nummul.append(c)
    ans = raw_input("Enter want to input more numbers?(Y/N) : ")
listmul = []
for num in nummul:
    j = 1
    while num * j < lim:
        multiple = num * j
        if multiple not in listmul:
            listmul.append(multiple)
        j += 1
print "The list of multiples is: ", listmul
sum1 = 0
for number in listmul:
    sum1 = sum1 + number
print "The sum of the multiples is: ", sum1

    
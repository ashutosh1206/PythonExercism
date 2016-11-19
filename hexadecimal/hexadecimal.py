inp = raw_input("Enter a hexadecimal number: ")
length = len(inp)
num = 0
cnt = length-1
for i in inp:
    if i == 'a':
        num = num + ((16**(cnt))*10)
    elif i == 'b':
        num = num + ((16**(cnt))*11)
    elif i == 'c':
        num = num + ((16**(cnt))*12)
    elif i == 'd':
        num = num + ((16**(cnt))*13)
    elif i == 'e':
        num = num + ((16**(cnt))*14)
    elif i == 'f':
        num = num + ((16**(cnt))*15)
    elif i >= '0' and i <= '9':
        num = num + ((16**(cnt))*int(i))
    else:
        print "Enter a valid hexadecimal number"
        exit()
    cnt = cnt - 1
print "The decimal form of the number is: ",num
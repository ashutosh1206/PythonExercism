def detmn(num):
    for i in xrange(2,num/2+1):
        if i*(i+1) >= num:
            return(i,i+1)
            break


def main():
    str1 = raw_input("Enter the string to encoded as per crypto-square: ")
    str1 = str1.replace(' ','')
    print str1
    num = len(str1)
    print num
    m,n = detmn(num)
    print m,n
    
    



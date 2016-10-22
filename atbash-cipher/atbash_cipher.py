def revascii(ch):
    x = ord(ch) - 97
    ord(ch) = 122 - x
    return ch
        
def encode(str2):
    for i in range(0,len(str2)):
        str2[i] = revascii(str2[i])
    print str2


def decode(str2):
    encode(str2)


ans = input("Enter your choice whether you want to encode or decode the message, if you want to encrypt input 0 and to decrypt input 1: ")
str1 = raw_input("Enter the string: ")
if ans == 0:
    encode(str1)
elif ans == 1:
    decode(str1)
else:
    print("Wrong choice, try again!")


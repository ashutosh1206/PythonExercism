itera = input("Enter the number of iterations to be done: ")

for i in range(0,itera):
    str1 = raw_input("Start conversating with bob!")
    if '!' in str1:
        print "Whoa, chill out!"
    elif '?' in str1:
        print "Sure."
    elif str1.lower() == "bob":
        print "Fine. Be that way!"
    else:
        print "Whatever"

    

string=raw_input("Enter a DNA strang: ")
temp=string
i=0
while(string[i]!='\0'):
    if(string[i]=='G'):
        string[i]='C'
    elif(string[i]=='C'):
        string[i]='G'
    elif(string[i]=='T'):
        string[i]='A'
    elif(string[i]=='A'):
        string[i]='U'
print("The string entered is %s",temp)
print("The RNA transcription of the given DNA strang is %s",string)


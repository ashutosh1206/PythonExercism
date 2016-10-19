str1= raw_input("Enter one strang of DNA: ")
str2= raw_input("Enter another strang of DNA: ")
i=0,count=0
while(str1[i]!='\0' and str2[i]!='\0'):
    if(str1[i]==str2[i]):
        count=count+1
    i=i+1
print("The hamming difference between the two DNA strangs is %d",count)

a=int(input("Enter First Number : "))
b=int(input("Enter Second Number : "))
c=int(input("Enter Third Number : "))
if a>b & a>c:
 largest=a
elif b>a & b>c:
 largest=b
else:
 largest=c
print("The largest of three numbers is : ",largest)
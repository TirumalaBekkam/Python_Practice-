#check wheater the given number is strong number or not
num=int(input("enter number:"))
copy=num
sum=0
while(num>0):
    rem=num%10
    fact=1
    for i in range(1,rem+1):
        fact=fact*i
    sum=sum+fact
    num=num//10
if sum==copy:
    print(copy,"is strong number")
else:
    print(copy,"is not strong number")
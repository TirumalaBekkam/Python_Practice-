#program to check whether given number is Happy number or not 
num=int(input("enter num:"))
visit=set()
while num!=1 and num not in visit:
    visit.add(num)
    sum=0
    temp=num
    while temp>0:
        d=temp%10
        sum=sum+d**2    
        temp=temp//10
    num=sum
if num==1:
    print("happy number")
else:
    print("sad number")
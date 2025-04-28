#Checking the number is armstrong or not 
num=int(input("enter number:"))  #ex:number=153
sum=0
copy=num
l=len(str(num))  #length=3
while(num>0):            
    rem=num%10  # rem stores the last digit of thr number
    sum=sum+pow(rem,l)  #armstrong number evaluation  1³ + 5³ + 3³ =153
    num=num//10 # gives two digit number of thr given number 
if copy==sum: # if taken number equal to sum 
    print("The given number is armstrong")
else:
    print("The given number is not armstrong")
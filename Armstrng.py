num=int(input("Number= "))
temp=num
sum=0
while(num!=0):
    rem=num%10
    sum=sum+(rem*rem*rem)
    num=num//10
if temp==sum:
    print(sum," is an Armstrong number")
else:
    print(sum,"Not an Armstrong number")

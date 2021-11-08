mylist = []
print("Enter no.of elements for the list: ")
n=int(input())
print("Enter the Elements:")
sum=0
for i in range(n):
    val = int(input())
    mylist.append(val)
max=min=mylist[0]
for i in mylist:
    sum+=i
    if i>max:
        max=i
    if i<min:
        min=i

print("Average = ",sum/n,"\nMaximum value = ",max,"\nMinimum value = ",min)
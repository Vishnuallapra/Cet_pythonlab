myList=list(map(int,input("Enetr random numbers: ").split()))
print("List: ",myList)
newList=[]
for i in myList:
    if i%2!=0:
        newList.append(i)

print("List After Removing Even Numbers: ",newList)

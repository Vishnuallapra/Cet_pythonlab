l=list(map(int,input("Enter random numbers:").split()))
print("List:",l)
new_lst=[i for i in l if i%2==0]
print("List of Even Numbers: ",new_lst)

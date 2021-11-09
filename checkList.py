list1=list(map(int,input("Enter first nlist : "). split()))
list2=list(map(int,input("Enter second nlist : "). split()))
if len(list1)==len(list2):
     print("Both of the list have same size")
else:
     print("Both lists have different size")

if sum(list1)==sum(list2):
     print("Both lists have same Sum")
else:
     print("Both lists have different sum")

if set(list1)==set(list2):
     print("Both lists have same values")
else:
     print("Both lists have different values")

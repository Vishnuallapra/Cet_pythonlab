dic_one={}
dic_two={}
n1=int(input("No.of Elements in Dictionary1:"))
for i in range(n1):
        k1=input("Enter Key:")
        v1=input("Enter value:")
        dic_one[k1]=v1
n2=int(input("No.of Elements in Dictionary2:"))
for i in range(n2):
        k2=input("Enter Key:")
        v2=input("Enter value:")
        dic_two[k2]=v2
print("Dictionary1:",dic_one)
print("Dictionary2:",dic_two)
dic_one.update(dic_two)
print("Merged Dictionary:",dic_one)

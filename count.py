str=input("Enter String: ").split()
for i in set(str):
    count=1
    for k in range(str.index(i) + 1,len(str)):
        if i==str[k] :
            count+=1
    print(i," occurs ",count," Times")

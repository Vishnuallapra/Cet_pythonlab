values=input("Enter Random values: ").split()
new_list = []
for value in values:
    if int(value) > 100:
        new_list.append("OVER")
    else:
        new_list.append(int(value))
print(new_list)
        

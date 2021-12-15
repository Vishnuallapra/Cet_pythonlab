s=input("String: ")
ch=s[0]
print(ch + s[1:].replace(ch, "$"))

#print(ch + "".join(["$" if x == ch else x for x in s[1:]]))
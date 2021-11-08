str1=input("first string: ")
str2=input("second string: ")
char=str1[:2]
str1=str1.replace(str1[:2],str2[:2])
str2=str2.replace(str2[:2],char)
str3=str1+" "+str2
print("Your string has become :- ",str3)

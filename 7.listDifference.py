
set1=set(input("first colorlist: ").split())
set2=set(input("second colorlist: ").split())
print("SET1 - ",set1)
print("SET2 - ",set2)
set1.difference_update(set2)
print("After SetDifference operation(SET1-SET2): ",set1)

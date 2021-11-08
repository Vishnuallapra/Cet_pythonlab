mylist = []
print("Enter no.of elements for the list: ")
n=int(input())
print("Enter the Elements:")

for i in range(n):
    val = int(input())
    mylist.append(val)

print("\nEnter an element to be search: ")
elem = int(input())

for i in range(n):
    if elem == mylist[i]:
        print("\nElement found at position:", i+1)
        break

else:
    print("Item not found")
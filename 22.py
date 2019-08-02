a=[]
m=int(input("Enter number of elements:"))
for i in range(1,m+1):
    c=int(input("Enter element:"))
    a.append(c)
a.sort()
print("Largest element is:",a[ m-1])

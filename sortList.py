a=[]
print("Enter 0 for exit and print")
d = int(input("Enter no. one by one : "));
a.append(d)
while(d!=0):
    d = int(input("Enter no. one by one : "))
    a.append(d)
a.pop()
print("original order : ",end=" ")
for i in range (0,len(a)):
    printf(a[i],end=" ")
a.sort()
print(" & in Ascending order : ",end=" ");
for i in range (0,len(a)):
    printf(a[i],end=" ")

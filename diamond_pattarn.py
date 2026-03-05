rowsize= int (input("Enter the number of rows:"))
if rowsize %2==0:
    Halfdiamrow =int(rowsize/2)
else:
    Halfdiamrow = int(rowsize/2)+1
space = (Halfdiamrow-1 )
for i in range(1,Halfdiamrow+1):
    for j in range(1,space+1):
        print(end=" ")
    space=space-1
    num=1
    for j in range(2*i-1):
        print(end=str(num))
        num=num+1
    print=()
space=1
for i in range(1,Halfdiamrow):
    for j in range(1,space+1):
        print(end="  ")
    space=space+1
    num=1
    for j in range(1,2*(Halfdiamrow-i)):
        print(end=str(num))
        num=num+1
    print()
    

 
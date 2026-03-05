row=int(input("Please enter the total number of rows:"))
Number=1
print("Floyd's Triangle")
for i in range(1,row+1):
    for j in range(1,i+1):
        print(Number,end="  ")
        Number= Number+1
    print()

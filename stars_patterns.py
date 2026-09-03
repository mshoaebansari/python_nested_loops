'''
c=input("Enter the character!")
for i in range(1,int(input("Enter number of rows:"))+1):    
    for j in range(1,i+1):  
        print(c,end=" ")
    print()

# floyed triangle
k=1
for i in range(1,int(input("Enter numebr of rows:"))+1):
    for j in range(i):
        print(k,end=" ")
        k+=1
    print()

'''
k='A'
for i in range(1,int(input("Enter numebr of rows:"))+1):
    for j in range(i):
        print(k,end=" ")
        k=ord(k)
        k+=1
        k=chr(k)
        
    print()

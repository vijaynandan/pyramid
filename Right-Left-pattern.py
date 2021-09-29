def pattern(n):
    for i in range(1,n):
        for j in range(i,n):
            print(" ",end=" ")
        for j in range(n):
            print("-", end=" ") 
        for i in range(j):
            print("#", end=" ") 
        for i in range(j+1):
            print("+", end=" ")    
        print()
    for i in range(n,0,-1):
        for j in range(i,n):
            print(" ",end=" ")
        for j in range(n):
            print("-", end=" ") 
        for i in range(j):
            print("#", end=" ") 
        for i in range(j+1):
            print("+", end=" ")    
        print()
    
n=5
pattern(n)
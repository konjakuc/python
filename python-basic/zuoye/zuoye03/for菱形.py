for i in range(1,5):
    for k in range(4,i,-1):
        print("   ",end="")
    for j in range(1,2*i):
        print("  *",end="")
    print()
for i in range(3,0,-1):
    for k in range(3,i-1,-1):
        print("   ",end="")
    for j in range(1,2*i):
        print("  *",end="")
    print()

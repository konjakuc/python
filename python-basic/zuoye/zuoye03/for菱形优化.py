for i in range(1,5):
    print("   "*(4-i),end="")
    print("*  "*(2*i-1))
for i in range(3,0,-1):
    print("   "*(4-i),end="")
    print("*  "*(2*i-1))

print("\n".join([" "*(4-i)+"*"*(2*i-1) for i in [1,2,3,4,3,2,1]]))

def triangles1(n):
    a=[1]
    print('  '*(n-1)+"1")
    while len(a)<=n-1:
        ar = [0] + a + [0]
        a = [ar[x-1] + ar[x] for x in range(1,len(ar))]
        for j in range(n-len(a)):
            print("  ",end="")
        for i in a:
            print("%-2d"%i,end="  ")
        print()

triangles1(8)
print("-"*30)

def triangles2(n):
    a=[1]
    while len(a)<=n-1:
        ar = [0] + a + [0]
        a = [ar[x-1] + ar[x] for x in range(1,len(ar))]
    for i in a:
        print(i,end="  ")
triangles2(8)
n=int(input("input n(3,5,7,9...):"))
#生成魔阵
row,col=0,n//2
magic=[]
for i in range(n):
    magic.append([0]*n)
magic[row][col]=1
for i in range(2,n*n+1):
    r,l=(row-1+n)%n,(col+1)%n
    if(magic[r][l]==0):row,col=r,l
    else: row=(row+1)%n
    magic[row][col]=i
#输出
t=len(str(n*n))  #计算n*n的位数
for i in magic:
    for j in i:
        print("%-*d" % (t,j),end="  ") #左对齐，占位是t
    print("")
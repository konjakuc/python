for i in range(1,5):
    for j in range(1,6):
        k=j+(i-1)*5
        print("%.2d\t"%k,end="")
    print()

for i in range(1,21):
    if i % 5 == 1:
        print()
    print("%.2d\t"%i,end="")
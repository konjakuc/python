def bubble_sort(list1):
    for i in range(len(list1)-1):       #确定循环次数
        for j in range(len(list1)-i-1):         #j为下标
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1]=list1[j+1],list1[j]
    print(list1)

testList=[2,43,453,-32,5465,432,23,13,4345,233,435,765]
bubble_sort(testList)

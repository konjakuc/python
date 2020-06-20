def select_sort(list1):
    for i in range(len(list1)-1):
        min_index=i
        for j in range(i+1,len(list1)):
            if list1[j]<list1[min_index]:
                min_index=j
        list1[i],list1[min_index]=list1[min_index],list1[i]
    print(list1)

testList=[2,43,453,-32,5465,432,23,13,4345,233,435,765]
select_sort(testList)

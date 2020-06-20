def insert_sort(list1):
    for i in range(1,len(list1)):
        current=list1[i]            #当前元素
        pre_index=i-1               #与当前元素比较的元素的下标
        while pre_index>=0 and current<list1[pre_index]:
            list1[pre_index+1]=list1[pre_index]        #如果当前元素小于比较元素则把比较元素后移
            pre_index-=1                         #继续判断前面的元素
        list1[pre_index+1]=current              #如果当前元素大于比较元素则退出while循环并插入到其后的位置
    print(list1)

testList=[2,43,453,-32,5465,432,23,13,4345,233,435,765]
insert_sort(testList)
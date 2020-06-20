people={}
#此处for循环会输出{1: 1, 2: 1, 3: 1, ..., 30: 1}，相当于给30个人都赋初始值1
for x in range(1,31):
    people[x]=1
# print(people)
#check记数，0-9；i为人们的编号，1-30；j为下船的人数
check=0
i=1
j=0
while i<=31:
    #因为只有30人，当i等于31时，手动将i置为1
    if i == 31:
        i=1
    #下船15人后退出循环
    elif j == 15:
        break
    else:
        #people[i]为0时，表示此人已下船，i加1,check不增加，继续循环
        if people[i] == 0:
            i+=1
            continue
        else:
            check += 1
            # i=1,check=1,...i=9,check=9
            if check == 9:
                #数到9的人的值设为0（下船），check置0，重新开始计数
                people[i]=0
                check = 0
                print("{}号下船了".format(i))
                #j为下船的人数，下一个人j加1
                j+=1
            else:
                i+=1
                continue
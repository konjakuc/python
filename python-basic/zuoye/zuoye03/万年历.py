def isLeapYear(year):#判断是否是闰年
    return True if (year % 100 != 0 and year % 4 == 0) or year % 400 ==0 else False

def monthDay(year,month):#判断当前月天数
    li = [31,28,31,30,31,30,31,31,30,31,30,31]
    if isLeapYear(year):
        li[1] = 29
    return li[month-1]

def totalDay(year, month):#距1900年1月1日的天数
    days = 0
    for index_year in range(1900, year):
        days += 366 if isLeapYear(index_year) else 365
    for index_month in range(1, month):
        days += monthDay(year, index_month)
    return days

def show(): #显示当前月
    year= eval(input("输入年份："))
    month = eval(input("输入月份："))
    space_num = totalDay(year, month) % 7 + 1
    #print("空格数",space_num)
    # print("星期",totalDay(year, month) % 7 + 1,"开始")
    print("\t日\t一\t二\t三\t四\t五\t六")
    for i in range(1, monthDay(year,month) + 1):
        if (i == 1):
            for j in range(space_num % 7):
                print("\t",end="")
        print("\t%.2d"%i,end="")
        if (i + space_num) % 7 == 0:
            print()
show()


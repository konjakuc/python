str=input("请输入：")
if 6<=len(str)<=18:
    if "a"<=str[0]<="z" or "A"<=str[0]<="Z":
        for char in str:
            if char=="_" or "a"<=char<="z" or "A"<=char<="Z" or char.isdigit()==True:
                continue
            else:
                print("请检查是否由字母、数字、下划线组成")
                exit()
        print("格式正确")
    else:
        print("请检查是否是字母开头")
else:
    print("请检查长度")
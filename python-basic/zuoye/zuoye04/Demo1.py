str=input("请输入：")

if "@" in str and "." in str:
    if str[0]!="@":
        if str.index(".")-str.index("@")>2:
            print("格式正确")
        else:
            print("请检查@和.的位置")
    else:
        print("开头不能为@")
else:
    print("请检查是否有@和.")
# 字符串中相同字符索引

def indexMany(s, str):  # str是要查询的字符
    length = len(s)  # 获取该字符串的长度
    str1 = s  # 拷贝字符串
    list = []
    sum = 0  # 用来计算每次截取完字符串的总长度
    try:
        while str1.index(str) != -1:  # 当字符串中没有该字符则跳出
            n = str1.index(str)  # 查询查找字符的索引
            str2 = str1[0:n + 1]  # 截取的前半部分
            str1 = str1[n + 1:length]  # 截取的后半部分
            sum = sum + len(str2)  # 计算每次截取完字符串的总长度
            list.append(sum - 1)  # 把所有索引添加到列表中
            length = length - len(str2)  # 截取后半部分的长度
    finally:
        return list


s = "aaabddabb"  # 测试用的字符串
print(indexMany(s, "a"))

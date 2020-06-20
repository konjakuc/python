class ShortInputError(Exception):
    def __init__(self, length, min_length):
        self.length = length
        self.min_length = min_length

    def __str__(self):
        return f'您输入的长度为{self.length},要求最短长度为{self.min_length}'


def main():
    try:
        pwd = input("请输入：")
        if len(pwd) < 3:
            raise ShortInputError(len(pwd), 3)
    except Exception as result:
        print(result)
    else:
        print("输入完成")


main()

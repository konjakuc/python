a = list(range(1, 31))  # a=[1,2,3,...29,30]这是人的代号
while len(a) > 15:
    print(f'{a[8]}号下船了')
    a = a[9:] + a[:8]  # 更新列表（去掉a[8],并从a[9]重新开始）

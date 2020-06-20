def splitDiy(s, sep):
    list1 = []
    i = 0
    while len(s) > i:
        if s[i] == sep:
            list1.append(s[:i])
            s = s[i + 1:]
            i = 0
            continue
        elif len(s) - i == 1:
            list1.append(s)
        i += 1
    print(list1)


str = "asv avs fas gf gdf"
splitDiy(str, " ")
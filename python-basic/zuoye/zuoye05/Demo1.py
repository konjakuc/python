def copyFiles(sourceFiles, targetFiles):
    import os
    if os.path.exists(targetFiles) == False:
        os.makedirs(targetFiles)
    list1 = os.listdir(sourceFiles)
    for i in list1:
        print(i)
        print(os.path.isfile(i))
        if i.endswith(".py") and os.path.isfile(i):
            f1 = open(os.path.join(sourceFiles, i), "r", encoding="utf-8")
            print("f1打开")
            f2 = open(os.path.join(targetFiles, i), "w", encoding="utf-8")
            print("f2打开")
            while True:
                line = f1.readline()
                if line == "":
                    break
                f2.write(line)
            f1.close()
            f2.close()


copyFiles(r"D:\Users\Administrator\python-workspace\exercise\zuoye01",
          r"D:\Users\Administrator\python-workspace\exercise\Demo2")

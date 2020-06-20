f = open("scores.txt", "w", encoding="utf-8")
f.write("张三,60,70,80\n李四,30,40,50\n王五,71,72,73\n赵六,80,58,74\n"
        "钱七,75.5,65,88\n孙八,67.5,56,66\n杨九,77,66.5,55\n吴十,92,83.5,74\n")
f.close()

f1 = open("scores.txt", "r", encoding="utf-8")
f2 = open("result.txt", "w", encoding="utf-8")


def average_score(array):  # 求平均分
    avg_score = sum(array) / len(array)
    return avg_score


allScoreInfo = []  # 所有人的成绩信息
allSumScore = []  # 所有人的总成绩
allFistScore = []  # 所有人的第一科成绩
allSecondScore = []  # 所有人的第二科成绩
allThirdScore = []  # 所有人的第三科成绩
i = 0
while True:
    line = f1.readline()

    if line == "":
        break

    personScoreInfo = line.split(",")  # ['张三', '60', '70', '80\n']
    personSumScore = float(personScoreInfo[1]) + float(personScoreInfo[2]) + float(personScoreInfo[3][:-1])

    allScoreInfo.append(personScoreInfo)
    allSumScore.append(personSumScore)

    allFistScore.append(float(personScoreInfo[1]))
    allSecondScore.append(float(personScoreInfo[2]))
    allThirdScore.append(float(personScoreInfo[3][:-1]))

    i += 1

allSumScore.sort()
allFistScore.sort()
allSecondScore.sort()
allThirdScore.sort()
maxSumScore = allSumScore[-1]  # 最高分
minSumScore = allSumScore[0]  # 最低分

classAverageScore = average_score(allSumScore[1:-1])  # 班级平均分
fistAverageScore = average_score(allFistScore[1:-1])  # 第一科平均分
secondAverageScore = average_score(allSecondScore[1:-1])  # 第二科平均分
thirdAverageScore = average_score(allThirdScore[1:-1])  # 第三科平均分

f2.write("学生总数为：{}\n".format(i))

for personScoreInfo in allScoreInfo:
    if float(personScoreInfo[1]) + float(personScoreInfo[2]) + float(personScoreInfo[3][:-1]) == maxSumScore:
        f2.write("最高分学生：{}总分为：{}\n".format(",".join(personScoreInfo), maxSumScore))
    if float(personScoreInfo[1]) + float(personScoreInfo[2]) + float(personScoreInfo[3][:-1]) == minSumScore:
        f2.write("最低分学生：{}总分为：{}\n".format(",".join(personScoreInfo), minSumScore))

f2.write("班级平均分：%.2f\n" % classAverageScore)
f2.write("第一科平均分：%.2f\n" % fistAverageScore)
f2.write("第二科平均分：%.2f\n" % secondAverageScore)
f2.write("第三科平均分：%.2f\n" % thirdAverageScore)

f1.close()
f2.close()

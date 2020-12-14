from PyQt5.QtCore import QDate

# 과제를 중요도-긴급도로 정렬하는 함수
def subjectSort(subjectList):

    s = {"상": 1, "중상": 2, "중": 3, "중하": 4, "하": 5}
    p_list = []
    d_list = []
    newSubjectList = []

    for i in subjectList:
        p = s[i["priority"]]
        d = i["deadLine"]

        dQDate = QDate.fromString(d, 'yyyy.MM.dd')
        currentDate = QDate.currentDate()
        interval = currentDate.daysTo(dQDate)

        p_list.append(p)
        d_list.append(interval)

    for i in range(len(subjectList)):

        if max(d_list) != 0:
            maxD = round(max(d_list) / 5)
        else:
            maxD = 1
        #print(interval)

        #print(subjectList[i])
        subjectList[i]["orderScore"] = p_list[i]**2 + (round(d_list[i]/maxD)**2)
        newSubjectList.append(subjectList[i])

    return newSubjectList


# 테스트를 위한 코드
#L = [{'subjectName': '3', 'priority': '중', 'deadLine': '2020.12.09'}, {'subjectName': '1', 'priority': '중상', 'deadLine': '2020.12.23'}, {'subjectName': '4', 'priority': '중', 'deadLine': '2020.12.21'}]
#n = subjectSort(L)
#print(n)
from PyQt5.QtCore import QDate


# 과제를 중요도-긴급도로 정렬하는 함수
def subjectSort(subjectList):
    s = {"상": 1, "중상": 2, "중": 3, "중하": 4, "하": 5}
    p_list = []  # 중요도를 저장하는 리스트
    d_list = []  # 남은 기한을 저장하는 리스트
    newSubjectList = []

    ...

    for i in subjectList:
        p = s[i["priority"]]
        d = i["deadLine"]

        dQDate = QDate.fromString(d, 'yyyy.MM.dd')  # 문자열에서 날짜값을 가져온다.
        currentDate = QDate.currentDate()  # 현재 시스템의 날짜값을 갖는 객체를 만든다.
        interval = currentDate.daysTo(dQDate)  # QDate 객체(currentDate)와 Parameter(dQDate)가 몇일 차이인지 알려준다.

        p_list.append(p)
        d_list.append(interval)

    for i in range(len(subjectList)):

        if max(d_list) != 0:
            maxD = round(max(d_list) / 5)  # 우선순위를 계산할 때 중요도와 비율을 맞추기 위해 maxD를 초기화
        else:
            maxD = 1

        # 중요도, 긴급도에 따라 우선순위 수치를 1~61로 구분(최소 1 + 0, 최대 25 + 36)
        subjectList[i]["orderScore"] = p_list[i] ** 2 + (round(d_list[i] / maxD) ** 2)
        newSubjectList.append(subjectList[i])

    return newSubjectList

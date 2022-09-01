def solution(N, stages):
    answer = []
    answerli = []
    stages.sort()
    for i in range(1, N + 1):
        if stages.count(i) == 0:
            fail = 0
        else:
            fail = stages.count(i)/len(stages)
        answerli.append([fail, i])
        for j in range(stages.count(i)):
            stages.remove(i)
    for item in sorted(answerli, key=lambda x:x[0],reverse=True):
        answer.append(int(item[1]))
    # for n in range(len(answerli)-1, -1, -1):
    #     for m in range(0, n, 1):
    #         if answerli[n][0] == answerli[m][0] and answerli[n][1] < answerli[m][1]:
    #             answerli[n], answerli[m] = answerli[m], answerli[n]
    #         if answerli[n][0] > answerli[m][0]:
    #             answerli[n], answerli[m] = answerli[m], answerli[n]
    # for k in answerli:
    #     answer.append(k[1])
    return answer

print(solution(5, [2,1,2,6,2,4,3,3]))
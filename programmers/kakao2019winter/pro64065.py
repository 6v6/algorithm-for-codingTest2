def solution(s):
    answer = []
    slist = s[2:-2].split("},{")
    slist = sorted(slist, key=len)

    for ls in slist:
        item = list(map(int, ls.split(",")))
        for i in item:
            if i not in answer:
                answer.append(i)

    return answer


def beforeSolution(s):
    answer = []
    s = s[1:len(s)-1]
    list = []
    temp = []
    t = ''
    for letter in s:
        if letter != "{" and letter != "}" and letter != ",":
            t += letter
        elif letter == "," and t != '':
            temp.append(t)
            t = ''
        elif letter == "}":
            temp.append(t)
            list.append(temp)
            temp = []
            t = ''
    list = sorted(list, key=len)

    for ls in list:
        for i in ls:
            if int(i) not in answer:
                answer.append(int(i))

    return answer

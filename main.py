
import pandas as pd
import numpy as np
import re


def getMarkedFromFile(fname):
    file = open(fname)
    marks = ""
    for line in file.readlines():
        m = re.findall(r"(<[^>]*>)([^<>]*?)(<\/[^>]*>)", line)
        if m:
            for item in m:
                s = "".join(item)
                marks += s + "\n"
    marks = marks[:len(marks)-1]
    return marks


def markedDict(marked):
    marked = marked.split(sep='\n')
    marks = {}
    for item in marked:
        m = re.search(r"(<[^>]*>)([^<>]*)", item)
        if m:
            s = m.group(0).split('>',)
            s[0] += '>'
            if s[0] not in marks:
                marks[s[0]] = [s[1]]
            else:
                marks[s[0]].append(s[1])
    print(marks)
    return marks



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = markedDict(getMarkedFromFile("example.txt"))
    df = pd.DataFrame.from_dict(data=data, orient='index').transpose()
    print(df.head())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

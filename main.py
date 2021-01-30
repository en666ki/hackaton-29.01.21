import re
import time

start_time = time.time()


def getMarkedFromFile(fname, mode):
    file = open(fname)
    marks = ""
    for line in file.readlines():
        if mode == 'full':
            exp = r"(<[^>]*>)([^<>]*?)(<\/[^>]*>)"
        elif mode == 'mark':
            exp = r"(<[^>\/]*>)"
        m = re.findall(exp, line)
        if m:
            for item in m:
                s = "".join(item)
                marks += s + "\n"
    marks = marks[:len(marks) - 1]
    file.close()
    return marks


def file_marker_Dict(path):
    import os
    from os.path import isfile, join
    file_marker_dict = {}
    for file in os.listdir(path):
        if isfile(join(path, file)):
            file_marker_dict[file] = getMarkedFromFile(join(path, file), "mark").split(sep='\n')
    return file_marker_dict


def marked_literal_Dict(marked):
    marked = marked.split(sep='\n')
    marks = {}
    for item in marked:
        m = re.search(r"(<[^>]*>)([^<>]*)", item)
        if m:
            s = m.group(0).split('>', )
            s[0] += '>'
            if s[0] not in marks:
                marks[s[0]] = [s[1]]
            else:
                marks[s[0]].append(s[1])
    #print(marks)
    return marks


def FreqDF(filemarks_dict: dict):
    freq_dict = {}
    for key in filemarks_dict.keys():
        freq_dict[key] = {}
        for item in np.unique(filemarks_dict[key]):
            if not item in freq_dict[key].keys():
                freq_dict[key][item] = filemarks_dict[key].count(item)
            else:
                freq_dict[key][item].append(filemarks_dict[key].count(item))
    #print(list(freq_dict.values())[0])
    df = pd.DataFrame(columns=list(freq_dict.values())[0].keys(), index=freq_dict.keys())
    for index in df.index:
        for column in df.columns:
            if column in freq_dict[index].keys():
                df.at[index, column] = freq_dict[index][column]
            else:
                df.at[index, column] = 0
    return df

if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    import os
    from os.path import isfile, join

    counter = 0

    data = file_marker_Dict('rvision-hackathon-2021-q1/marked/')
    df = FreqDF(data)
    df.to_excel("output_new.xlsx")
    #df = pd.DataFrame.from_dict(data=data, orient='index').transpose()

    """for file in os.listdir("rvision-hackathon-2021-q1/marked/"):
        if isfile(join("rvision-hackathon-2021-q1/marked/", file)):
            data = marked_literal_Dict(getMarkedFromFile(join("rvision-hackathon-2021-q1/marked/", file)))
            df = pd.concat([df, pd.DataFrame.from_dict(data=data, orient='index').transpose()], ignore_index=True)
            counter += 1"""
    # print(counter)
    print("--- %s seconds ---" % (time.time() - start_time))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

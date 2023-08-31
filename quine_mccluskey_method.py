# Copyright by SovesT 2023
import pandas as pd


def make_sdnf(f):
    temp = [[], [], [], [], [], [], []]
    start = []
    for i_ in range(len(f)):
        if f[i_] == "1":
            st = ""
            x = i_
            n = 32
            k = 0
            while n > 0:
                if x >= n:
                    x = x - n
                    st += "1"
                    k += 1
                else:
                    st += "0"
                n = n >> 1
            temp[k].append([st, True])
            start.append(st)
    return temp, start


def check_str(j, k):
    st = ""
    n = 0
    for q in range(6):
        if j[q] != k[q]:
            st += '*'
            n += 1
            if n > 1:
                return st, False
        if j[q] == k[q]:
            st += j[q]
    return st, True


def find_near(temp_):
    new_temp_ = [[], [], [], [], [], [], []]
    for i_ in range(6):
        for j in temp_[i_]:
            for k in temp_[i_ + 1]:
                st, check = check_str(j[0], k[0])
                if check:
                    j[1] = k[1] = False
                    if [st, True] not in new_temp_[i_]:
                        new_temp_[i_].append([st, True])
    return new_temp_, temp_


def beautiful_output(temp_, number):
    print("iteration " + str(number + 1))
    final = "Final: "
    final__ = []
    for i_ in range(len(temp_)):
        # st = "weight " + str(i_) + ": "
        st = ''
        for j_ in temp_[i_]:
            st += j_[0] + ' '
            if j_[1]:
                final += "\'" + j_[0] + "\' "
                final__.append(j_[0])
        print(st)
    print(final)
    print("-----------------------------------------------------------------------------------------------------------")
    return final__


def make_table(start, final):
    workbook = pd.DataFrame(index=final, columns=start)
    for i in workbook.columns:
        for j in workbook.index:
            check = True
            for k in range(6):
                if i[k] != j[k] and j[k] != '*':
                    check = False
            if check:
                workbook[i][j] = '+'
    workbook.to_excel('Quine.xlsx')


def add_to_table(temp_, table_, number):
    lst__ = []
    k = 0
    for i in temp_:
        for j in i:
            table_.iat[k, number] = j[0]
            k += 1
    return table_


def quine_method(f):
    final_final = list()
    table = pd.DataFrame(columns=[1, 2, 3, 4, 5], index=range(150))
    print("--- This is McCluskey method ---\n")
    new_temp, start_start = make_sdnf(f)
    for i in range(5):
        new_temp, old_temp = find_near(new_temp)
        table = add_to_table(old_temp, table, i)
        final_final += beautiful_output(old_temp, i)
    table.to_excel('Quine_1.xlsx')
    print("\n\n")
    print(final_final)
    make_table(start_start, final_final)

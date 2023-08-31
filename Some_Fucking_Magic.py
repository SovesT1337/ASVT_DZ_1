import pandas as pd


def update__(string2, string3):
    temp = ""
    while len(string2) < len(string3):
        string2 = '0' + string2
    for i in range(len(string2)):
        if string2[i] == '0':
            temp += "!x" + string3[i]
        if string2[i] == '1':
            temp += "x" + string3[i]
    return "K(" + temp + ")"


if __name__ == '__main__':
    workbook = pd.read_excel("To Filter.xlsx")
    c = 100
    for i in range(len(workbook.index)):
        st = ""
        for j in range(len(workbook.columns) - 1):
            test = workbook.iat[i, j + 1]
            if not pd.isnull(workbook.iat[i, j + 1]):
                if st != "":
                    st += " v " + update__(str(int(workbook.iat[i, j + 1])), workbook.columns[j + 1])
                if st == "":
                    st += update__(str(int(workbook.iat[i, j + 1])), workbook.columns[j + 1])
        print(str(i + 1) + ") " + st + " = 1")


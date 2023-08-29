# Copyright by SovesT 2023
import pandas as pd

cols = ['1', '2', '3', '4', '5', '6', '12', '13', '14', '15', '16', '23', '24', '25', '26', '34', '35',
        '36', '45', '46', '56', '123', '124', '125', '126', '134', '135', '136', '145', '146', '156',
        '234', '235', '236', '245', '246', '256', '345', '346', '356', '456', '1234', '1235', '1236', '1245',
        '1246', '1256', '1345', '1346', '1356', '1456', '2345', '2346', '2356', '2456', '3456', '12345', '12346',
        '12356', '12456', '13456', '23456', '123456']


def del_bad_cells(table, f):
    for st in range(63):
        a = set()
        for i in range(64):
            if f[i] == '0':
                table.iat[i, 63] = f[i]
                a.add(table.iat[i, st])
        for i in range(64):
            if table.iat[i, st] in a:
                table.iloc[i, st] = ''


def output(table):
    table.to_excel('Final.xlsx')


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


def make_boolean_expression(table):
    for i in range(64):
        if table.iat[i, 63] == '1':
            st = ""
            for j in range(63):
                if table.iat[i, j] != '' and st != '':
                    st += " v " + update__(table.iat[i, j], cols[j])
                if table.iat[i, j] != '' and st == '':
                    st += update__(table.iat[i, j], cols[j])
            st += " = 1"
            print(st)


def method_of_uncertain_coefficients(f):
    workbook = pd.read_excel('First_Table.xlsx').astype(str)
    del_bad_cells(workbook, f)
    output(workbook)
    make_boolean_expression(workbook)

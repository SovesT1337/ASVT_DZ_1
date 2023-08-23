import pandas as pd

# cols = {'1', '2', '3', '4', '5', '6', '12', '13', '14', '15', '16', '23', '24', '25', '26', '34', '35',
#         '36', '45', '46', '56', '123', '124', '125', '126', '134', '135', '136', '145', '146', '156',
#         '234', '235', '236', '245', '246', '256', '345', '346', '356', '456', '1234', '1235', '1236', '1245',
#         '1246', '1256', '1345', '1346', '1356', '1456', '2345', '2346', '2356', '2456', '3456', '12345', '12346',
#         '12356', '12456', '13456', '23456', '123456'}


def del_bad_cells(table):
    for st in range(63):
        a = set()
        for i in range(64):
            if table.iat[i, 63] == '0':
                a.add(table.iat[i, st])
        for i in range(64):
            if table.iat[i, st] in a:
                table.iloc[i, st] = ''


def output(table):
    table.to_excel('Final.xlsx')


if __name__ == '__main__':
    workbook = pd.read_excel('First_Table.xlsx').astype(str)
    del_bad_cells(workbook)
    output(workbook)

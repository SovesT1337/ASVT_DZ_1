# Copyright by SovesT 2023
import uncertain_coefficients as method2

F = "1110111111001100101010101011001111111011110011001010101000111011"


def make_sdnf():
    # F = f
    F.replace(" ", "")
    temp = []
    for i in range(len(F)):
        if F[i] == "1":
            st = ""
            x = i
            if x >= 32:
                x -= 32
                st += "1"
            else:
                st += "0"
            if x >= 16:
                x -= 16
                st += "1"
            else:
                st += "0"
            if x >= 8:
                x -= 8
                st += "1"
            else:
                st += "0"
            if x >= 4:
                x -= 4
                st += "1"
            else:
                st += "0"
            if x >= 2:
                x -= 2
                st += "1"
            else:
                st += "0"
            if x >= 1:
                x -= 1
                st += "1"
            else:
                st += "0"
            temp.append([st, True])
    return temp


def divide(temp_):
    new_temp_ = [[], [], [], [], [], [], []]
    for i_, b in temp_:
        n = 0
        for j in i_:
            if j == '1':
                n += 1
        new_temp_[n].append([i_, b])
    return new_temp_


def show(temp_):
    for i_ in temp_:
        print(i_)
    print("-----------------------------------------------------------------------------------------------------------")


def check_str(j, k):
    st = ""
    n = 0
    check = False
    for q in range(6):
        if j[q] != k[q]:
            st += '*'
            n += 1
        if j[q] == k[q]:
            st += j[q]
    if n <= 1:
        check = True
    return st, check


def find_near(temp_):
    new_temp_ = [[], [], [], [], [], [], []]
    for i_ in range(6):
        if len(temp_[i_]) != 0:
            for j in range(len(temp_[i_])):
                if len(temp_[i_ + 1]) != 0:
                    for k in range(len(temp_[i_ + 1])):
                        shit1 = temp_[i_][j]
                        shit2 = temp_[i_ + 1][k]
                        st, check = check_str(temp_[i_][j][0], temp_[i_ + 1][k][0])
                        if check:
                            temp_[i_][j][1] = False
                            temp_[i_ + 1][k][1] = False
                            new_temp_[i_].append([st, True])

    return new_temp_, temp_


def make_set(temp_):
    new_temp_ = [set(), set(), set(), set(), set(), set(), set()]
    final_ = [set(), set(), set(), set(), set(), set(), set()]
    for i_ in range(6):
        for j_, c in temp_[i_]:
            new_temp_[i_].add((j_, c))
    for i_ in range(6):
        for j_, c in temp_[i_]:
            if c:
                final_[i_].add((j_, c))
    return new_temp_, final_

if __name__ == '__main__':
    old_temp = make_sdnf()
    new_temp = divide(old_temp)
    for i in range(5):
        new_temp, old_temp = find_near(new_temp)
        shit, final = make_set(old_temp)
        # show(shit)
        show(final)
    # method2.method_of_uncertain_coefficients()

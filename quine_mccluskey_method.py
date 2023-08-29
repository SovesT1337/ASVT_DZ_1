# Copyright by SovesT 2023


def make_sdnf(f):
    temp = [[], [], [], [], [], [], []]
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
    return temp


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
    for i_ in range(len(temp_)):
        st = "weight " + str(i_) + ": "
        for j_ in temp_[i_]:
            st += j_[0] + ' '
            if j_[1]:
                final += j_[0] + ' '
        print(st)
    print(final)
    print("-----------------------------------------------------------------------------------------------------------")


def quine_method(f):
    new_temp = make_sdnf(f)
    for i in range(5):
        new_temp, old_temp = find_near(new_temp)
        beautiful_output(old_temp, i)
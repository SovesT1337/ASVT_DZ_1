#Copyright by SovesT 2023
import uncertain_coefficients as method2

# f = "1110 1111 1100 1100 1010 1010 1011 0011 1111 1011 1100 1100 1010 1010 0011 1011"
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
            temp.append(st)
    return temp


if __name__ == '__main__':
    print(make_sdnf())
    # method2.method_of_uncertain_coefficients()
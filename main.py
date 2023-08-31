# Copyright by SovesT 2023
import quine_mccluskey_method as first_method
import uncertain_coefficients as second_method

F = "1110111111001100101010101011001111111011110011001010101000111011"


if __name__ == '__main__':
    first_method.quine_method(F)
    second_method.method_of_uncertain_coefficients(F)

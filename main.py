import math


def toString(input_lst):
    lst = []
    converted_string = ""

    for list_element in input_lst:
        stored_bits = 0
        list_element_of_log10 = int(math.log10(list_element)) + 1

        for iteration_of_log10 in range(list_element_of_log10):
            bits = ((list_element % 10) * (2 ** iteration_of_log10))
            list_element = list_element // 10
            stored_bits += bits
        lst.append(stored_bits)

    for x in lst:
        converted_string += chr(x)
    return converted_string


# print(toString([1001000, 1100101, 1101100, 1101100, 1101111])) #  Outputs: "Hello"

try:
    print("---- Please input binary code ----")
    print("---- When finished typing, press 'enter' ----")
    input_list = []
    while True:
        inputas = int(input())
        if inputas != None:
            input_list.append(inputas)
        else:
            break

except:
    print(f"Binary input: {input_list}")
print(f"Converted input: {toString(input_list)}")
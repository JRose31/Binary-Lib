''' converting a number into binary:
    -Divide intial number by 2
    -If no remainder results from previous operation, binary = 0,
    else if remainder exists, round quotient down and binary = 1
    -Repeat operation on remaining rounded-down quotient
    -Operations complete when quotient(rounded down or not) == 0
'''

import math

def intToBinary(x):
    convert = x
    binary_holder = []
    while convert > 0:
        #dividing any number by 2 results in a remainder of 0 or 1
        binary_holder.append(convert % 2)
        #reassign rounded down quotient to our variable (convert)
        convert = math.floor(convert//2)
    #convert complete binary_holder list into string
    holder_string = "".join([str(num) for num in binary_holder])
    #our binary is backwards in the list (now a str) so we reverse it
    binary_complete = holder_string[::-1]

    return(binary_complete)


binary = intToBinary(13)
print(binary)

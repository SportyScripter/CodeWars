# Given an array of ones and zeroes, convert the equivalent binary value to an integer.

# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

def binary_array_to_number(arr):
    binary_string=""
    for i in arr:
        binary_string+= str(i)
    convert_number = int(binary_string,2)
    return convert_number

print(binary_array_to_number([0,1,0,1]))

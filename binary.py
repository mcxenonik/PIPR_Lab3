def binary_length(number):
    binary = bin(number)

    return len(binary) - 2 

print(binary_length(4))
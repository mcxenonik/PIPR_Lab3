def bin_length(number):
    binary = bin(number)

    return len(binary) - 2 

print(bin_length(4))
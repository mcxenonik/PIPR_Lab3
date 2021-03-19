def rectangle(width, height):
    old = ''.ljust(width, '#')
    new = ''.ljust(width, '#') + '\n'
    rect = ''.ljust(width * height, '#') 
    print(rect.replace(old, new, height - 1))

rectangle(6, 3)

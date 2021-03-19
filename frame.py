def frame_with_text(text, width):
    print(''.ljust(width, '*'))
    print('*{0}*'.format(''.center(width - 2)))
    print('*{0}*'.format(text.center(width - 2)))
    print('*{0}*'.format(''.center(width - 2)))
    print(''.ljust(width, '*'))

frame_with_text('HELLO', 11)

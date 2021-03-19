def format_row(left_cell, right_cell):
    return f" {left_cell[0]:{left_cell[1]}} | {right_cell[0]:{right_cell[1]}.3f} "

def optimal_column_width(top, values):
    return max(len(top), len(values[0]), len(values[1]), len(values[2]))

def table(a, b, c):
    optimal_left = optimal_column_width("Wymiary", ("Szerokość", "Wysokość", "Długość"))
    optimal_right = optimal_column_width("Wartość", (str(round(a, 3)), str(round(b, 3)), str(round(c, 3))))
    optimal = max(optimal_left, optimal_right)

    print(' {0} | {1} '.format('Wymiary'.ljust(optimal), 'Wartość'.rjust(optimal)))
    print(''.ljust(2 * optimal + 5, '-'))
    print(format_row(("Szerokość", optimal), (a, optimal)))
    print(format_row(("Wysokość", optimal), (b, optimal)))
    print(format_row(("Długość", optimal), (c, optimal)))
         
table(10121.23, 21243444444324.4567, 32343250.8)
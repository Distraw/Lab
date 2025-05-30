from sympy.strategies.core import switch

from csv_handler import CsvHandler

handler = CsvHandler('elixirs.csv')

while True:
    option = input("Menu"
                   "\n\t0) Print CSV"
                   "\n\t1) Average"
                   "\n\t2) Max"
                   "\n\t3) Min"
                   "\n\t4) Normalized"
                   "\n\t5) Tensor"
                   "\n\t6) Save tensor to CSV"
                   "\n\t7) Exit\n")

    if option == '0':
        handler.print()
    if option == '1':
        handler.print_average()
    elif option == '2':
        handler.print_max()
    elif option == '3':
        handler.print_min()
    elif option == '4':
        handler.print_normalized()
    elif option == '5':
        handler.print_tensor()
    elif option == '6':
        handler.save_to_csv('tensor.csv')
    elif option == '7':
        break
    else:
        print('Invalid option')
from Models.index import * 
import os

if __name__ == '__main__':
    print(os.getenv('CONNECTION_STRING'))

# from tabulate import tabulate
# table = [['col 1', 'col 2', 'col 3', 'col 4'], [1, 2222, 30, 500], [4, 55, 6777, 1]]
# print(tabulate(table))
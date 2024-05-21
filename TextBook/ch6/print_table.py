def print_table(table_data):
    col_widths = [0] * len(table_data)
    for i in range(len(table_data)):
        col_widths[i] = len(max(table_data[i], key=len))

    for i in range(len(table_data[0])):
        for j in range(len(table_data)):
            print(table_data[j][i].rjust(col_widths[j] + 1), end='')
        print()

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)


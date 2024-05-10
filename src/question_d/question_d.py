

def create_multiplication_table():
    table = []
    for i in range(1, 6):
        row = []
        for j in range(1, 11):
            row.append(i * j)
        table.append(row)
    return table


def display_multiplication_table(table):
    for row in table:
        for i in row:
            print("{:<4}".format(i), end=" ")
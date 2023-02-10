

# day_2_problem-6

def print_center_column(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    if num_cols % 2 == 1:
        center_col = num_cols // 2
        for row in matrix:
            print(row[center_col])
    else:
        center_col = num_cols // 2
        for row in matrix:
            print(row[center_col - 1], row[center_col])

matrix = [[1, 2, 3], [4,  5, 6], [7,  8, 9]]
print_center_column(matrix)
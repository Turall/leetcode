def search_matrix(matrix, target):
    for index in matrix:
       if target in index:
           return True
    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]

print(search_matrix(matrix, 3))


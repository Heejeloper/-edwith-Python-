def matrix_size_check(*matrix_variables):
    return (len(set(len(a) for a in matrix_variables))) == 1 & (len(set(len(a[0]) for a in matrix_variables))) == 1

def matrix_addition(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    return [[sum(t) for t in zip(*row)] for row in zip(*matrix_variables)]

# 행단위로 vector_addition 하자.



# 실행결과
matrix_x = [[2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]

print (matrix_addition(matrix_x, matrix_y)) # Expected value: [[4, 7], [4, 3]]
print (matrix_addition(matrix_x, matrix_y, matrix_z)) # Expected value: [[6, 11], [9, 6]]
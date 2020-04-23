def matrix_size_check(*matrix_variables):
    return (len(set(len(a) for a in matrix_variables))) == 1 & (len(set(len(a[0]) for a in matrix_variables))) == 1

def matrix_addition(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    return [[sum(t) for t in zip(*row)] for row in zip(*matrix_variables)]

# matrix간 뺄셈을 실행하여 결과를 반환함, 단 입력되는 matrix의 갯수와 크기는 일정하지 않음
def matrix_subtraction(*matrix_variables):
    """
    matrix_variable[0] - matrix_addition에 -1 곱해주고 나머지 다 합.
    """
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    print(matrix_variables[0][0][0]-matrix_variables[1:][0][0])
    print([matrix_variables[1:][0][0]])
    


    return None

# 실행결과
matrix_x = [[2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]

print (matrix_subtraction(matrix_x, matrix_y)) # Expected value: [[0, -3], [0, 1]]
print (matrix_subtraction(matrix_x, matrix_y, matrix_z)) # Expected value: [[-2, -7], [-5, -2]]
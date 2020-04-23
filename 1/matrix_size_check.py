#vector 간 덧셈 또는 뺄셈 연산을 할 때, 연산이 가능한 사이즈인지를 확인하여 가능 여부를 True 또는 False로 반환함
def vector_size_check(*vector_variables):
    return len(set(len(a) for a in vector_variables)) == 1

# #matrix 간 덧셈 또는 뺄셈 연산을 할 때, 연산이 가능한 사이즈인지를 확인하여 가능 여부를 True 또는 False로 반환함
# def matrix_size_check(*matrix_variables):
#     for mat in *matrix_variables:
#     print([len(mat), len(mat[0]) for mat in *matrix_variables])
#     return None

def matrix_size_check(*matrix_variables):
    return (len(set(len(a) for a in matrix_variables))) == 1 & (len(set(len(a[0]) for a in matrix_variables))) == 1

# 실행결과
matrix_x = [[2, 2], [2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]
matrix_w = [[2, 5], [1, 1], [2, 2]]

# [len(mat), len(mat[0])]을 set로 만들고 len(set()) == 1

print (matrix_size_check(matrix_x, matrix_y, matrix_z)) # Expected value: False
print (matrix_size_check(matrix_y, matrix_z)) # Expected value: True
print (matrix_size_check(matrix_x, matrix_w)) # Expected value: True
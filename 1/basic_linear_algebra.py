#vector 간 덧셈 또는 뺄셈 연산을 할 때, 연산이 가능한 사이즈인지를 확인하여 가능 여부를 True 또는 False로 반환함
def vector_size_check(*vector_variables):
    return len(set(len(a) for a in vector_variables)) == 1


#vector간 덧셈을 실행하여 결과를 반환함, 단 입력되는 vector의 갯수와 크기는 일정하지 않음
def vector_addition(*vector_variables):
    if vector_size_check(*vector_variables) == False: return "ArithmeticError"
    return ([sum(t) for t in zip(*vector_variables)])

#vector간 뺄셈을 실행하여 결과를 반환함, 단 입력되는 vector의 갯수와 크기는 일정하지 않음
def vector_subtraction(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        raise ArithmeticError
    return vector_addition(vector_variables[0],[(-1)*sum(t) for t in zip(*vector_variables[1:])])

#하나의 scalar 값을 vector에 곱함, 단 입력되는 vector의 크기는 일정하지 않음
def scalar_vector_product(alpha, vector_variable):
    return [alpha*x for x in vector_variable]

#matrix 간 덧셈 또는 뺄셈 연산을 할 때, 연산이 가능한 사이즈인지를 확인하여 가능 여부를 True 또는 False로 반환함
def matrix_size_check(*matrix_variables):
    return (len(set(len(a) for a in matrix_variables))) == 1 & (len(set(len(a[0]) for a in matrix_variables))) == 1

# # 실행결과
# matrix_x = [[2, 2], [2, 2], [2, 2]]
# matrix_y = [[2, 5], [2, 1]]
# matrix_z = [[2, 4], [5, 3]]
# matrix_w = [[2, 5], [1, 1], [2, 2]]

# print (matrix_size_check(matrix_x, matrix_y, matrix_z)) # Expected value: False
# print (matrix_size_check(matrix_y, matrix_z)) # Expected value: True
# print (matrix_size_check(matrix_x, matrix_w)) # Expected value: True

# 비교가 되는 n개의 matrix가 서로 동치인지 확인하여 True 또는 False를 반환
from functools import reduce
def is_matrix_equal1(*matrix_variables):
    return reduce(lambda x,y: x==y, matrix_variables)
# # 실행결과
# matrix_x = [[2, 2], [2, 2]]
# matrix_y = [[2, 5], [2, 1]]

# print (is_matrix_equal(matrix_x, matrix_y, matrix_y, matrix_y)) # Expected value: False
# print (is_matrix_equal(matrix_x, matrix_x)) # Expected value: True

#matrix간 덧셈을 실행하여 결과를 반환함, 단 입력되는 matrix의 갯수와 크기는 일정하지 않음
def matrix_addition(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    return [[sum(t) for t in zip(*row)] for row in zip(*matrix_variables)]

# # 실행결과
# matrix_x = [[2, 2], [2, 2]]
# matrix_y = [[2, 5], [2, 1]]
# matrix_z = [[2, 4], [5, 3]]

# print (matrix_addition(matrix_x, matrix_y)) # Expected value: [[4, 7], [4, 3]]
# print (matrix_addition(matrix_x, matrix_y, matrix_z)) # Expected value: [[6, 11], [9, 6]]

#matrix간 뺄셈을 실행하여 결과를 반환함, 단 입력되는 matrix의 갯수와 크기는 일정하지 않음
def matrix_subtraction(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    return [[t[0]*2 - sum(t) for t in zip(*row)] for row in zip(*matrix_variables)]

# 실행결과
matrix_x = [[2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]

print (matrix_subtraction(matrix_x, matrix_y)) # Expected value: [[0, -3], [0, 1]]
print (matrix_subtraction(matrix_x, matrix_y, matrix_z)) # Expected value: [[-2, -7], [-5, -2]]

#matrix의 전치행렬을 구하여 결과를 반환함, 단 입력되는 matrix의 크기는 일정하지 않음
def matrix_transpose(matrix_variable):
    return list(zip(*matrix_variable))

# # 실행결과
# matrix_w = [[2, 5], [1, 1], [2, 2]]
# matrix_transpose(matrix_w)

#하나의 scalar 값을 matrix에 곱함, 단 입력되는 matrix의 크기는 일정하지 않음
def scalar_matrix_product(alpha, matrix_variable):
    return [[alpha*x for x in row] for row in matrix_variable]

# # 실행결과
# matrix_x = [[2, 2], [2, 2], [2, 2]]
# matrix_y = [[2, 5], [2, 1]]
# matrix_z = [[2, 4], [5, 3]]
# matrix_w = [[2, 5], [1, 1], [2, 2]]

# print(scalar_matrix_product(3, matrix_x)) #Expected value: [[6, 6], [6, 6], [6, 6]]
# print(scalar_matrix_product(2, matrix_y)) #Expected value: [[4, 10], [4, 2]]
# print(scalar_matrix_product(4, matrix_z)) #Expected value: [[8, 16], [20, 12]]
# print(scalar_matrix_product(3, matrix_w)) #Expected value: [[6, 15], [3, 3], [6, 6]]

#두 개의 matrix가 입력 되었을 경우, 두 matrix의 곱셈 연산의 가능 여부를 True 또는 False로 반환함
def is_product_availability_matrix(matrix_a, matrix_b):
    try:
        return len(matrix_b) == len(matrix_a[0])
    except:
        return None

# # 실행결과
# matrix_x= [[2, 5], [1, 1]]
# matrix_y = [[1, 1, 2], [2, 1, 1]]
# matrix_z = [[2, 4], [5, 3], [1, 3]]

# print(is_product_availability_matrix(matrix_y, matrix_z)) # Expected value: True
# print(is_product_availability_matrix(matrix_z, matrix_x)) # Expected value: True
# print(is_product_availability_matrix(matrix_z, matrix_w)) # Expected value: False //matrix_w가없습니다
# print(is_product_availability_matrix(matrix_x, matrix_x)) # Expected value: True

#곱셈 연산이 가능한 두 개의 matrix의 곱셈을 실행하여 반환함
def matrix_product(matrix_a, matrix_b):
    if is_product_availability_matrix(matrix_a, matrix_b) == False:
        raise ArithmeticError
    return None

# # 실행결과
# matrix_x= [[2, 5], [1, 1]]
# matrix_y = [[1, 1, 2], [2, 1, 1]]
# matrix_z = [[2, 4], [5, 3], [1, 3]]

# print(matrix_product(matrix_y, matrix_z)) # Expected value: [[9, 13], [10, 14]]
# print(matrix_product(matrix_z, matrix_x)) # Expected value: [[8, 14], [13, 28], [5, 8]]
# print(matrix_product(matrix_x, matrix_x)) # Expected value: [[9, 15], [3, 6]]
# print(matrix_product(matrix_z, matrix_w)) # Expected value: False
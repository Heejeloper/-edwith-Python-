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

print(vector_subtraction([1, 3], [2, 4])) # Expected value: [-1, -1]
print(vector_subtraction([1, 5], [10, 4], [4, 7])) # Expected value: [-13, -6]
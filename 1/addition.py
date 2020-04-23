# # #vector간 덧셈을 실행하여 결과를 반환함, 단 입력되는 vector의 갯수와 크기는 일정하지 않음
def vector_size_check(*vector_variables):
    return len(set(len(a) for a in vector_variables)) == 1

def vector_addition(*vector_variables):
    if vector_size_check(*vector_variables) == False: return "ArithmeticError"
    return ([sum(t) for t in zip(*vector_variables)])

# def vector_addition(*vector_variables):
#     if vector_size_check(*vector_variables) == False:
#         raise ArithmeticError
#     return [sum(x) for x in zip(*vector_variables)]


print(vector_addition([1, 3], [2, 4], [6, 7])) # Expected value: [9, 14]
print(vector_addition([1, 5], [10, 4], [4, 7])) # Expected value: [15, 16]
print(vector_addition([1, 3, 4], [4], [6,7])) # Expected value: ArithmeticError
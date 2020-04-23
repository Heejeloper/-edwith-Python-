# # vector 간 덧셈 또는 뺄셈 연산을 할 때, 연산이 가능한 사이즈인지를 확인하여 가능 여부를 True 또는 False로 반환함
# def vector_size_check(*vector_variables):
#     a = set()
#     for i in vector_variables:
#         a.add(len(i))
#     if len(a) == 1:
#         return True
#     return False

def vector_size_check(*vector_variables):
    return len(set(len(a) for a in vector_variables)) == 1


# 구조를 생각해보자.
# 먼저, vector_variables를 unpacking해서 받는다.
# 그리고 vector_variables 각각의 len을 받아서 리스트를 만든다. 혹은 set을 만든다.
# 그 len들의 값들간 일치여부를 판단한다...

print(vector_size_check([1,2,3], [2,3,4], [5,6,7])) # Expected value: True
print(vector_size_check([1, 3], [2,4], [6,7])) # Expected value: True
print(vector_size_check([1, 3, 4], [4], [6,7])) # Expected value: False
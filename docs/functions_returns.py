## 나오는 값 처리
# first = 5
# second = 4
# sum = first + second
def add() :
    first = 5
    second = 4
    sum = first + second
    # return 0  0으로 보냄
    return sum # 상수대신 변수 사용 (파이썬에 한정적), 값을 return한다

# num_sum = 0
num_sum = add()

print("add() return 결과 : {}".format(num_sum))

# num_first = 4
# num_second = 5
# # 곱셈 연산
# num_first * num_second

# 두 수를 곱해서 결과 return
def multiply() : 
    num_first = 4
    num_second = 5
    # 곱셈 연산
    result = num_first * num_second      # 내용 넣기
    return result

num_multiply = multiply()
print("num_multiply return value : {}".format(num_multiply))

# list_fruits = ["melon","apple", "banana", "cherry"]
## index로 값 가져오기
# list_fruits[0]  # 단일 변수로 여김 1차원(행)

def return_list() : 
  list_fruits = ["melon","apple", "banana", "cherry"]      # 내용 넣기
  return list_fruits

print("return_list() return value : {}".format(return_list()))
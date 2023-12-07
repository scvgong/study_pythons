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

# list 중에 index로 값 return
def return_listbyindex() : 
  list_fruits = ["melon","apple", "banana", "cherry"]
  # index로 값 가져오기
  return list_fruits[0]  # 단일 변수로 여김 1차원(행)

print("return_listbyindex() return result : {}".format(return_listbyindex()))

# my_score = 79

# if my_score >= 90 :     # 90점 이상 : A
#     print("{}은 90점 이상으로 A학점".format(my_score))
# elif my_score > 80 :    # 80점 초과 : B
#     print("{}은 80점 초과로 B학점".format(my_score))
# else :                  # 나머지는 : F
#     print("{}은 80점 이하으로 F학점".format(my_score))

# 목표 : 반복적인 print 작업을 줄이기 위한 functions 만들기
def return_grade() : 
  my_score = 79
  my_grade = ''
  if my_score >= 90 :     # 90점 이상 : A
    my_grade = 'A'
    pass
  elif my_score > 80 :    # 80점 초과 : B
    my_grade = 'B'
    pass
  else :                  # 나머지는 : F
    my_grade = 'F'
    pass
  # return_listbyindex()
  return my_grade

str_grade = return_grade()
print("당신의 학점 : {}".format(str_grade))

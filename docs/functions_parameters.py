# function에 들어가는 값들

def add(first, second) :
    sum = first + second
    # return 0  0으로 보냄
    return sum # 상수대신 변수 사용 (파이썬에 한정적), 값을 return한다

if __name__ == "__main__":
  # num_sum = 0
  num_sum = add(5,4)  # parameters로 상수 사용
  print("add() return 결과 : {}".format(num_sum))

  third = 6
  fourth = 10
  num_sum = add(third,fourth)     # function 부르면 값들만 전달됨
  print("add() return 결과 : {}".format(num_sum))

# 내 점수를 넣으면 학점이 나오는 function
def return_grade(my_score) :    # 자신을 불렀을때 값들 들어감(순서 매칭)
  my_grade = ''
  if my_score >= 90 :     # 90점 이상 : A
    my_grade = 'A'
    pass
  elif my_score > 80 :    # 80점 초과 : B
    my_grade = 'B'
    pass
  elif my_score > 70 :    # 70점 초과 : C
    my_grade = 'C'
    pass
  elif my_score > 60 :    # 60점 초과 : D
    my_grade = 'D'
    pass
  else :                  # 나머지는 : F
    my_grade = 'F'
    pass
  # return_listbyindex()
  return my_grade

if __name__ == "__main__":
  # str_grade = return_grade(99)  # 호출 시 값들이 넘어감(순서 매칭)
  # print("당신의 학점 : {}".format(str_grade))
  my_score = 88
  str_grade = return_grade(my_score)  
  print("당신의 학점 : {}".format(str_grade))

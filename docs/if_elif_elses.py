# 기본 if - elif - else 구문 :과 tab의 조화
if True :
    pass
elif True :
    pass
else :
    pass

# 문자 비교
str_name = "myeongyun gong"

# 질문 형식(condition) = 변수 + 부등호 + 기준값
# 문자에 대한 긍정으로 질문
if str_name == "myeongyun gong" :
    pass
    print("name is {}.".format(str_name))

# 문자에 대한 부정으로 질문
if str_name != "myeongyun gong" :
    pass
    print("name is not {}.".format(str_name))

# if - else
# num_first >= 4 -> True : 큼, False : 작음

num_first = 5

# if num_first >= 4 : # 무조건 둘 중 하나 표현
if num_first >= 6 : # 무조건 둘 중 하나 표현
    pass        # condition이 True 이면 실행
    print("{}는 4보다 크다".format(num_first))
else :          
    pass        # condition이 False 이면 실행
    print("{}는 4보다 작다".format(num_first))

# if - elif - else
# 점수에 따른 표시
# 90점 이상 : A, 80점 초과 : B, 나머지는 : F

# my_score = 90
my_score = 79

if my_score >= 90 :     # 90점 이상 : A
    pass
    print("{}은 90점 이상으로 A학점".format(my_score))
elif my_score > 80 :    # 80점 초과 : B
    pass
    print("{}은 80점 초과로 B학점".format(my_score))
else :                  # 나머지는 : F
    pass
    print("{}은 80점 이하으로 F학점".format(my_score))

# 부등호 사용 시 결과는 True or False(boolean)
# 논리 연산자(True or False 대한 결과값) 
first = 200
second = 33
third = 500

# condition 사용 이전에 각각 결과 확인 후 사용하는게 좋다
first > second
# True
third > first
# True
(first > second) and (third > first)
# True

if (first > second) and (third > first) :
    print("Both conditions are True")

if not (first < second):
    print("not (first < second)")
# False

# (first > second) or (third > first) and (first > second) and (third > first)

pass

print("End Program")
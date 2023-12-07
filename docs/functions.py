# 기본 function 형식 - 특징 : 기다림, 불러올때 가능한다.
def function() : 
  pass
  return 0
#################

#그냥 연습
def my_function():
  print("Hello from a function")

my_function()
pass


#문항 1과 답항을 출력하는 function
def print_question_and_answer():
    str_question = "1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?"
    print(str_question)
    answer = "A. Windows B. macOS C. Linux D. Chrome OS E. 기타"
    print(answer)
    return 0

print_question_and_answer()
print_question_and_answer()
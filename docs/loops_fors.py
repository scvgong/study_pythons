# for 기본 문형
for x in []:
    pass

# 얼마만큼 반복할지에 대한 값들을 알려줌
numberic = 0
numberics = [0, 1, 2, 3, 4]      # 5개수 값으로 이루어진 리스트
for number in numberics :
    pass
    print(number)

# 문자 3개 값들로 이루어진 리스트
for x in ["apple", "melon", "banana", "cherry"]:  # x는 변수, 처음 시작하는 값 순차적으로 대입, 반복 대상 리스트 직접 넣기
    pass
    print("fruit name : {}!".format(x))

list_fruits = ["apple", "banana", "cherry"]
for str_fruit in list_fruits:  # x는 변수, 처음 시작하는 값 순차적으로 대입, 반복 대상 리스트 직접 넣기
    pass
    print("fruit name : {}!".format(str_fruit))

numberics = [0, 1, 2, 3, 4]      # 5개수 값으로 이루어진 리스트
for number in numberics :
    pass
    #print("Number : {}".format(number))
    print("Number : {}".format(number+2))


## 설문 답변 받기
# 1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?                index 0
# A. Windows B. macOS C. Linux D. Chrome OS E. 기타    index 1
# 당신의 답변 : A 
# 2. 주로 사용하는 프로그래밍 언어는 무엇인가요?                index 2
# A. Python B. Java C. JavaScript D. C++ E. 기타       index 3
# 당신의 답변 : D
# 3. 개발자에게 인기 있는 프로그래밍 언어는 무엇인가요?           index 4
# A. Python B. Java C. JavaScript D. C++ E. 기타       index 5
# 당신의 답변 : E 

list_polls = ["1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?"
             ,"A. Windows B. macOS C. Linux D. Chrome OS E. 기타"
             ,"2. 주로 사용하는 프로그래밍 언어는 무엇인가요?"
             ,"A. Python B. Java C. JavaScript D. C++ E. 기타"
             ,"3. 개발자에게 인기 있는 프로그래밍 언어는 무엇인가요?"
             ,"A. Python B. Java C. JavaScript D. C++ E. 기타"
             ]

list_statistics = [0, 0, 0, 0, 0]  # 답항만큼 0을 넣어줌, 답항을 번호로 바꿨을때에 대한 list, 선호답항
for num_count in [0,2,4]:
    # str_content = list_polls[num_count]
    # print("{}".format(str_content))
    str_question = list_polls[num_count] # 질문에 대한 list 대입
    print("{}".format(str_question))    # 질문 출력

    str_anwser = list_polls[num_count+1] # 답변에 대한 list 대입
    print("{}".format(str_anwser))      # 답변 출력
    
    str_question_result = input("당신의 답변(A~E를 순서 맞게 번호로 입력) : ") # 답변 입력 받아서(숫자로) str_question_result로 대입
    num_question_result = int(str_question_result)  # 문자를 숫자로 변환시켜서 num_question_result로 대입
    index = num_question_result - 1 # index 위치값 적용을 위한 연산, index는 0부터 시작하기 때문에, num_question_result 결과값에 -1 연산 결과 index에 대입
    list_statistics[index] = list_statistics[index] + 1 # index list 최종 위치 잡아줌

    print("------------------------------------------------------------")
    pass

print("선호 답항 : {}".format(list_statistics))
print("End program")
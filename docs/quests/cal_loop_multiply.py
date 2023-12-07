# 사용자 입력 반복 곱셈 계산기
# 'q' 입력시 종료
# function 2개 사용

# 필요한 function = 연산 function, 종료 functions
# 변수 : 입력받을 2개의 숫자, 연산결과, q입력 변수, q 입력시 종료

# 반복 계산 함수
def return_cal():    
    while True :
        cal_first,cal_second = input().split()

        result = int(cal_first) * int(cal_second)
        print("{} * {} = {}".format(cal_first, cal_second, result))

    return True



# 버튼 입력시 종료 코드
push_str = input()

if push_str != 'q':
    print(return_cal())
elif push_str == 'q':
    pass
else :
    exit()

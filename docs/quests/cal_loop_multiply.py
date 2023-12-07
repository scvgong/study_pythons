# 사용자 입력 반복 곱셈 계산기
# 'q' 입력시 종료
# function 2개 사용

# 필요한 function = 연산/조건 function, 메인 functions
# 변수 : 입력받을 2개의 숫자
# 조건 : 문자/숫자 유무 판단, 'q' 입력시 종료, 숫자일시 계산


def in_cal():
    while True:
        cal_num1 = input("첫번째 숫자 입력 : ")
        cal_num2 = input("두번째 숫자 입력 : ")
        
        if cal_num1 == "q" or cal_num2 == "q": # 특정코드 'q' 입력시 종료
            print("프로그램을 종료합니다")
            break
        elif cal_num1.isalpha() or cal_num2.isalpha() : # 문자일시 재입력
            print("재입력 바랍니다.")
            continue
        elif cal_num1.isdigit() and cal_num2.isdigit() : # 숫자일시 계산
            result = int(cal_num1) * int(cal_num2)
            print("{} * {} = {}".format(cal_num1,cal_num2,result))
            # pass
    return 

def main():
    print("계산기")
    print("계산 종료하려면 q 버튼 누르기")
    result = in_cal()
    return

main()
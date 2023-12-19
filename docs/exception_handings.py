# 기본구문 
try:
    pass    # 업무코드, 여러줄(코드) 삽입 가능
except:
    pass    # 업무코드 문제 발생 시 대처코드,여러줄(코드) 삽입 가능
finally:
    pass    # try나 except이 끝난 후 무조건 실행 코드
# pure python with 계산기

# 숫자
# num_first = '4'
num_first = 4
num_second = 5
# 곱셈 연산


try: # 시도합니다
    result = num_first / num_second # 코드가 num_first가 문자 '4'일경우 / 숫자 4일 경우
    pass    # 업무코드, 여러줄(코드) 삽입 가능
except:                             # 에러가 발생안하면 except은 패스한다, 문제 발생시 들어가는 부분 
    result = int(num_first) / int(num_second)
    pass    # 업무코드 문제 발생 시 대처코드,여러줄(코드) 삽입 가능
finally:
    pass 

print("{} = {} * {}".format(result,num_first,num_second))

pass

# function in try exception
def multiply_withexception(num_first,num_second) : 
    try: # 시도합니다
        result = num_first / num_second # 코드가 num_first가 문자 '4'일경우 / 숫자 4일 경우
        pass    # 업무코드, 여러줄(코드) 삽입 가능
    except:                             # 에러가 발생안하면 except은 패스한다, 문제 발생시 들어가는 부분 
        result = int(num_first) / int(num_second)
        pass    # 업무코드 문제 발생 시 대처코드,여러줄(코드) 삽입 가능
    finally:
        pass 
    pass      # 내용 넣기
    return result
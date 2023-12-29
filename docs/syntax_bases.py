# 코드 기본 형식
## import 시 주로 사용하는 방식

from classes_formats import Person, Arithmetics, Class_name

class Class_name :
    def __init__(self) : # 모든 class에 기본적으로 제공하는 function / class 생성자
        pass

    def function_name(self): # self 키워드 필요 (class 소속 확인용)
        try:
            pass    # 업무코드, 여러줄(코드) 삽입 가능
        except:
            pass    # 업무코드 문제 발생 시 대처코드,여러줄(코드) 삽입 가능
        finally:
            pass    # try나 except이 끝난 후 무조건 실행 코드
        return 0

# 기본 function 형식 - 특징 : 기다림, 불러올때 가능한다.
def function_name() : 
    try:
        pass    # 업무코드, 여러줄(코드) 삽입 가능
    except:
        pass    # 업무코드 문제 발생 시 대처코드,여러줄(코드) 삽입 가능
    finally:
        pass    # try나 except이 끝난 후 무조건 실행 코드
    return 0

if __name__ == "__main__":
    try:
        pass    # 업무코드, 여러줄(코드) 삽입 가능
    except:
        pass    # 업무코드 문제 발생 시 대처코드,여러줄(코드) 삽입 가능
    finally:
        pass    # try나 except이 끝난 후 무조건 실행 코드


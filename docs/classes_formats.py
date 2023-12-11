# class 사용 순서
# 1. import : 같은 파일에 있을 경우 생략
# 2. class instance : 생성자 호출
# 3. call function : 원하는 기능 호출

# class 기본 구조(basic format)
class Class_name :
    def __init__(self) : # 모든 class에 기본적으로 제공하는 function / class 생성자
        pass

    def function_name(self): # self 키워드 필요 (class 소속 확인용)
        pass
        return 0

class Person :
    def add_age(self):
        pass
        print("45세")
        return 0 
    
# 1. import : 같은 파일에 있을 경우 생략
# 2. class instance
person = Person() # 변수에 class가 담김
# 3. call function
person.add_age()

# 사칙연산 되는 class 작성
# 덧셈, 뺄셈
class Arithmetics :
    def __init__(self) : # 생성자(class가 갖고 있는 자원), 모든 class에 기본적으로 제공하는 function
        pass

    def add(self, first, second) :
        sum = first + second
        # return 0  0으로 보냄
        return sum # 상수대신 변수 사용 (파이썬에 한정적), 값을 return한다

    def minus(self, first, second) : 
        result = first - second
        return result

# 1. import : 같은 파일에 있을 경우 생략
# 2. class instance
arithmetics = Arithmetics()
# 3. call function
print(arithmetics.add(5,6))
pass
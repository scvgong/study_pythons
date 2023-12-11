# class 사용 순서
# 1. import : 같은 파일에 있을 경우 생략
# 2. class instance
# 3. call function

# class 기본 구조(basic format)
class Class_name :
    def function_name(self):
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
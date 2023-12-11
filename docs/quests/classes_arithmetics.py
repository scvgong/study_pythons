class Arithmetic:
    def __init__(self) : 
        pass

    def sum(self, first, second): 
        result = first + second
        pass
        return result
    
    def sub(self, first, second):
        result = first - second
        pass
        return result

    def multi(self, first, second):
        result = first * second
        pass
        return result

    def div(self, first, second):
        result = first / second
        pass
        return result

a = int(input("첫 번째 숫자 : "))
b = int(input("두 번째 숫자 : "))
arithmetics = Arithmetic()
print("덧셈 : ",arithmetics.sum(a,b))
print("뺄셈 : ",arithmetics.sub(a,b))
print("곱셈 : ",arithmetics.multi(a,b))
print("나눗셈 : ",arithmetics.div(a,b))

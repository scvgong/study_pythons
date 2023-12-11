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
    
arithmetics = Arithmetic()
print("덧셈 : ",arithmetics.sum(7,6))
print("뺄셈 : ",arithmetics.sub(7,6))
print("곱셈 : ",arithmetics.multi(7,6))
print("나눗셈 : ",arithmetics.div(7,6))

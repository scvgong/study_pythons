# condition이 True 동안 반복 동작
# while True :
#     pass

num_virtual = 0
# while문 정지 case 1 with break문 사용
while True: 
    pass 
    num_virtual = num_virtual + 1
    print("{} = num_virtual + 1".format(num_virtual))
    if num_virtual >= 5 :
        pass
        break
    pass

# while문 정지 case 2 without break문 사용
num_virtual = 0
while num_virtual < 5 : 
    pass 
    num_virtual = num_virtual + 1
    print("{} = num_virtual + 1".format(num_virtual))
    pass

print("End Program")
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

print("End Program!")
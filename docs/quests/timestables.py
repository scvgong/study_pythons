# 단수 입력 받아 연산, 구구단
## - 구구단 5단 단계별 표시(while 문 사용)
# 예. 5 * 1= 5  5 * 2 = 10 ... 5 * 9 = 45
## - option) 단수 입력 받아 연산

# 구구단 5단 연산
gugu = 5
num = 0

while num < 9:
    pass
    num = num + 1
    result = int(gugu) * int(num)
    print("{} * {} = {}".format(gugu,num,result))
    pass
print("End Program")

# 단수 입력 받아 연산ß
gugu = int(input("구구단 숫자를 입력하세요 : "))
num = 0

while num < 9:
    pass
    num = num + 1
    result = int(gugu) * int(num)
    print("{} * {} = {}".format(gugu,num,result))
    pass

print("End Program")
# 단수 입력 받아 연산, 구구단
## - 구구단 5단 단계별 표시(for 문 사용)
# 예. 5 * 1= 5  5 * 2 = 10 ... 5 * 9 = 45
## - option) 단수 입력 받아 연산

# 5단
gugu = 5
num = [1,2,3,4,5,6,7,8,9]

for gugu_num in num:
    pass
    print("5단 : {} * {} = {}".format(gugu,gugu_num,(gugu * gugu_num)))


# 입력받아서 하기
gugu = int(input("구구단 숫자를 입력하세요 : "))
num = num = [1,2,3,4,5,6,7,8,9]

for gugu_num in num:
    pass
    print("{} * {} = {}".format(gugu,gugu_num,(gugu * gugu_num)))
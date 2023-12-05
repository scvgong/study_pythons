# 가로 * 세로 * 높이 = 직육면체
# input = 가로 세로 높이
# output = 가로(4)m * 세로(1)m * 높이(1)m = 직육면체(4)m^3


# 입력받을 변수 지정
# width = input()
# length = input()
# height = input()

# 입력받을 변수 지정 -> 한줄 요약
width, length, height = input().split()


# type 변환
w = int(width)
l = int(length)
h = int(height)

result = w * l * h

print("가로{}m * 세로{}m * 높이{}m = 직육면체{}m^3".format(w,l,h,result))
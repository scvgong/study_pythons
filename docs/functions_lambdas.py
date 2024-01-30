# 압축된 for문 적용
numberics = [0, 1, 2, 3, 4]      # 5개수 값으로 이루어진 리스트
numberics_list = []     # numberics + 2 ==> [2,3,4,5,6]
for number in numberics :
    result = number + 2
    numberics_list.append(result)
    pass
print(numberics_list)

print([number+2 for number in numberics])
pass
    
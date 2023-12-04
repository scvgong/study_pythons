one = "1"
two = "0"
three = "2"
four = "0"
five = "3"

# 1,0,2,0,3
print("{}, {}, {}, {}, {}.".format(one, two, three, four, five))

one, two = two, one # 1, 0 -> 0, 1 로 변환, 0,1,2,0,3
print("{}, {}, {}, {}, {}.".format(one, two, three, four, five))

two, three = three, two # 1, 2 -> 2, 1 로 변환 0,2,1,0,3
print("{}, {}, {}, {}, {}.".format(one, two, three, four, five))

three, four = four , three # 1, 0 -> 0, 1 로 변환 0,2,0,1,3
print("{}, {}, {}, {}, {}.".format(one, two, three, four, five))

five, four = four, five # 1, 3 -> 3, 1 로 변환 0,2,0,3,1
print("{}, {}, {}, {}, {}.".format(one, two, three, four, five))

three, four = four, three # 3, 0 -> 0, 3로 변환 0,2,3,0,1
print("{}, {}, {}, {}, {}.".format(one, two, three, four, five))

two, three = three, two # 3, 2 -> 2, 3 로 변환 0,3,2,0,1
print("{}, {}, {}, {}, {}.".format(one, two, three, four, five))

one, two = two, one # 0, 3 -> 3, 0 로 변환 3,0,2,0,1
print("{}, {}, {}, {}, {}.".format(one, two, three, four, five))
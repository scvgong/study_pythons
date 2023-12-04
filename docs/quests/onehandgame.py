one = "1"
two = "0"
three = "2"
four = "0"
five = "3"
print("{}, {}, {}, {}, {}.".format(one, two, three, four, five))

one, two = two, one # 1, 0 -> 0, 1 로 변환
print("{}, {}, {}, {}, {}.".format(one, two, three, four, five))

two, four = four, two # 0, 1 -> 1, 0 로 변환
print("{}, {}, {}, {}, {}.".format(one, two, three, four, five))

two, three = three, two # 2, 0 -> 2, 0 로 변환
print("{}, {}, {}, {}, {}.".format(one, two, three, four, five))

five, four = four, five
print("{}, {}, {}, {}, {}.".format(one, two, three, four, five))

three, four = four, three
print("{}, {}, {}, {}, {}.".format(one, two, three, four, five))

two, three = three, two
print("{}, {}, {}, {}, {}.".format(one, two, three, four, five))

one, two = two, one
print("{}, {}, {}, {}, {}.".format(one, two, three, four, five))
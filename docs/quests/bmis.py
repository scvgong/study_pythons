# quest
# input(두 값은 정수) : 몸무게, 키
## BMI = 몸무게(kg) / 키(m)^2
## BMI 분류
# 18 미만 : 저체중
# 18-22 : 정상
# 23-24 : 과체중
# 25 이상 : 비만

# 변수
key, weight = input().split()
bmi = int(weight) / int(key) ** 2


if bmi >= 25  :
    pass
    print("{}은 비만입니다.".format(bmi))
elif bmi >= 23 :
    pass
    print("{}은 정상입니다.".format(bmi))
elif bmi >= 18 :
    pass
    print("{}은 과체중입니다.".format(bmi))
else :
    pass
    print("{}은 저체중입니다.".format(bmi))
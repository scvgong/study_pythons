#초기화 방법
dict_initial = {} # 초기화 세팅
dict_initial = dict()

list_car = ['Ford','Mustang',1964]

# key(str) : value(여러 변수 종류 가능)
dict_carinfor = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "item": []
}

model = dict_carinfor["model"]
print("dict_carinfor 있는 model name : {}".format(model))

# key로 인한 값 변경
dict_carinfor['year'] = 1970
# 새로운 key와 값 정의
dict_carinfor['color'] = "red"
dict_carinfor['color'] = ["red","yellow","brown"]

pass
#function만 사용해 적 캐릭터 만들기

#first 적 캐릭터
name_first = "first"
health_first = 120
damage_first = 0

def attack(health,damage):
    health = health - damage
    return health

damage_first = attack(health_first, 5)

#second 적 캐릭터
name_second = "second"
health_second = 200
damage_second = 0

damage_second = attack(health_second,10)

# function만 사용 시 제한 극복 -> class
class Enemy :
    def __init__(self, name, health) : # 모든 class에 기본적으로 제공하는 function / class 생성자
        self.name = name    # 외부 변수 name 값이 내부 변수 self.name에 할당
        self.health = health
        self.damage = 0
        pass

    def attack(self,damage):
        self.health = self.health - damage
        return self.health

    def function_name(self): # self 키워드 필요 (class 소속 확인용)
        pass
        return 0
    
    
# first_enemy = Enemy() # 자신의 자원(function과 var) 확인
first_enemy = Enemy('first',150)
secondß_enemy = Enemy('second',300)
pass
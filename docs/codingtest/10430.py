# https://www.acmicpc.net/problem/10430
# 문제
## (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
## (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
## 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

# 입력
## 첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)

# 출력
## 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.

#입력예제 : 5 8 4 출력예제 : 1 1 0 0

a, b, c = input().split()
num1 = int(a)
num2 = int(b)
num3 = int(c)

print(((num1+num2)%num3))
print(((num1%num3)+(num2%num3))%num3)
print((num1*num2)%num3)
print(((num1%num3)*(num2%num3))%num3)


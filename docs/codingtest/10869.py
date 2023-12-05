# https://www.acmicpc.net/problem/10869
# 문제
## 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 
# 입력
## 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)

# 출력
## 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

a,b = input().split()
num1 = int(a)
num2 = int(b)
c = num1 + num2
d = num1 - num2
e = num1 * num2
f = num1 / num2
g = num1 % num2


print(c)
print(d)
print(e)
print(round(f))
print(g)

# https://www.acmicpc.net/problem/11382
# 문제
## 꼬마 정민이는 이제 A + B 정도는 쉽게 계산할 수 있다. 이제 A + B + C를 계산할 차례이다!

# 입력
## 첫 번째 줄에 A, B, C (1 ≤ A, B, C ≤ 1012)이 공백을 사이에 두고 주어진다.

# 출력
## A+B+C의 값을 출력한다.

#입력예제 : 77, 77, 7777 출력예제 : 7931

# 1의 자리 연산 , 10의 자리 연산, 100의 자리 연산

a,b,c = input().split()

A = int(a)
B = int(b)
C = int(c)

print(A+B+C)
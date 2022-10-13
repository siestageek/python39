# 반복문
# 정해진 회수 만큼 특정코드를 실행하도록 만든 문장
# 파이썬에서는 for문과 while문이 지원

# 만일, Hello, World!!를 1번 출력한다면?
# -> print함수 1번 사용
print('Hello, World!!')

# 그런데, Hello, World!!를 3번 출력한다면?
print('Hello, World!!') # 3번 출력
print('Hello, World!!')
print('Hello, World!!')

# 만일, 100번 출력해야 한다면 복붙을 계속할 것인가?
# 또한, 반복시 출력하는 문구가 변경된다면? - 다시 수정
# 효율적인 반복실행을 위해서 반복문을 사용함

# for 반복변수 in range(시작값, 종료값-1, 증감값):
#     반복실행할 문장

# range함수 사용하기
# range(숫자) - 0부터 숫자-1까지의 범위
list(range(10))  # 0 ~ (10-1) 범위

# range(시작, 끝-1) - 시작값부터 끝값-1까지의 범위
list(range(1, 45+1))

# range(시작, 끝-1, 증감값)
# => 시작값에서 증감값을 처리해서 끝값-1의 범위까지 출력
list(range(1, 10, 2))
list(range(0, 10, 2))

# ex) 1 ~ 100 사이 정수 출력
print(1)
print(2)
print(3)
# ...
print(99)
print(100)

# 반복문을 이용한다면?
list(range(1, 100+1))

for i in range(1, 100+1):
    print(i, end=', ')
# print함수로 값 출력시 줄바꿈 문자가 자동 추가됨
# 줄바꿈 문자 대신 다른 문자로 대신하려면 end 속성 사용

# ex) 100 ~ 1 사이 정수 출력
list(range(100, 0, -1))

for i in range(100, 0, -1):
    print(i, end=' ')

# ex) 1 ~ 100 사이 정수 중 짝수만 출력
list(range(2, 100+1, 2))

for i in range(2, 100+1, 2):
    print(i, end=' ')

list(range(1, 100+1))

for i in range(1, 100+1):
    if i % 2 == 0: print(i, end=' ')

# ex) 1 ~ 100사이 정수들의 모든 합 계산후 출력
hap = 0

for i in range(1, 100+1):
    hap = hap + i

print(hap)

# 가우스 덧셈 공식을 이용해서
# 1 ~ 100사이 모든 정수들의 합 계산후 출력
# x ~ y 까지의 숫자를 더한 합을 구하는 공식
# ((x + y) * (y - x + 1)) / 2
((1 + 100) * (100 - 1 + 1)) / 2


# 문자열에 반복문 적용하기
# => 문자열에서 문자를 하나씩 가져와서 출력함
for i in 'Hello, World!!':
    print(i, end=' ')


# ex) 단을 입력받아 해당 단의 구구단을 출력
dan = int(input('단은?'))

# print(f'{dan} x 1 =', (dan*1))
# print(f'{dan} x 2 =', (dan*2))
# print(f'{dan} x 3 =', (dan*3))
# print(f'{dan} x 4 =', (dan*4))
# print(f'{dan} x 5 =', (dan*5))
# print(f'{dan} x 6 =', (dan*6))
# print(f'{dan} x 7 =', (dan*7))
# print(f'{dan} x 8 =', (dan*8))
# print(f'{dan} x 9 =', (dan*9))

for i in range(1, 9+1):
    print(f'{dan} x {i} = {dan * i}')


# p79 ex3) 3의 배수지만 2의 배수는 아닌 정수 출력하고
# 누적합도 계산해서 출력
hap = 0
result = ''
for i in range(1, 100+1):
    if i % 3 == 0 and i % 2 != 0:
        result += str(i) + ' '
        hap += + i

print(result)
print(hap)









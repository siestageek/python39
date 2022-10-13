# 20

# 22 - if문의 함정
number = 30

if number % 2 == 0:
    print('입력한 값은 짝수입니다')
print('입력한 값은 홀수입니다')

if number % 2 == 0:
    print('입력한 값은 짝수입니다')
else:
    print('입력한 값은 홀수입니다')


# 26 - 연봉/결혼 여부 세금 계산 (0:미혼)
salary = int(input('연봉은?'))
isMarried = int(input('결혼여부는? (0:미혼, 1:기혼)'))
tax = 0

if isMarried:
    if salary < 6000: tax = salary * 0.15
    else: tax = salary * 0.35
else:
    if salary < 3000: tax = salary * 0.1
    else: tax = salary * 0.25

print(salary, isMarried, tax)


# 27 - 윤년 여부
# 2020, 2008, 2000 윤년
# 2022, 1900, 2010 평년
year = int(input('년도는?'))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, '는 윤년입니다')
else:
    print(year, '는 윤년이 아닙니다')


# 25 - 복권 발행 프로그램 v1
# 난수 생성시 random 모듈의 randrange(st, ed-1) 사용
import random as rnd

yourkey = int(input('복권번호는?'))
lottokey = rnd.randrange(111, 1000)

if yourkey == lottokey:
    print('복권 당첨!! - 상금 백만원!!')
else:
    print('아쉽지만 다음 기회를!!')

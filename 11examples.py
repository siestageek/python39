# 33 - 신용카드 판별
card = input('신용카드번호는?')
result = ''

# if card == '356317': result = 'NH농협JCB카드'
# elif card == '515594': result = '신한Master카드'
# ...

if card[:2] == '35':
    nums = card[2:]   # 나머지 카드 번호 추출
    if nums == '6317': result = 'NH농협 JCB카드'
    elif nums == '6901': result = '신한 JCB카드'
    elif nums == '6912': result = 'KB국민 JCB카드'
    else: result = '잘못된 카드번호입니다!!'

elif card[:1] == '4':
    nums = card[1:]   # 나머지 카드 번호 추출
    if nums == '04825': result = '비씨 Visa카드'
    elif nums == '38676': result = '신한 Visa카드'
    elif nums == '57973': result = 'KB국민 Visa카드'
    else: result = '잘못된 카드번호입니다!!'

elif card[:1] == '5':
    nums = card[1:]   # 나머지 카드 번호 추출
    if nums == '15594': result = '신한 Master카드'
    elif nums == '24353': result = '외환 Master카드'
    elif nums == '40926': result = 'KB국민 Master카드'
    else: result = '잘못된 카드번호입니다!!'

else: result = '잘못된 카드번호입니다!!'

print(result)


# 35 - 시간때를 의미하는 영단어 판별
daytime = input('시간때를 의미하는 영단어는?')
result = '잘못입력하셨습니다!'

if daytime == 'morning hours': result = '아침시간 (7~12)'
# elif daytime == 'midday' or daytime == 'noon': result = '점심시간'
elif daytime in ('midday', 'noon') : result = '점심시간 (12~1)'
elif daytime == 'afternoon hours': result = '오후(1~6)'
elif daytime == 'evening hours': result = '저녁시간(6~9)'
elif daytime == 'night hours': result = '밤시간(9~12)'
elif daytime == 'midnight': result = '자정시간(12)'
elif daytime == 'early morning hours': result = '새벽시간(12~5)'
elif daytime == 'small hours': result = '새벽(1~3)'
elif daytime in ('dawn', 'daybreak') : result = '해뜰력 (5~7)'

print(result)


# switch ~ case 와 비슷하게 작성해보기
# 파이썬은 지금까지(~v3.9)  switch ~ case 구문을 지원하지 않음
# 만일, switch ~ case 구문을 구현하려면 dict를 이용해야 함
# 한편, v3.10 이상부터는 match case라는 구문으로 구현가능

# dict 자료구조
# 키와 값 형태로 자료를 저장하는 형식
# 연관(키-값) 배열 자료형의 한 종류임
# 객체명 = {키 : 값} => 객체명.get(키), 객체명[키]

cards = {'356317':'NH농협JCB카드', '404825':'비씨Visa카드',
         '515594':'신한Master카드'}
cards.get('404825')

daytimes = {'midday':'점심시간', 'noon':'점심시간',
            'midnight':'자정시간', 'small hours':'새벽'}
daytimes.get('midnight')

# 성적처리 프로그램 v3b
# 이름, 국어, 영어, 수학을 입력받아
# 총점, 평균, 학점을 계산하고 출력함
# 학점처리 조건은 수우미양가로 하되
# 학점은 dict를 이용해서 처리함
name = input('이름은?')
kor = int(input('국어는?'))
eng = int(input('영어는?'))
mat = int(input('수학은?'))

tot = kor + eng + mat
avg = tot / 3

grd = '가'
grds = { 10:'수', 9:'수', 8:'우', 7:'미', 6:'양' }
grd = grds.get(avg // 10)

print(f'이름:{name} 국어:{kor} 영어:{eng} 수학:{mat}')
print(f'총점:{tot} 평균:{avg:.1f} 학점:{grd}')


# 3항 연산자 - if 단축문 : 컴프리헨션
# 참일때값 if 조건식 else 거짓일때값
print('참' if True else '거짓')
print('참' if False else '거짓')

# ex) 윤년여부를 출력하는 프로그램을 작성하세요
# 단, 3항 연산자를 이용해서 구현함
year = int(input('년도는?'))

isLeapYear = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
result = '윤년입니다' if isLeapYear else '윤년이 아닙니다'

print(year, result)


# ex) 년도와 월을 입력받아 윤년여부와
# 입력한 달의 마지막 날을 출력하는 프로그램을 작성하세요
# 30: 4, 6, 9, 11
# 31: 1, 3, 5, 8, 10, 12
# 28: 2 (윤년이 아닐때)
# 29: 2 (윤년일때)





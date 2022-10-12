# input 함수
# 변수명 = input(입력메세지)
# input함수로 입력받은 내용은 기본적으로 문자로 취급!

# 성적처리 프로그램 v2
# 이름, 국어, 영어, 수학을 입력받아
# 총점, 평균을 계산하고 출력함
name = input('이름은?')
kor = int(input('국어는?'))  # 산술식에 사용해야 함으로 형변환 필요
mat = int(input('수학은?'))
eng = int(input('영어는?'))

tot = kor + eng + mat
avg = tot / 3

print(tot, avg)

# p57, ex3)
# 지방, 탄수화물, 단백질을 입력받아 총 칼로리 계산
# 풀이1
fat = 25
carbo = 520
protein = 45

totcal = fat * 9 + carbo * 4 + protein * 4
print(totcal)

# 풀이2 - input 함수 사용
fat = float(input('지방은?'))
carbo = float(input('탄수화물은?'))
protein = float(input('단백질은?'))

totcal = fat * 9 + carbo * 4 + protein * 4
print(f'총 칼로리 : {totcal} cal')


# 성적처리 프로그램의 메뉴화면 작성 1
print('성적 처리프로그램 v1')
print('-------------------')
print('1. 성적 데이터 추가')
print('2. 성적 데이터 조회')
print('3. 성적 데이터 상세조회')
print('4. 성적 데이터 수정')
print('5. 성적 데이터 삭제')
print('0. 프로그램 종료')
print('-------------------')

# 성적처리 프로그램의 메뉴화면 작성 2
main_menu = '성적 처리프로그램 v1 \n'
main_menu += '-------------------\n'
main_menu += '1. 성적 데이터 추가\n'
main_menu += '2. 성적 데이터 조회\n'
main_menu += '3. 성적 데이터 상세조회\n'
main_menu += '4. 성적 데이터 수정\n'
main_menu += '5. 성적 데이터 삭제\n'
main_menu += '0. 프로그램 종료\n'
main_menu += '-------------------'

print(main_menu)

# 성적처리 프로그램의 메뉴화면 작성 3
main_menu = f'''
성적 처리프로그램 v1
-------------------
1. 성적 데이터 추가
2. 성적 데이터 조회
3. 성적 데이터 상세조회
4. 성적 데이터 수정
5. 성적 데이터 삭제
0. 프로그램 종료
-------------------'''
print(main_menu)
input('=> 작업을 선택하세요 : ')
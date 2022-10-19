# 튜플tuple
# 파이썬의 리스트와 유사한 자료구조 - 순서기억, 중복저장
# 선언방법은 ()안에 값들을 정의하고 사용
# 단, 튜플의 요소는 수정이나 삭제 불가 (생성은 가능)
# 주로, 읽기전용 데이터를 다룰때 사용 - 상수값 저장

# 튜플 선언
nums = (1,5,10,15,20)
print(nums)

# 튜플의 요소 읽기 : 객체명[인덱스]
print(nums[0], nums[3])

# 튜플의 요소 수정 : 객체명[인덱스] = 수정값
nums[0] = 999

# 튜플의 요소 삭제 : del 객체명[인덱스]
del nums[1]

# 만일, 튜플의 요소를 수정/삭제하려면
# 튜플을 리스트로 변환한 후 값을 수정/삭제하고
# 다시 리스트를 튜플로 변환하면 됨
# 변환함수 : list(객체명), tuple(객체명)
nums = list(nums)     # 튜플 -> 리스트

nums[0] = 999
print(nums)

nums = tuple(nums)    # 리스트 -> 튜플
print(nums)


# ex) 년도를 입력하면 십간와 십이지를 이용해서
# 해당년도의 60갑자(간지) 출력
# 십간 : 갑을병정무기경신임계
# => (10일마다 바뀌는 태양에 부쳐진 이름)
# 십이지 : 자축인묘진사오미신유술해
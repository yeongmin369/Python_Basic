# 컬렉션 타입
# - 변수 하나에 값을 여러개 저장
# - 실질적으로 변수에컬렉션 1개가 저장
# - 리스트(List), 튜플(Tuple), 딕트(Dictionary),                 세트(Set)

# - 1. 리스트(List) - ex) train
# 시퀀스 자료형(연속 된 값 저장)
# 대괄호 사용 []
# 정렬 가능
# mutable(생성 된 후 변경 가능)
# index 사용(Slicing 가능)
# paking과 unpaking 가능
# 멤버함수:  append(), insert(), pop(), remove(), index(), sorted(), 등등
# 2차원 리스트는 표(table)과 동일한 형태

# 리스트 초기화(생성)
list_a = [1, 2, 3]
list_b = []
list_c = ["chosun", 98, 3.14, [1, 2, 3]]

print(list_c[0])  # 리스트에서 단일 값 추출
print(list_c[1:3])  # 리스트 슬라이싱.

# 패킹과 언패킹
list_d = ["A", "B", "C"]  # 패킹

a, b, c = list_d  # 언패킹

# a = list_d[0]
# b = list_d[1]    - 자바, C언어
# c = list_d[2]

# append(): 리스트 맨 마지막에 값 추가!
a = [1, 2, 3, 4, 5]
a.append(10)
print(a)

# insert(): 원하는 인덱스에 값 추가!
a.insert(1, "A")  # (인덱스, 값)
print(a)

# extend(): 리스트 병합(List A + List B)
a = [1, 2, 3]
b = [3, 4, 5]
# a.apeend(b) -> [1,2,3,[3,4,5]]

# a.extend(b) # a를 기준으로 병합
# print(a)
print(a + b)

# remove(): 값으로 삭제
a = ["a", "b", "c"]
a.remove("b")
print(a)
# pop(): 인덱스로 삭제
b = ["a", "b", "c"]
c = b.pop(0)  # 값을 삭제전 변수에 담아서 삭제 후에 사용 가능( 선택)

b.pop(0)
print(b)
print(c)

# index(): 찾고자 하는 값의 인덱스 반환 ()<- 매개변수
a = [1, 2, 3]
print(a.index(3))  # 인덱스 반환

# sort() and sorted(): 리스트 값 정렬!

# - sort(): 원본 값 정렬(주의: 보통 원본 값을 수정  하는 경우 극히 드뭄)
# - sorted(): 복제 한 값 정렬

a = [9, 3, 2, 1, 5, 8, 10]
b = sorted(a)  # 오름차순
c = sorted(a, reverse=True)  # 내림차순
print(a)
print(b)
print(c)

# 2. Tuple ex) train
# - List와 대부분 동일
# 시퀀스 자료형(정렬 불가능)
# immutable(생성 된 후 변경 불가능)
# index 사용(Slicing가능)
# packing과 Unpacking가능
# () 사용(생략 가능)
# 여러분이 직접 tuple을 생성하는 경우 x
# -> 파이썬에서 결과값을 받을 때 Tuple로 제공

print("=" * 100)
a = [1, 2, 3]  # LIST
b = (1, 2, 3)  # TUPLE
c = 1, 2, 3  # TUPLE(괄호 생략 가능)

a[0] = 99
print(a)

# b[0] = 99
# print(b) #Tuple은 값 변경 불가능

# 튜플 원소가 1개의 값인 경우
a = (1, 2, 3)  # tuple
b = 1, 2, 3  # tuple
c = (1)  # tuple
d = 1  # int
e = 1,  # tuple

print(type(b))
print(type(d))
print(type(e))

# a랑b랑 교환하는 코드 작성
a = 5
b = 8

# c=a
# a=b
# b=c

a, b = b, a  # Tuple packing & unpacking 사용
print(a)  # 8
print(b)  # 5

# 3. Set   ex) 복주머니
# 수학의 집합 개념 순서 없음(index 없음, 정렬 불가능)
# 중복값을 허용하지 않음(중요)
# {} 사용
# 멤버함수: union(), intersection(), difference() 등등

set_a = {1, 2, 3}
set_b = {1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5}
print(set_b)

# 중복값 제거 활용 방법
# a List의 중복값을 제거
a = ["A", "A", "B", "B", "C", "C", "D", "E"]  # List type
# a = set(a) #()안의 값을 set type으로 변환
# a = list(a) #()안의 값을 list type으로 변환
# List -> Set(중복값 제거) -> List
a = list(set(a))
print(a)
print(type(a))

# 딕트 (dict)  ex) 복주머니
# 순서가 없음(인덱스 없음, 정렬 불가능)
# {key,: value} 사용 - > key, value 1 pair
# key는 중복 불가, value 중복 가능
# key를 통해서만 value에 접근 가능
# 멤버함수 update(), get(), keys(), values(), items()

# 외부에서 데이터를 받아올 때 대부분 JSON 형식으로 전달
# - JSON == DICT

# {"id" : "ccw1102", "pw": "abv1234!", "name", "최철웅"}

dict_a = {"Korea": "Seoul",
          "Canada": "Ottawa",
          "USA": "Washington D.C"}
print(dict_a)
import pprint

pprint.pprint(dict_a)

# update() : dict와 dict 병합
a = {"a": 1,
     "b": 2, }
b = {"b": 3,
     "c": 5, }
a.update(b)  # 병합시 중복key 있는 경우 입력값(b)이 우선
print(a)

# pop() : dict 원소를 key를 통해서 삭제
c = a.pop("a")
print(a)
print(c)  # {"a" : 1} 삭제 된 value(key x)

# in(): ()안의 key 값이 존재 확인
print("c" in a)
print("f" in a)

# get() : 값 접근
# list, tuple, dict 접근 -> 컬렉션[index or key] ex: a[0] ex: a[2]

# print(a["f"]) # key가 없으면 error 발생
print(a.get("f"))  # key 없으면 None 출력(error X)

# keys(), values(), items()
print(a.keys())  # key만 추출
print(a.values())  # value만 추출
print(a.items())  # (key, value) 추출

print(list(a.keys()))  # 활용 방법

# claer(): dict 초기화

print(a)
a.clear()
print(a)

a = {}
print(type(a))


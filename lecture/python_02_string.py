# 문자열의 이해(string)

# 1. 문자열 인덱스
# - 문자열은 각 문자마다 순서(인덱스)가 있음
# - 첫번째 문자부터 마지막 문자까지 순차적으로 인덱스
# - 인덱스 시작은 0
# - 인덱스는 공백 포함
print("* 。 • ˚ ˚ ˛ ˚ ˛ • 。* 。° 。* 。 • ˚"*10)
print("python(´▽`ʃ♡ƪ)")

# 2. 문자 추출
# - 인덱스를 통해서 문자 추출
# - 인덱스 범위 벗어난 경우 오류(Error: index out of range)
lang = "Python"
print(lang[0])
print(lang[2])
# print(lang[9]) Error

# -1 인덱스(Reverse Index)
# - 우측에서 좌측으로 인덱스
# - 시작값 -1
print(lang[-1])
print(lang[-3])

# 3. 문자열 슬라이싱
# - lang[3]: 문자 1개만 추출
# - 부분 문자열을 추출하고 싶은 경우
# - 시작인덱스, 끝인덱스 필요!

msg = "Python is all you need"
print(msg[0:6]) # 끝 인덱스+1
print(msg[:6]) # 시작 인덱스 생략 ➡ 자동 0 입력
print(msg[6:]) # 끝 인덱스 생략 ➡ 자동 -1 입력

print(msg[17:22])
print(msg[-5:])

# 4. 문자열 함수
str = "Hello World"

print("* 。 • ˚ ˚ ˛ ˚ ˛ • 。* 。° 。* 。 • ˚"*10)
# 4-1. len() : 문자열 길이 계산
print(len(str))

# 4-2. upper() and lower() : 대소문자 변경
# - 데이터 전처리: 1A, 1a ➡ 1A 통일(upper())
print(str.upper())
print(str.lower())

# 4-3. replace() : 문자열 내의 특정 문자 치환
print(str.replace("H", "J"))

# 4-4.split() : 구분자를 기준으로 문자열 분할(Default: 공백)
b = "hello world what a nice weather"
print(b.split("w")) #w를 기준으로 분할
print(b.split()) #공백을 기준으로 분할

# 4-5.strip() : 문자열의 좌우 공백을 제거
id = "                              python1004                   "
print(id)
print(id.strip())

# 4-6.find() and rfind() : 문자열 내부의 특정 문자 위치 인덱스 출력(하나만, 중복 고려 안 함)
print(str.find("o")) # Hell"o" World
print(str.rfind("o")) # Hello W"o"rld
print(str.find("world")) # 없으면 -1 출력
print(str.find("World")) # 단어의 첫글자 인덱스 출력
print(str.rfind("World")) # 단어의 첫글자 인덱스 출력

# 4-7.in() : 특정 문자열 포함하는지 확인(True, False 출력)
print("Hi" in "Hi Python")

# 1. id = "cherry1004@gmail.com"
#   ➡ id 만 추출 "cherry1004"
id = "cherry1004@gmail.com"
val = id[:10]
print(val)

print("* 。 • ˚ ˚ ˛ ˚ ˛ • 。* 。° 。* 。 • ˚"*10)

i = id.find("@")
print(id[:i])
# i = id[:id.find("@")] 교수님 답안

# www.naver.com
# www.daum.net
# www.goole.com

na = "www.naver.com"
w = na.rfind(".")
d = na.find(".")+1
print(na[d:w])


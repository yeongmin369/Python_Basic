# while 반복문
# - 반복횟수를 모르는 경우
# - 조건이 만족하는 동안 꼐속 반복
# - 조건 True이면 무한 반복
# - 조건 False이면 반복 종료
# - while문에 조건 True ➡ 무한 Loop문(조심!)
# - 반드시 break문과 함께 사용할 것!

# while 기본 문법
# while 조건:
#       실행문

a = list(range(1, 6))
print(a)

i = 0 #index
while i < len(a):
    print(a[i])
    i += 1

# 사용자가 입력한 값 1,2,3 통과
# 아닌 경우 다시 입력하도록

count = 0 #틀린 횟수
 #while True:
  #  if count >= 4:
 #      num = int(input("값: "))
  #     print("프로그램을 사용할 수 없습니다.")
  #     break
  #       if num in [1, 2, 3]:
  #         print(f"{num}을 입력하셨습니다.")
  #         break
  #        else:
   #        print("1, 2, 3의 값만 입력해 주세요.")

#문제7) 1부터 100까지 총합을 출력하는 코드
# - for문으로 작성


print("* 。 • ˚ ˚ ˛ ˚ ˛ • 。* 。° 。* 。 • ˚"*10)
sum = 0
for num in range(1, 101):
    sum += num
print(sum)
print("* 。 • ˚ ˚ ˛ ˚ ˛ • 。* 。° 。* 。 • ˚"*10)
# - while문으로 작성
num = 0
total = 0
while True:
    num += 1
    if num == 101:
        break
    total += num
print(f"{total}")


# 제어문
# 1. 조건문 (if)
# 2. 반복문 (for, while)

# 반복문 (Loop)
# - 반복적인 작업을 가능하게 해주는 도구
# - list, str, tuple 등 컬렉션 타입의 아이템을 하나씩 순회하면서
#   사용 가능 (for)
# - 특정 조건을 만족하는 경우 (while)

# 반복 횟수 O -> for
# 반복 횟수 X => while

# for 문
# for i in [1,2,3]:
#   print(i)
# for (int i = 0; i < 3; i ++) {
#   print(i)
# }
# range 함수
# default : 시작(0), 증감(+1)
# range(시작, 끝, 증감)
# range(3)          => 0, 1, 2
# range(1, 10)      => 1, 2, 3, 4, 5, 6, 7, 8, 9,
# range(2, 5, 2)    => 2, 4

# range()를 활용해서 1 ~ 9 까지 출력하는 for문
for i in range(1, 10):
    print(i)
# List를 활용한 for문
temp = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
for alpha in temp:
    print(alpha)
# 반복 횟수(index) 출력하고 싶을 경우!
# - enumerate() : 0번 인덱스부터 시작
# for i, alpha in temp:
    #print(i+1, alpha)


print("="*100)

# 구구단 2단 출력
# 2 x 1 = 2
# 2 x 2 = 4
# ...
# 2 x 9 = 18

for i in range(1,10):
   print(f"2x{i}={2*i}")

# input() 활용해서 사용자가 입력한 값 (2 ~ 9) => 해당 칸 출력
dan = int(input("단수: "))
for i in range(1, 10):
    print(f"2x{i}={2 *int(i)}")
print("="*100)
# 2단 9단까지 출력 => 중첩for
# 2 x 1 = 2
# 2 x 2 = 4
# ...
# 2 x 9 = 18
# 3 x 1 = 3
# ...
# 9 x 9 = 81

# for i in range(1, 10):
    # print(f"{dan}x{i}={dan*i}")

for dan in range(1,10):
    for i in range(1,10):
        print(f"{dan} x {i} = {dan*i}")

# dict를 사용한 for문
#
temp = {"A" : 1,
        "B" : 2,
        "C" : 3,
        "D" : 4}

print("="*100)
# dict => for => key값 출력
# keys(), values(), items()
for element in temp.values():
    print(element)

for element in temp.items():

for key, value in temp.items():
    print("*****")
    print(key)      # key
    print(value)    # value

# break, continue
# break : 즉시 반복문을 빠져 나가세요.
# continue : 즉시 다음 반복으로 넘어가세요.

a = [1, 2, 3, 4, 5]
for i in a:
    if i == 3:
        break
    print(i)

# 짝수만 출력
for i in range(30):
    if i % 2 == 0:
        continue
    print(i)

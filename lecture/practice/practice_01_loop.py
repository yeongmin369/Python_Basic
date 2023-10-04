# 문제 1 ) 입력 된 단수를 출력하는 코드
# dan = int(input("단수:"))
# for i range ( 1, 10)
#   print(f"{dan}x{i}={dan*i}")


# 문제 2) 2단 9단까지 출력 => 중첩for
# 2 x 1 = 2
# 2 x 2 = 4
# ...
# 2 x 9 = 18
# 3 x 1 = 3
# ...
# 9 x 9 = 81
for i in range(1, 10):
    for j in range(1,10):
        print(f"{i}x{j}={i*j}")

# 문제 3) list a 의 평균값을 계산하세요.
a = [1, 2, 3, 4, 5, 99, 87, 54, 2, 5, 4]
length = len(a)
total = 0
for num in a:
    total = total + num
length = len(a)
result = total / length
# round (값, 소수점숫자) : 반올림
print(round(result, 2)) # 평균값

# 문제 4) list b에서 최소값 찾기 !
b = [22, 1, 4, 7, 98]

print(num_min) # 1 출력

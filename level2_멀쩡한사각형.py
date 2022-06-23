# 직선 방정식을 이용하여 값 구하기
w = 8
h = 12

def f(x):
    y = h/w * x
    return y

y_list = []
for x in range(w+1):
    y_list.append(f(x))

count = 0
for i in range(len(y_list)-1):
    cmp1 = int(y_list[i])  # 내림

    if y_list[i+1] % 1 == 0:
        cmp2 = int(y_list[i+1]) # 정수일 때는 그대로
    else:
        cmp2 = int(y_list[i + 1] + 1)  # 올림

    count += (cmp2 - cmp1)

# print(w*h - count)

######################################
# 위의 코드는 시간초과 및 테스트 케이스 실패....
# 최대공약수를 사용하여 문제를 해결할 수 있다. --> 유클리드 호제법 사용

def gcd(w,h):
    a = max(w,h)
    b = min(w,h)
    while b:
        a, b = b, a%b
    return a

x = gcd(w,h)
count = (w//x + h//x - 1)*x
print(w*h-count)
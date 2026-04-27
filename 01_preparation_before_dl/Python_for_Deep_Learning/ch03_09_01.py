resolution = 256
if resolution < 256:
    print("해상도가 너무 작습니다.")
else:
    print("충분히 큰 해상도입니다.")
    print("입력한 해상도는", resolution,"입니다.")

print("---------------------------")
x = int(input())
y = int(input())

if y == 0:
    print('0으로 나눌 수 없습니다.')
else:
    print(x/y)

print("---------------------------")
score = 90
if score >= 94:
    print('1등급입니다.')
elif score >= 87:
    print('2등급입니다.')
elif score >= 81:
    print('3등급입니다.')
else:
    print('3등급 미만입니다.')

age = 25
if age >= 1 and age < 8:
    print("입장료는", 3000,"원입니다.")
elif age >= 8 and age < 19:
    print("입장료는",7000,"원입니다")
elif age >= 19 and age < 60:
    print("입장료는", 12000, "원입니다")
elif age >= 60 :
    print("입장료는", 0 ,"원입니다")


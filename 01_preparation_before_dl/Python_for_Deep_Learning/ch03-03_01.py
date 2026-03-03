#print(값): 원하는 값을 출력 할 수 있다.

data = "Hello World"
print(data)

print("Hello python")
print("Wellcome to deep learning World")

data1 = 7
data2 = 5
data3 = 8

print(data1, data2, data3)
print(data1, data2, data3, sep=",")
print(data1, data2, data3, end="[END]")

score = 70
print(f"학생의 점수는{score}점입니다.")
#input() : 사용자로부터 입력을 받을 수 있다.
data = input()
print(data)

data = input("당신의 이름은? ")
print("입력된 값:", data)

age = int(input("당신의 나이는? "))#입력받은 값은 문자열이므로 int() 함수를 이용하여 정수로 변환
print("당신의 나이:", age)    
print("당신의 나이 15년 후:", age + 15)

#사전 자료형
#데이터를 키와 값 깡의 형태로 저장할 때 사용할 수 있다
#다음과 같은 형태로 사전 자료형에 데이터를 기록 할 수 있다
#사전 데이터[키] = 값

arr1 = ["컴퓨터","키보드","모니터"]
arr2 = ["computer","keyboard","monitor"]

data = {}
for i in range(3):
    data[arr1[i]] = arr2[i]
print(data)
#모든 키를 하나씩 확인할 때는 keys() 메서드를 사용할 수 있다
data = {}
data['apple'] = '사과'
data['banana'] = '바나나'
data["carrot"] = "당근"
for key in data.keys():
        print("key:",key, "value:",data[key])
#사전 자료형은 특정한 데이터의 등장 횟수를 셀 때 효과적으로 사용할 수 있다.
data = [1,3,3,5,4,3,2,1,4]
counter = {}

for x in data:
    if x not in counter:
        counter[x] = 1
    else:
        counter[x] += 1

print(counter)
#집합 자료형
#데이터의 중복을 허용하지 않고 순서가 상관없을 때 사용하는 자료형이다
#특정한 데이터가 등장한 적 있는지 체크할때 효과적으로 사용된다
#데이터를 삽입할 때는 add() 메서드를 사용한다
data = [1,3,3,5,4,3,1,4]
visited = set()
for x in data:
    if x not in visited: #데이터가 있는지 체크할 때는 in이나 not in 연산자 사용
        visited.add(x)
    else:
        print("중복 원소 발견:",x)
    
print("고유한 원소들:",visited)
#집합 자료형은 remove() 메서드를 사용하여 특정한 원소를 제거할 수 있다
# 집합 자료형은 list()함수를 이용하여 리스트로 변경할 수 있다.
dtat = {5,6,7,8,9}
print(data)

data.remove(7)
print(data)

arr = list(data)
print(arr)
#집합 자료형은 다양한 연산자를 제공한다
#합집합 연산자:|
#교집합 연산자:&
#차집합 연산자:-

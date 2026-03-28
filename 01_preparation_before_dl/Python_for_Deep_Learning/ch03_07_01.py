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
# 📊 [선수 지식] 통계 1) 확률(Probability) 개요

> 💡 **핵심 요약:** 확률은 특정 사건의 가능성을 0~1 사이의 수로 표현한 것이며, 딥러닝 모델의 출력과 데이터 처리에 필수적인 기초 개념입니다.

---

## 1. 확률의 정의와 활용

### 기본 정의
특정한 사건이 일어날 가능성을 **0~1 사이의 실수**로 표현합니다.

### 스팸 분류 모델 예시
- 도착 메일 총 1,000개 중  
  - 스팸: 700개  
  - 정상: 300개  
- 새 메일이 스팸일 확률:

\[
P(\text{Spam}) = \frac{700}{1000} = 0.7 = 70\%
\]

### 기계학습에서의 확률 해석
모델의 출력은 대부분 **확률 형태**입니다.

- 이미지 분류  
  → “이 이미지가 고양이일 확률 = 75%”
- 텍스트 생성  
  → “‘나는 밥을’ 다음에 ‘먹었다’가 나올 확률 = 42%”

---

## 2. 경우의 수: 순열과 조합

확률 계산의 핵심은 **순서 고려 여부**입니다.

---

### ① 순열 (Permutation)

**정의**  
서로 다른 n개에서 r개를 중복 없이 뽑아 **순서를 고려하여 나열**

**공식**
\[
nP_r = \frac{n!}{(n-r)!}
\]

**딥러닝 활용 예**
- 학습 데이터 **셔플(Shuffling)** 경우의 수 계산

**Python 예제**
```python
from itertools import permutations

arr = ['A', 'B', 'C']
result = list(permutations(arr, 2))
# [('A','B'), ('A','C'), ('B','A'), ('B','C'), ('C','A'), ('C','B')]
```

---

### ② 조합 (Combination)

**정의**  
서로 다른 n개에서 r개를 **순서를 고려하지 않고 선택**

**공식**
\[
nC_r = \frac{n!}{r!(n-r)!}
\]

**딥러닝 활용 예**
- Siamese Network → 이미지 **쌍(pair)** 생성

**Python 예제**
```python
from itertools import combinations

arr = ['A', 'B', 'C']
result = list(combinations(arr, 2))
# [('A','B'), ('A','C'), ('B','C')]
```

---

## 3. 중복 허용 경우의 수

---

### ① 중복 순열 (Permutation with Repetition)

**정의**  
중복 허용 + 순서 고려

**공식**
\[
n^r
\]

**Python**
```python
from itertools import product

arr = ['A','B','C']
result = list(product(arr, repeat=2))
```

---

### ② 중복 조합 (Combination with Repetition)

**정의**  
중복 허용 + 순서 미고려

**공식**
\[
nH_r = \binom{n+r-1}{r}
\]

**딥러닝 활용 예**
- 앙상블 모델 구성

**Python**
```python
from itertools import combinations_with_replacement

arr = ['A','B','C']
result = list(combinations_with_replacement(arr, 2))
```

---

## 4. 통계적 확률

**개념**
\[
\lim_{N\to\infty} \frac{R}{N}
\]

시행 횟수가 증가할수록 **이론 확률에 수렴**

### 주사위 예시 (5가 나올 확률)

| 시행 횟수 | 확률 |
|---|---|
| 6회 | 0.333 |
| 60,000회 | 0.1679 |

---

## 5. 실제 응용: 생성 모델

### Generative Model
실제로 존재하지 않는 데이터를 **확률 기반으로 생성**합니다.

**특징**
- 데이터 분포를 학습하여 새로운 샘플 생성
- 이미지, 텍스트, 음성 생성 등에 활용

**대표 사례**
- PGGAN (2018)
- 고해상도 가상 인물 이미지 생성 가능

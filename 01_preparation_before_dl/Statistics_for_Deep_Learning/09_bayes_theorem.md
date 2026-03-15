# 베이즈 정리 (Bayes' Theorem)
 
> Fast Campus | 선수 지식 - 통계 | 강사: 나동빈
 
---
 
## 1. 문제 상황 — 스팸 분류 모델
 
텍스트 $x$가 입력으로 주어졌을 때, 스팸(spam) 또는 햄(ham)으로 분류하는 소프트웨어를 만드는 것이 목표다.
 
- **입력**: 하나의 텍스트(text)
- **출력**: 텍스트가 특정 클래스(스팸 또는 햄)에 속할 확률
- **목표**: 텍스트 $x$가 스팸 $y$일 확률 $P(y_2 \mid X = x)$ 계산
 
클래스는 두 가지만 존재한다고 가정한다.
 
$$y_1 = \text{햄(ham)}, \quad y_2 = \text{스팸(spam)}$$

### 예시
 
| 클래스 | 확률 |
|--------|------|
| $P(y_1 \mid X = x)$ — 햄(ham)일 확률 | 5% |
| $P(y_2 \mid X = x)$ — 스팸(spam)일 확률 | 95% |
 
---
 
## 2. 배경지식 — 조건부 확률 복습
 
사건 $X$가 발생했을 때, 사건 $Y$가 발생할 확률을 의미한다.
 
$$P(Y \mid X) = \frac{n(X \cap Y)}{n(X)}$$
 
---

## 3. 베이즈 정리 (Bayes' Theorem)
 
$P(Y \mid X)$를 직접 계산하기 어려울 때, 베이즈 정리를 이용한다.
 
### 공식
 
$$P(Y \mid X) = \frac{P(X \mid Y) \, P(Y)}{P(X)}$$
 
$$\text{posterior} \propto \text{likelihood} \times \text{prior}$$
### 각 항의 의미
 
| 기호 | 의미 |
|------|------|
| $P(X)$ | 특정 텍스트가 나올 확률 (evidence) |
| $P(Y)$ | 특정 클래스가 나올 확률 (**사전 확률, prior**) |
| $P(X \mid Y)$ | 특정 클래스에서 특정 텍스트가 나올 확률 (**가능도, likelihood**) |
| $P(Y \mid X)$ | 특정 텍스트가 특정 클래스에서 나올 확률 (**사후 확률, posterior**) |
 
 ### 유도 과정
 
조건부 확률 정의로부터 유도한다.
 
$$P(A \mid B) = \frac{P(A, B)}{P(B)} \quad \Rightarrow \quad P(A, B) = P(A \mid B) \, P(B)$$
 
$$P(B \mid A) = \frac{P(A, B)}{P(A)} \quad \Rightarrow \quad P(A, B) = P(B \mid A) \, P(A)$$
 
두 식을 같다고 놓으면:
 
$$P(A \mid B) \, P(B) = P(B \mid A) \, P(A)$$
 
$$\therefore \quad P(A \mid B) = \frac{P(B \mid A) \, P(A)}{P(B)}$$
 
---
## 4. 풀이 예시 — 스팸 메일 분류 문제
 
### 주어진 정보
 
| 항목 | 값 |
|------|----|
| $P(\text{스팸})$ | 0.7 |
| $P(\text{정상})$ | 0.3 |
| $P(\text{대출} \mid \text{스팸})$ | 0.9 |
| $P(\text{대출} \mid \text{정상})$ | 0.03 |
 
**Q. "대출"이라는 단어가 들어있는 메일이 스팸 메일일 확률 $P(\text{스팸} \mid \text{대출})$은?**
 
### 풀이
 
**Step 1.** $P(\text{대출})$ 먼저 계산 (전체 확률의 법칙 적용)
 
$$P(\text{대출}) = P(\text{대출} \mid \text{스팸}) \, P(\text{스팸}) + P(\text{대출} \mid \text{정상}) \, P(\text{정상})$$
 
$$= 0.9 \times 0.7 + 0.03 \times 0.3 = 0.63 + 0.009 = 0.639$$
 
**Step 2.** 베이즈 정리 적용
 
$$P(\text{스팸} \mid \text{대출}) = \frac{P(\text{대출} \mid \text{스팸}) \, P(\text{스팸})}{P(\text{대출})} = \frac{0.9 \times 0.7}{0.639} \approx 0.986$$
 
---
## 5. 확률 모델 (Probabilistic Models)
 
일반적인 분류 모델은 다음 공식으로 예측 결과 $\hat{y}$를 계산한다.
 
$$\hat{y} = \underset{y}{\operatorname{argmax}} \, P(y \mid x)$$
베이즈 정리를 적용하면:
 
$$\underset{y}{\operatorname{argmax}} \, P(y \mid x) = \underset{y}{\operatorname{argmax}} \, \frac{P(x \mid y) P(y)}{P(x)} = \underset{y}{\operatorname{argmax}} \, P(x \mid y) P(y)$$
 
> $P(x)$는 모든 클래스에 대해 동일하므로, **분모 $P(x)$는 무시해도 된다.**
 
---


## 6. 최대 우도 추정 (Maximum Likelihood Estimation)
 
가능도(likelihood)가 가장 높은 클래스를 선택하는 방법이다.
 
- $X$ = 텍스트 내 광고성 단어의 개수("특가" 등)
- likelihood만 고려 시: $X \geq 5$이면 스팸으로 분류
 
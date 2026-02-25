# 표준정규분포 (Standard Normal Distribution) 정리

## 1. 표준 정규 분포란?

**평균이 0이고 분산이 1인 표준화된 정규 분포**

$$Z \sim N(0, 1)$$

$$\mu = E(X) = 0, \quad \sigma = SD(X) = 1, \quad \sigma^2 = Var(X) = 1$$

---

## 2. 표준화 공식

확률 변수 $X$가 $X \sim N(\mu, \sigma^2)$을 따를 때, 아래 공식으로 **표준화(Standardization)** 가능:

$$Z = \frac{X - \mu}{\sigma}$$

---

## 3. 확률밀도함수 (PDF)

$Z \sim N(0, 1)$일 때 확률밀도함수:

$$f(z) = \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}z^2}$$

---

## 4. 표준 정규 분포의 확률 구간

| 구간 | 확률 |
|------|------|
| $\mu - 1\sigma$ ~ $\mu$ | 34.1% |
| $\mu$ ~ $\mu + 1\sigma$ | 34.1% |
| $\mu - 2\sigma$ ~ $\mu - 1\sigma$ | 13.6% |
| $\mu + 1\sigma$ ~ $\mu + 2\sigma$ | 13.6% |
| $\mu - 3\sigma$ ~ $\mu - 2\sigma$ | 2.1% |
| $\mu + 2\sigma$ ~ $\mu + 3\sigma$ | 2.1% |
| $3\sigma$ 이상 또는 이하 | 0.1% |

> $\sigma = 1$이므로, $P(Z \leq 1) \approx 84.1\%$

---

## 5. 표준 정규 분포 표 (누적 분포 함수)

| $z$ | +0.00 | +0.05 |
|-----|-------|-------|
| 0.0 | 0.50000 | 0.51994 |
| 0.2 | 0.57926 | 0.59871 |
| 0.5 | 0.69146 | 0.70884 |
| 0.7 | 0.75804 | 0.77337 |
| 0.8 | 0.78814 | 0.80234 |
| 1.0 | 0.84134 | 0.85314 |
| 1.5 | 0.93319 | 0.93943 |
| 2.0 | 0.97725 | 0.97982 |
| 2.5 | 0.99379 | 0.99461 |
| 3.0 | 0.99865 | 0.99886 |

---

## 6. 예시 문제

### 예시 ① 확률 계산

**$P(0 \leq z \leq 0.75)$는 얼마인가?**

$$P(0 \leq z \leq 0.75) = P(z \leq 0.75) - P(z \leq 0) = 0.77337 - 0.5 = 0.27337$$

**$P(z \leq 0.8)$는 얼마인가?**

표준 정규 분포 표에서 $z = 0.8$, $+0.00$ 열 → $\boxed{0.78814}$

---

### 예시 ② IQ 계산

- 평균 IQ: $\mu = 100$
- 표준 편차: $\sigma = 24$ (한국 기준)
- **IQ 148은 상위 몇 %인가?**

$$P(X > 148) = P\left(\frac{X - \mu}{\sigma} > \frac{148 - \mu}{\sigma}\right) = P\left(Z > \frac{148 - 100}{24}\right)$$

$$= P(Z > 2) = 1 - f_Z(2) = 1 - 0.97725 = \boxed{0.02275}$$

> 지능 검사에서 **상위 약 2%** → IQ 148로 본다.

---

## 7. 딥러닝에서의 입력 정규화 (Input Normalization)

### 왜 정규화를 하는가?
- 입력 데이터를 정규화하면 **학습 속도(training speed)가 개선**됨
- 각 차원(feature)의 데이터가 **동일한 범위** 내의 값을 갖도록 만들 수 있음

### 표준화 공식

$$\hat{x} = \frac{x - E[x]}{\sqrt{Var[x]}}$$

### Python 구현 예시
```python
import numpy as np
import matplotlib.pyplot as plt

x1 = np.asarray([33, 72, 40, 104, 52, 56, 89, 24, 52, 73])
x2 = np.asarray([9, 8, 7, 10, 5, 8, 7, 9, 8, 7])

normalized_x1 = (x1 - np.mean(x1)) / np.std(x1)
normalized_x2 = (x2 - np.mean(x2)) / np.std(x2)

plt.axvline(x=0, color='gray')
plt.axhline(y=0, color='gray')
plt.scatter(normalized_x1, normalized_x2, color='black')
plt.show()
```

> 결과: **평균(mean) = 0, 분산(variance) = 1** 인 데이터로 변환

### 정규화 3단계 (시각적 이해)

| 단계 | 설명 |
|------|------|
| 원본 데이터셋 | 데이터가 치우쳐 분포 |
| 평균이 0이 된 데이터셋 | 평균을 빼서 중심을 원점으로 이동 |
| 정규화된 데이터셋 | 표준편차로 나눠 스케일 통일 |

### 화이트닝 (Whitening)

- 평균이 0이며 **공분산이 단위행렬**인 정규분포 형태로 변환
- 일반 딥러닝에서는 PCA나 화이트닝보다 **표준 정규화가 더 많이 사용됨**
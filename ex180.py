#!/usr/bin/env python
# coding: utf-8

# In[2]:


low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

# 반복문 밖에 비어있는 volatility리스트를 만든다.
volatility = [ ]
# range(5)를 이용하여 i를 0,1,2,3,4에 대응시킨다.
for i in range(5):       # 0,1,2,3,4
    # 변동폭 diff를 고가와 저가의 차로 정의한다. 이때 인덱싱번호가 같은것끼리 계산되도록한다.
    diff = high_prices[i] - low_prices[i]
    # append()를 사용하여 volatility리스트에 diff값을 추가하면서 확장시켜준다.
    volatility.append(diff)

# volatility리스트를 출력한다.
print(volatility)


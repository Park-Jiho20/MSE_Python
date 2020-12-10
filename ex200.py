#!/usr/bin/env python
# coding: utf-8

# In[7]:


ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

# 각 거래일 수익금 : 종가 - 시가
# 총 수익금 : 3일간의 수익금 총 합

# 누적을 위한 변수와 초기값을 설정한다.
total_profit = 0

# 각 행을 day_profit에 대응 시킨다.
for day_profit in ohlc[1:]:
    # profit을 4열의 수에서 1열의 수를 뺀 값으로 정의한다.
    profit = day_profit[3] - day_profit[0]
    # total_profit에 계산된 profit값을 더하고 for문을 통해 누적해간다.
    total_profit += profit
    
print(total_profit)

# 실행결과 : 0


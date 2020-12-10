#!/usr/bin/env python
# coding: utf-8

# In[8]:


# 아래 두 줄의 코드는 비트코인의 가격 정보를 딕셔너리로 가져오는 코드이다.
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

# 시가, 최고가, 최저가, 변동폭의 값을 불러와서 설정해준다.
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])
최저가 = float(btc['min_price'])
변동폭 = float(btc['max_price']) - float(btc['min_price']) # 변동폭 = (최고가 - 최저가) 

# if - else 구문을 사용하여 (시가+변동폭)이 최고가 보다 높으면 "상승장"을, 그렇지 않으면 "하락장"을 출력하도록 한다.
if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")

# 실행결과 : 상승장


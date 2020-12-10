#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Stock이라는 클래스를 만들고, 
# 종목명과 종목코드를 리턴하는 get_name, get_code 메서드를 추가한다.
class Stock:
    def __init__(self, name, code, per, pbr, 배당수익률):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.배당수익률 = 배당수익률

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

# 종목 이라는 이름의 빈 리스트를 생성한다.
종목 = []

# 3종목에 대한 객체를 생성한다.
삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

# 생성한 객체들을 '종목' 리스트에 저장한다.
종목.append(삼성)
종목.append(현대차)
종목.append(LG전자)

# 리스트에 저장된 각 종목에 대해 for 루프를 통해 종목코드와 PER을 출력한다.
for i in 종목:
    print(i.code, i.per)
    
# 실행결과 :
# 005930 15.79
# 005380 8.7
# 066570 317.34


# In[ ]:





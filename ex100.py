#!/usr/bin/env python
# coding: utf-8

# In[2]:


# data 와 close_price 라는 두 리스트를 생성한다. 
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
# 우선 zip() 함수를 사용하여 data를 키로, close_price를 값으로 설정하고 dict() 함수를 사용하여 close_table 라는 이름의 딕셔너리로 저장한다.
close_table = dict(zip(date, close_price))
# close_table 딕셔너리를 출력한다. 
print(close_table)

# 실행결과 : {'09/05': 10500, '09/06': 10300, '09/07': 10100, '09/08': 10800, '09/09': 11000}


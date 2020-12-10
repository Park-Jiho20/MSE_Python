#!/usr/bin/env python
# coding: utf-8

# In[5]:


class OMG : 
    def print() :     # print(self) 가 되어야함.
        print("Oh my god")

myStock = OMG()
myStock.print()    # OMG.print(mystock)

# 해설 : OMG 와 mystock은 저장되는 메모리가 다르다. 
# mystock.print()를 실행하면 OMG의 class로 넘어가는데, 이 class에 있는 print()함수를 실행하기 위해 필요한 인자들이 mystock으로 자동으로
# 이동하지 않는다. print()는 공용함수이기 때문에 계산에 필요한 인자들이 어느것으로 부터 오는지 명시해 주어야 한다.
# 현재 상황에서는 print()함수의 arguments가 공백인 상태이므로 에러가 발생한다.
# 이를 위해 print(self)로 명시해주어야 한다.


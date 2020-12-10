#!/usr/bin/env python
# coding: utf-8

# In[5]:


# numpy모듈을 불러낸다.
import numpy
# range()는 정수단위 밖에 안되기 때문에 range(0, 5, 0.1)는 실행이 불가하다. 
# numpy.arrange()를 사용하여 0.1 단위의 숫자도 출력할 수 있다.
for i in numpy.arange(0, 5, 0.1):
    print(i)

# 실행결과 : 0부터 4.9까지 0.1 단위로 숫자들이 출력됨.


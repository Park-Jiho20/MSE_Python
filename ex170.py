#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 반복문에서 실행했던 어떤값을 누적할 때, 반복문 밖에 누적을 위한 변수가 필요하다.
# 곱셈을 위해 초기값을 1로 설정한다.
result = 1
# 1~10인 수를 i에 대응시킨다. 
for i in range(1, 11) :
    # result 와 i를 곱하면서 그 결과값을 계속 누적시키고 i가 10이 될 때까지 반복한다.
    result = result * i    # result *= i 도 가능하다.
print(result)

# 실행결과 : 3628800


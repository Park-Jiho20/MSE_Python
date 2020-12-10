#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 6th. num에 (num + 2)를 대입한다. num은 14가 된다.
def 함수0(num) :
    # 7th. 계산값이 28이 된다.
    return num * 2

# 4th. num에 12를 대입하고 계산을 진행한다.
def 함수1(num) :
    # 5th. (num + 2)의 값을 함수0()에 대입한다.
    return 함수0(num + 2)

# 2nd. num에 2를 대입하고 계산한다. 계산 후, num은 12가 된다.
def 함수2(num) :
    num = num + 10
    # 3rd. num을 함수1()에 대입한다.
    return 함수1(num)

# 1st. 함수2()에 2를 대입했다.
c = 함수2(2)
# 8th. 마지막 계산값 28인 c를 출력한다.
print(c)


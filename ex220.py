#!/usr/bin/env python
# coding: utf-8

# In[17]:


# print_max라는 이름의 함수를 정의한다.
def print_max(a, b, c):
    # if - elif - else 구문과 비교연산자를 통해 a, b, c를 비교하여 최댓값을 출력하도록 한다.
    if a > b and a > c:
        print(a)
    elif b > c and b > a:
        print(b)
    else:
        print(c)
# 정의한 함수를 호춯하여 임의의 세 숫자를 기입하고, 최댓값을 출력하도록 한다.        
print_max(1,2,3)

# 실행결과 : 1,2,3 을 지정했을때 3이 출력됨.


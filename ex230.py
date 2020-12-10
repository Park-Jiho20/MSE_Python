#!/usr/bin/env python
# coding: utf-8

# In[5]:


# my_print라는 이름의 함수를 정의한다.
def my_print (a, b) :
    # a, b값을 지정하면 '왼쪽: a' 를 출력한 후, '오른쪽: b'를 출력하도록 한다.
    print("왼쪽:", a)
    print("오른쪽:", b)

# 정의한 함수를 호출하고 a에 200, b에 100을 바인딩하라고 지정한다.
my_print(b=100, a=200)

# 실행결과 : 
# 왼쪽: 200
# 오른쪽: 100


#!/usr/bin/env python
# coding: utf-8

# In[18]:


# 1. endswith() 을 사용하는 방법

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# 리스트의 값들을 i로 받고, endswith() 을 사용하여 i가 ',h' 나 '.c'로 끝나는지 판별한다.
# if문을 사용하여 i가 '.h' 나 '.c'로 끝나면 i를 출력하도록 한다.
# 이때 for문을 사용하여 해당되는 모든 i를 출력하도록 한다.
for i in 리스트:
    if i.endswith(('.h', '.c')):
        print(i)
        
# 실행결과 : intra.h
#            intra.c
#            define.h


# In[17]:


# 2. split() 과 or 을 사용하는 방법

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# 리스트의 값들을 i로 받고, i를 split() 을 사용하여 '.'을 기준으로 name, ext로 나누어준다.
for i in 리스트:
    name, ext = i.split('.')
# if 구문을 사용하여 ext가 h또는 c라면 해당되는 i를 출력하도록 한다.
# for문을 이용하여 모든 i를 판별하고, 조건문에 해당하는 i를 모두 출력하도록 한다.
    if ext == 'h' or ext == 'c':
        print(i)

# 실행결과 : intra.h
#            intra.c
#            define.h


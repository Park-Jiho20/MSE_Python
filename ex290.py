#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 부모라는 class를 생성한다.
class 부모:
    def __init__(self):
        print("부모생성")

# 자식이라는 class를 생성한다.
# 자식 class는 부모 class를 상속받는다.
class 자식(부모):
    def __init__(self):
        # 자식 class가 생성될 때, 먼저 "자식생성"이라고 프린트한다.
        print("자식생성")
        # 추가로, super()라는 키워드를 통해서 부모 class에 접근하고
        # __init__을 통해 부모 class의 생성자를 명시적으로 호출한다.
        super().__init__()        # 이때 self는 알아서 전달이 되므로 쓰지않아도 된다.

나 = 자식()

# 실행결과 : 
# 자식생성
# 부모생성


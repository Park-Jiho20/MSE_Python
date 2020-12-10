#!/usr/bin/env python
# coding: utf-8

# In[2]:


# if True 이므로 참이다. 따라서 다음에 오는 코드들은 실행된다.
if True :
    # if False 이므로 거짓이다. 따라서 실행되지 않는다.
    if False:
        print("1")
        print("2")
    # else 이므로 여기선 True의 값이 된다. 따라서 print("3") 은 실행된다.
    else:
        print("3")
# 첫번째 If와 연결된 else 로서 여기선 False의 값이 된다. 따라서 실행되지 않는다.
else :
    print("4")
# 위의 if 구문과는 연결되지 않은 독립적이고 공통된 명령어이다. 무조건 실행된다.
print("5")

# 실행결과 : 3 과 5


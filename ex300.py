#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 리스트를 생성한다. 다음 코드를 실행하면서 ""는 예외로서 취급된다. 
per = ["10.31", "", "8.00"]

for i in per:
    # try : 실행 코드
    try:
        print(float(i))
    # except : 예외가 발생했을 때 수행할 코드로서, 예외의 경우에 0을 프린트한다.
    except:
        print(0)
    # else : 예외가 발생하지 않았을 때 수행할 코드로서, 예외가 아닌경우에 "clean data"라고 프린트한다.
    else:
        print("clean data")
    # finally : 예외 발생 여부와 상관없이 항상 수행할 코드
    finally:
        print("변환 완료")
        
# 실행결과 : 
# 10.31
# clean data
# 변환 완료
# 0
# 변환 완료
# 8.0
# clean data
# 변환 완료


#!/usr/bin/env python
# coding: utf-8

# In[3]:


# string값에 "abcd"를 설정해준다.
string = "abcd"
# string에 있는 b를 B로 바꾸어준다.
string.replace('b', 'B')
# string값을 출력해준다.
print(string)

# 실행결과 : abcd

# 해설 : 문자열은 변경될수 없다. 따라서 replace함수를 사용하면 aBcd를 저장한 새로운 메모리가 형성되는데, 이를 바인딩해주는 값을
# 정해주지 않았기 때문에 이 메모리는 곧 사라지게 되고, 여전히 string은 abcd만을 지칭하게 된다.


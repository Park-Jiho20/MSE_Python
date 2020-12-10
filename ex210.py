#!/usr/bin/env python
# coding: utf-8

# In[10]:


# message1() 라는 입력값을 받으면 A를 출력하도록 함수를 만든다.
def message1():
    print("A")

# message2() 라는 입력값을 받으면 B를 출력하도록 함수를 만든다. 
def message2():
    print("B")

# message3() 라는 입력값을 받으면 message2() 에 해당하는 B를 출력하고, 연달아 다음줄에 C를 출력하도록 한다.
# 이때 message2() 와 print("C") 는 for문에 포함되어 있으므로 range(3)에 맞게 3번 반복된다.
def message3():
    for i in range (3) :
        message2()
        print("C")
    # for문에 속해있지 않으므로 for문의 반복실행이 끝나면 한 번 실행된다.
    message1()

# message3() 를 입력한다.
message3()

# 실행결과 : B
#            C
#            B
#            C
#            B
#            C
#            A


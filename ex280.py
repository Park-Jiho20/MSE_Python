#!/usr/bin/env python
# coding: utf-8

# In[5]:


# 계좌번호를 랜덤하게 생성하기위해 random을 불러온다.
import random

# Account 클래스를 생성한 후 생성자를 구현한다.
# 생성자에서는 예금주와 초기 잔액만 입력 받는다.
# 은행이름은 SC은행으로 계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성된다.
class Account:
    # class variable
    account_count = 0

    def __init__(self, name, balance):
        self.deposit_count = 0
        # 입출금 내역을 기록하기위해 빈 리스트를 만든다.
        self.deposit_log = []
        self.withdraw_log = []

        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        # 3-2-6
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        Account.account_count += 1

# Account 클래스에 입금을 위한 deposit 메서드를 추가한다.
# 입금은 최소 1원 이상만 가능하다.
    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  # Account.account_count

    def deposit(self, amount):
        if amount >= 1:
            # 입금이 될 때마다 입금액을 입금내역 리스트에 추가해준다.
            self.deposit_log.append(amount)
            self.balance += amount

# 입금 횟수가 5회가 될 때 잔고를 기준으로 1%의 이자가 잔고에 추가되도록 한다.
            self.deposit_count += 1
            if self.deposit_count % 5 == 0:         # 5, 10, 15
                # 이자 지금
                self.balance = (self.balance * 1.01)

                
# Account 클래스에 출금을 위한 withdraw 메서드를 추가한다.
# 출금은 계좌의 잔고 이상으로 출금할 수는 없다.
    def withdraw(self, amount):
        if self.balance > amount:
            # 출금이 될 때마다 출금액을 출금내역 리스트에 추가해준다.
            self.withdraw_log.append(amount)
            self.balance -= amount

# Account 인스턴스에 저장된 정보를 출력하는 display_info() 메서드를 추가한다.
# 잔고는 세자리마다 쉼표를 출력한다.
    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

# 입금과 출금 내역이 기록되도록 코드를 업데이트한다.
# 입금 내역과 출금 내역을 출력하는 deposit_history와 withdraw_history 메서드를 추가한다.
# for문을 사용하여 입금, 출금내역 리스트에 있는 값들을 하나씩 출력하도록 한다.
    def withdraw_history(self):
        for amount in self.withdraw_log:
            print(amount)

    def deposit_history(self):
        for amount in self.deposit_log:
            print(amount)


# 계좌의 이름과 초기 금액을 설정.
k = Account("Kim", 1000)
# 계좌에 입금한다.
k.deposit(100)
k.deposit(200)
k.deposit(300)
# 계좌의 입금내역을 출력한다.
k.deposit_history()

# 계좌에서 출금한다.
k.withdraw(100)
k.withdraw(200)
# 계좌의 출금내역을 출력한다.
k.withdraw_history()


# 실행결과 : 
# 100
# 200
# 300
# 100
# 200


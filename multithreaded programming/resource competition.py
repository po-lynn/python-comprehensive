import time
from concurrent.futures import ThreadPoolExecutor

class Account(object):
    """Bank Account"""

    def __init__(self):
        self.balance = 0.0

    def deposit(self, money):
        """save money"""
        new_balance = self.balance + money
        time.sleep(0.01)
        self.balance = new_balance

def main():
    """main function"""
    account = Account()
    with ThreadPoolExecutor(max_workers=16) as pool:
        for _ in range(100):
            pool.submit(account.deposit, 1)
    print(account.balance)

if __name__ == '__main__':
    main()

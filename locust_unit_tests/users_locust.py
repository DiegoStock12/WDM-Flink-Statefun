import random
from typing import List

from locust import HttpLocust, TaskSet, TaskSequence, seq_task, between

# all the endpoints are in the same flask instance
ORDER_URL = PAYMENT_URL = STOCK_URL = USER_URL = "http://192.168.99.100:5000"

def create_user(self):
    response = self.client.post(f"{USER_URL}/users/create", name="/users/create/")
    self.user_id = response.json()['user_id']

def add_balance_to_user(self):
    balance_to_add = random.randint(10000, 100000)
    self.client.post(f"{USER_URL}/users/credit/add/{self.user_id}/{balance_to_add}",
                     name="/users/credit/add/[user_id]/[amount]")

class LoadTest1(TaskSequence):
    @seq_task(1)
    def user_creates_account(self): create_item(self)

    @seq_task(2)
    def user_adds_balance(self): add_balance_to_user(self)

class LoadTests(TaskSet):
    # [TaskSequence]: [weight of the TaskSequence]
    tasks = {
        LoadTest1: 100,
    }

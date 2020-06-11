import random
from typing import List

from locust import HttpLocust, TaskSet, TaskSequence, seq_task, between

# all the endpoints are in the same flask instance
ORDER_URL = PAYMENT_URL = STOCK_URL = USER_URL = "http://192.168.99.100:5000"

def create_order(self):
    response = self.client.post(f"{ORDER_URL}/orders/create/{self.user_id}", name="/orders/create/[user_id]")
    self.order_id = response.json()['order_id']

class LoadTest1(TaskSequence):
    @seq_task(1)
    def user_creates_order(self): create_order(self)

class LoadTests(TaskSet):
    # [TaskSequence]: [weight of the TaskSequence]
    tasks = {
        LoadTest1: 100,
    }

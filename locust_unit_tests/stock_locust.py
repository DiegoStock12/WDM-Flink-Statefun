import random
from typing import List

from locust import HttpLocust, TaskSet, TaskSequence, seq_task, between

# all the endpoints are in the same flask instance
ORDER_URL = PAYMENT_URL = STOCK_URL = USER_URL = "http://192.168.99.100:5000"

def create_item(self):
    price = random.randint(1, 10)
    response = self.client.post(f"{STOCK_URL}/stock/item/create/{price}", name="/stock/item/create/[price]")
    self.item_ids.append(response.json()['item_id'])

def add_stock(self, item_idx: int):
    stock_to_add = random.randint(100, 1000)
    self.client.post(f"{STOCK_URL}/stock/add/{self.item_ids[item_idx]}/{stock_to_add}",
                     name="/stock/add/[item_id]/[number]")

class LoadTest1(TaskSequence):
    """
    Scenario where a stock admin creates an item and adds stock to it
    """
    item_ids: List[str]

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.item_ids = list()

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        self.item_ids = list()

    @seq_task(1)
    def admin_creates_item(self): create_item(self)

    @seq_task(2)
    def admin_adds_stock_to_item(self): add_stock(self, 0)

class LoadTests(TaskSet):
    # [TaskSequence]: [weight of the TaskSequence]
    tasks = {
        LoadTest1: 100,
    }

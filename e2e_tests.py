import requests

API_BASE = "http://localhost:5000"

user_ids = []

def user_create():
    return requests.post(API_BASE + '/users/create')

def user_remove(user_id):
    return requests.delete(API_BASE + '/users/remove/' + user_id)

def user_find(user_id):
    return requests.get(API_BASE + '/users/find/' + user_id)

def user_credit(user_id):
    return requests.get(API_BASE + '/users/credit/' + user_id)

def user_credit_subtract(user_id, amount):
    return requests.post(API_BASE + '/users/subtract/' + user_id + '/' + amount)

def user_credit_add(user_id, amount):
    return requests.post(API_BASE + '/users/add/' + user_id + '/' + amount)

def test_user_happy_flow():
    # Test if we a digit user_id back
    response = user_create()
    user_id = response.text
    assert user_id.isdigit()

    response = user_find(user_id)




# def test_create_100_users():
#     for _ in range(100):
#         response = user_create()
#         user_ids.append(response.text)
#     print(user_ids)

import requests

API_BASE = "http://localhost:5000"

user_ids = []

def user_create():
    return requests.post(API_BASE + '/users/create')

def user_remove(user_id):
    return requests.delete(API_BASE + '/users/remove/' + str(user_id))

def user_find(user_id):
    return requests.get(API_BASE + '/users/find/' + str(user_id))

def user_credit(user_id):
    return requests.get(API_BASE + '/users/credit/' + str(user_id))

def user_credit_subtract(user_id, amount):
    return requests.post(API_BASE + '/users/credit/subtract/' + str(user_id) + '/' + str(amount))

def user_credit_add(user_id, amount):
    return requests.post(API_BASE + '/users/credit/add/' + str(user_id) + '/' + str(amount))

def test_user_happy_flow():
    # USER CREATE
    # New user is created, response is non-empty
    data = user_create().json()
    user_id = data['id']
    assert user_id is not ''

    # USER FIND
    # Test if user exists and has 0 credit
    data = user_find(user_id).json()
    # user_id is the same as the one we requested the data for
    assert data['id'] == user_id
    # initially the user has 0 credit
    assert data['credit'] == 0

    # USER CREDIT
    # Test if credit function also returns 0 credit
    assert user_credit(user_id).json()['credit'] == 0

    # USER CREDIT ADD
    # Add 1 credit, response should indicate success (200)
    assert user_credit_add(user_id, 1).status_code == 200

    # USER CREDIT SUBTRACT
    # Subtract 1 credit, response should indicate success (200)
    assert user_credit_subtract(user_id, 1).status_code == 200

    # USER REMOVE
    assert user_remove(user_id).status_code == 200

def test_user_not_existing():
    # user_id = -1 does not exists, should error
    assert user_find(-1).status_code == 404
    assert user_credit(-1).status_code == 404
    assert user_credit_add(-1, 1).status_code == 404
    assert user_credit_subtract(-1, 1).status_code == 404
    assert user_remove(-1).status_code == 404

def test_credit_amount_negative():
    user_id = user_create().json()['id']
    assert user_credit_add(user_id, -1).status_code == 404
    assert user_credit_subtract(user_id, -1).status_code == 404

def test_credit_negative_balance():
    user_id = user_create().json()['id']
    assert user_credit_subtract(user_id, 1).status_code == 404

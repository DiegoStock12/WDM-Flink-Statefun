import requests

URL = "http://localhost:5000"

def user_create():
    return requests.post(URL + '/users/create')

def user_remove(user_id):
    return requests.delete(URL + '/users/remove/' + str(user_id))

def user_find(user_id):
    return requests.get(URL + '/users/find/' + str(user_id))

def user_credit_subtract(user_id, amount):
    return requests.post(URL + '/users/credit/subtract/' + str(user_id) + '/' + str(amount))

def user_credit_add(user_id, amount):
    return requests.post(URL + '/users/credit/add/' + str(user_id) + '/' + str(amount))

def test_user_basic():
    # USER CREATE
    # New user is created, response is non-empty
    user = user_create().json()
    assert 'user_id' in user
    assert user['user_id'] is not ''

    # USER FIND
    # Test if user exists and has 0 credit
    data = user_find(user['user_id']).json()
    # user_id is the same as the one we requested the data for
    assert data['user_id'] == user['user_id']
    # initially the user has 0 credit
    assert data['credit'] == 0

    user_id = user['user_id']

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
    assert user_find(-1).status_code == 500
    assert user_credit_add(-1, 1).status_code == 500
    assert user_credit_add(-1, 1).status_code == 500
    assert user_credit_subtract(-1, 1).status_code == 500
    assert user_remove(-1).status_code == 500

# DISCUSS WITH DIEGO
# def test_credit_amount_negative():
#     user_id = user_create().json()['user_id']
#     assert user_credit_add(user_id, -1).status_code == 404
#     assert user_credit_subtract(user_id, -1).status_code == 404

# def test_credit_negative_balance():
#     user_id = user_create().json()['user_id']
#     assert user_credit_subtract(user_id, 1).status_code == 404


def order_create(user_id):
    return requests.post(URL + '/orders/create/' + str(user_id))

def order_remove(order_id):
    return requests.delete(URL + '/orders/remove/' + str(order_id))

def order_find(order_id):
    return requests.get(URL + '/orders/find/' + str(order_id))

def order_add_item(order_id, item_id):
    return requests.post(URL + '/orders/addItem/' + str(order_id) + '/' + str(item_id))

def order_remove_item(order_id, item_id):
    return requests.delete(URL + '/orders/removeItem/' + str(order_id) + '/' + str(item_id))

def order_checkout(order_id):
    return requests.post(URL + '/order/checkout/' + str(order_id))

def test_orders_basic():
    # Create a user
    user_id = user_create().json()['user_id']

    # Create an order for this user
    order = order_create(user_id).json()
    assert 'order_id' in order
    order_id = order['order_id']
    assert order_id is not ''

    # Check if everything is properly initialized
    order = order_find(order['order_id']).json()
    assert order['order_id'] == order_id
    assert order['paid'] == 'false'
    assert order['items'] == []
    assert order['user_id'] == user_id
    assert order['total_cost'] == 0

    # Remove the order
    assert order_remove(order_id).status_code == 200

    # Non-existing user
    assert order_create(-1).status_code == 404
    # Non-existing order
    assert order_find(-1).status_code == 404
    assert order_remove(-1).status_code == 404

def stock_item_find(item_id):
    return requests.get(URL + '/stock/find/' + str(item_id))

def stock_item_subtract(item_id, amount):
    return requests.post(URL + '/stock/subtract/' + str(item_id) + '/' + str(amount))

def stock_item_add(item_id, amount):
    return requests.post(URL + '/stock/add/' + str(item_id) + '/' + str(amount))

def stock_item_create(price):
    return requests.post(URL + '/stock/create/' + str(price))


def test_stock_basic():
    # Create an item
    ITEM_PRICE = 1
    item = stock_item_create(ITEM_PRICE).json()
    item_id = item['item_id']
    assert 'item_id' in item
    assert item_id is not ''

    item = stock_item_find(item_id).json()
    assert item['stock'] == 0
    assert item['price'] == ITEM_PRICE

    assert stock_item_add(item_id, 1).status_code == 200
    assert stock_item_find(item_id).json()['stock'] == 1
    assert stock_item_subtract(item_id, 1).status_code == 200
    assert stock_item_find(item_id).json()['stock'] == 0
    assert stock_item_subtract(item_id, 1).status_code == 404

def payment_cancel(user_id, order_id):
    return requests.post(URL + '/payment/cancel/' + user_id + '/' + order_id)

def payment_status(order_id):
    return requests.get(URL + '/payment/status/' + order_id)

def test_integration():
    user_id = user_create().json()['user_id']
    assert user_credit_add(user_id, 1) == 200

    order_id = order_create(user_id).json()['order_id']
    item_id = stock_item_create().json()['item_id']
    assert stock_item_add(item_id, 1).status_code == 200
    assert order_add_item(order_id, item_id).status_code == 200
    assert order_find(order_id).json()['total_cost'] == 1
    assert stock_item_find(item_id).json()['stock'] == 0
    assert order_checkout(order_id).status_code == 200

    assert order_find(order_id).json()['paid'] == 'true'
    assert user_find(user_id).json()['credit'] == 0
    assert payment_status(order_id).json()['paid'] == 'true'

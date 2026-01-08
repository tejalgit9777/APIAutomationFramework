def create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload


def post_payload():
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def put_payload():
    payload = {
        "firstname": "James",
        "lastname": "Mackwan",
        "totalprice": 116,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-07",
            "checkout": "2019-01-07"
        },
        "additionalneeds": "Dinner"
    }
    return payload


def patch_payload():
    payload = {
        "firstname": "James",
        "lastname": "Brown",
    }
    return payload



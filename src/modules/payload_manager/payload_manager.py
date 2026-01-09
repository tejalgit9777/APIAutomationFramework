def create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload


def post_payload():
    payload = {
        "firstname": "Sheryl",
        "lastname": "Brown",
        "totalprice": 121,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-05",
            "checkout": "2019-01-05"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def put_payload():
    payload = {
        "firstname": "Monil",
        "lastname": "Mackwan",
        "totalprice": 176,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-08",
            "checkout": "2019-01-08"
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



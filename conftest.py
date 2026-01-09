import logging
from logging import Logger
import pytest
import allure
import requests

from src.modules.verifications.common_verification import verify_status_code
from src.modules.wrapper.api_requests_wrapper import put_request, post_request, get_booking_request2
from src.endpoints.api_constants import APIConstants
from src.utils.utils import Utils
from src.modules.payload_manager.payload_manager import create_token, put_payload, post_payload


# class TestUpdateBooking:
@pytest.fixture(scope="session")
def test_get_token():
    #logs= logging.getLogger(__name__)
    #logs.info("started....")
    token_response = post_request(
        url=APIConstants().get_token(),
        auth=None,
        headers=Utils().create_headers_json(),
        payload=create_token(),
        in_json=False
    )
    #logs.info("Ended!..")
    token = token_response.json()["token"]
    print("Token: ", token)
    return token


@pytest.fixture(scope="session")
#@allure.title("Create Booking")
def test_create_booking_1():
    response_create_booking = post_request(
        url=APIConstants().create_booking(),
        auth=None,
        headers=Utils().create_headers_json(),
        payload=post_payload(),
        in_json=False
    )
    verify_status_code(response_status_code=response_create_booking.status_code, expected_code=200)
    #print(response_create_booking.text)
    booking = response_create_booking.json()["bookingid"]
    print("\n")
    print("Booking Id: ", booking)
    return booking

'''
- Create Booking
- Verify booking
- Update Booking
- Delete Booking
'''
from http.client import responses

import pytest
import allure
import requests
from src.modules.wrapper.api_requests_wrapper import delete_request, post_request, put_request, get_request, get_booking_request2
from src.endpoints.api_constants import APIConstants
from src.modules.payload_manager.payload_manager import create_token, put_payload, post_payload
from src.utils.utils import Utils
from src.modules.verifications.common_verification import verify_status_code

#@pytest.mark.usefixtures("test_get_token")
class TestEndToEnd:

    @pytest.mark.createbooking
    @allure.title("Create Booking")
    def test_create_booking_1(self):
        responses = post_request(
            url=APIConstants().create_booking(),
            auth=None,
            headers=Utils().create_headers_json(),
            payload=post_payload(),
            in_json=False
        )
        verify_status_code(response_status_code=responses.status_code,expected_code=200)
        print(responses.text)
        booking = responses.json()["bookingid"]
        print("\n")
        print("Booking Id: ", booking)
        return booking


    @pytest.mark.getbooking
    @allure.title("Get Booking")
    def test_get_booking_1(self):
        response_get_booking = get_booking_request2(
            url=APIConstants().get_booking_ID(12)
        )
        verify_status_code(response_status_code=response_get_booking,expected_code=200)
        print(response_get_booking)


# @allure.title("Update Booking")
# def test_update_booking_1(self):

# @allure.title("Delete Booking")
# def test_delete_booking_1(self):

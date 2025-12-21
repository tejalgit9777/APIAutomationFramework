import pytest
import allure
import requests
from src.modules.wrapper.api_requests_wrapper import post_request
from src.endpoints.api_constants import APIConstants
from src.utils.utils import Utils
from src.modules.payload_manager.payload_manager import post_payload
from src.modules.verifications.common_verification import *


class TestCreateBooking:

    @pytest.mark.Positive
    @allure.title("Create Booking positive test case")
    def test_create_booking_TC1(self):
        response = post_request(
            url=APIConstants().create_booking(),
            auth=None,
            headers=Utils().create_headers_json(),
            payload=post_payload(),
            in_json=False
        )
        verify_status_code(response_status_code=response.status_code, expected_code=200)
        verify_json_key_for_not_null(response.json()["bookingid"])

    @pytest.mark.Negative
    @allure.title("Create Booking negative test case")
    def test_create_booking_TC2(self):
        response = post_request(
            url=APIConstants().create_booking(),
            auth=None,
            headers=Utils().create_headers_json(),
            payload={},
            in_json=False
        )
        verify_status_code(response_status_code=response.status_code, expected_code=200)
        # verify_json_key_for_not_null(response.json()["bookingid"])

    @pytest.mark.Negative
    @allure.title("Create Booking negative test case")
    def test_create_booking_TC3(self):
        response = post_request(
            url=APIConstants().create_booking(),
            auth=None,
            headers=Utils().create_headers_json(),
            payload={"firstname": "Tejal"},
            in_json=False
        )
        verify_status_code(response_status_code=response.status_code, expected_code=500)
        # verify_json_key_for_not_null(response.json()["bookingid"])

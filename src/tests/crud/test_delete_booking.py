import pytest
import allure
import requests
from src.modules.wrapper.api_requests_wrapper import delete_request,post_request
from src.endpoints.api_constants import APIConstants
from src.utils.utils import Utils
from src.tests.crud.test_create_booking import TestCreateBooking

from src.modules.payload_manager.payload_manager import create_token, put_payload, post_payload
from src.modules.verifications.common_verification import *

@pytest.mark.usefixtures("test_get_token")
class TestDeleteBooking:

    @pytest.mark.positive
    @allure.title("Update Booking")
    @allure.description("Update Booking for particular booking id")
    def test_verify_delete_booking_TC1(self,test_get_token):
        booking_ID = TestCreateBooking().test_create_booking_TC1()
        response = delete_request(
            url=APIConstants().put_patch_delete_booking(booking_ID),
            headers=Utils().common_headers_put_patch_delete_cookie_auth(test_get_token),
        )
        print("\n")
        print("Deleted!",response.status_code)
        assert response.status_code == 201


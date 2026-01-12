import pytest
import allure
import requests
from src.modules.wrapper.api_requests_wrapper import put_request, post_request
from src.endpoints.api_constants import APIConstants
from src.utils.utils import Utils
from src.modules.payload_manager.payload_manager import create_token, put_payload
from src.modules.verifications.common_verification import *

@pytest.mark.usefixtures("test_get_token")
class TestUpdateBooking:

    @pytest.mark.positive
    @allure.title("Update Booking")
    @allure.description("Update Booking for particular booking id")
    def test_verify_update_booking_TC1(self,test_get_token):
        response = put_request(
            url=APIConstants().get_booking_ID(booking_ID=2000),
            headers=Utils().common_headers_put_patch_delete_cookie_auth(test_get_token),
            payload=put_payload(),
        )
        print(response.status_code)
        print(response.text)
        assert response.status_code == 200

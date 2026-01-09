'''
- Create Booking
- Verify booking
- Update Booking
- Delete Booking
'''
from http.client import responses
import logging
import pytest
import allure
import requests
from src.modules.wrapper.api_requests_wrapper import delete_request, post_request, put_request, get_request, get_booking_request2
from src.endpoints.api_constants import APIConstants
from src.modules.payload_manager.payload_manager import create_token, put_payload, post_payload
from src.utils.utils import Utils
from src.modules.verifications.common_verification import verify_status_code, verify_response_delete


#logs = logging.getLogger(__name__)
#@pytest.mark.usefixtures("test_get_token")
class TestEndToEnd:

    #@pytest.mark.createbooking
    # @allure.title("Create Booking")
    # def test_create_booking_1(self):
    #     response_create_booking = post_request(
    #         url=APIConstants().create_booking(),
    #         auth=None,
    #         headers=Utils().create_headers_json(),
    #         payload=post_payload(),
    #         in_json=False
    #     )
    #     verify_status_code(response_status_code=response_create_booking.status_code,expected_code=200)
    #     print(response_create_booking.text)
    #     booking = response_create_booking.json()["bookingid"]
    #     print("\n")
    #     print("Booking Id: ", booking)
    #     return booking


    #@pytest.mark.getbooking
    @allure.title("Get Booking")
    def test_get_booking_1(self,test_create_booking_1):

        #logs.info("Started!!!")
        response_get_booking = get_booking_request2(
            url=APIConstants().get_booking_ID(booking_ID=test_create_booking_1)
        )
        #logs.info("Ended!!!")
        verify_status_code(response_status_code=response_get_booking,expected_code=200)
        print(response_get_booking)
        print("\n")
        print("Booking ID: ",response_get_booking)


    @allure.title("Update Booking")
    def test_update_booking_1(self,test_get_token,test_create_booking_1):
        response_update_booking = put_request(
            url=APIConstants().put_patch_delete_booking(test_create_booking_1),
            headers=Utils().common_headers_put_patch_delete_cookie_auth(test_get_token),
            payload=put_payload()
        )
        print("\n")
        print("Booking ID: ",test_create_booking_1)
        print("After Update: ",response_update_booking.text)

    @allure.title("Delete Booking")
    def test_delete_booking_1(self,test_create_booking_1,test_get_token):
        response_delete_booking = delete_request(
            url=APIConstants().put_patch_delete_booking(test_create_booking_1),
            headers=Utils().common_headers_put_patch_delete_cookie_auth(test_get_token)
        )
        print(test_create_booking_1," Booking Deleted!")
        print(response_delete_booking.text)
import pytest
import allure
import requests
from src.modules.wrapper.api_requests_wrapper import put_request, post_request
from src.endpoints.api_constants import APIConstants
from src.utils.utils import Utils
from src.modules.payload_manager.payload_manager import create_token, put_payload
from src.modules.verifications.common_verification import *


# class TestUpdateBooking:
@pytest.fixture(scope="session")
def test_get_token():
    token_response = post_request(
        url=APIConstants().get_token(),
        auth=None,
        headers=Utils().create_headers_json(),
        payload=create_token(),
        in_json=False
    )
    token = token_response.json()["token"]
    print("Token: ",token)
    return token

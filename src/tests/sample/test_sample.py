import pytest
import requests
import allure

@allure.title("True Test Case")
@allure.description("True test case Description")
def test_true_case():
    assert True == True

@allure.title("False Test Case")
@allure.description("False test case Description")
def test_false_case():
    assert False == True
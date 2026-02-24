import json

import pytest
from playwright.sync_api import Playwright, expect, Page
# command to run the test
# pytest.exe -n 5 --html=report.html --tracing on --browser_name chrome
from page_objects.home_page import HomePage
from page_objects.login import LoginPage
from page_objects.orderDetailsPage import OrderDetailsPage
from page_objects.orderHistoryPage import OrderHistoryPage
from utils.apiBaseFramework import APIUtils

with open('data/credentials.json', ) as f:
    test_data = json.load(f)
    #print("\n", test_data)
    user_credentials_list = test_data["user_credentials"]
    #print(user_credentials_list[0])
    # print(user_credentials_list[1])


@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_api_web(playwright: Playwright, browser_instance, user_credentials):
    ## createOreder -> orderID
    api_Util = APIUtils()
    orderID = api_Util.create_order(playwright, user_credentials)
    # print(f"productID = {orderID}")
    ## verify if order is placed through API
    ##print("Verifying order ID through API")
    api_Util.validate_orderID()
    login_page = LoginPage(browser_instance)
    login_page.navigate()
    login_page.login(user_credentials['userEmail'],user_credentials['userPassword'])
    homePage = HomePage(browser_instance)
    homePage.orderPageNavigation()
    order_history_page = OrderHistoryPage(browser_instance)
    order_history_page.selectOrder(orderID)
    order_details = OrderDetailsPage(browser_instance)
    order_details.verifyOrder()
    # page.goto("https://rahulshettyacademy.com/client/")
    # page.get_by_placeholder("email@example.com").fill(user_credentials['userEmail'])
    # page.get_by_placeholder("enter your passsword").fill(user_credentials['userPassword'])
    # page.get_by_role("button", name="login").click()
    # page.get_by_role("button", name="ORDERS").click()
    #### order history page -> Check if order is present
    # row_Item = page.locator("tr").filter(has_text=orderID)
    # row_Item.get_by_role("button", name="View").click()
    # expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")


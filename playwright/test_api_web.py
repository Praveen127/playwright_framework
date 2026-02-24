from playwright.sync_api import Playwright, expect

from utils.apiBase import APIUtils


def test_e2e_api_web(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()


    ## createOreder -> orderID
    api_Util = APIUtils()
    orderID = api_Util.create_order(playwright)

    ## verify if order is placed through API
    ##print("Verifying order ID through API")
    api_Util.validate_orderID()

    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_placeholder("email@example.com").fill("pkumarv@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@123")
    page.get_by_role("button", name="login").click()
    page.get_by_role("button", name="ORDERS").click()

    #### order history page -> Check if order is present
    row_Item = page.locator("tr").filter(has_text=orderID)
    row_Item.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()



























































































from time import sleep

from playwright.sync_api import Page, Playwright, expect

from utils.apiBase import APIUtils


def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=699689081fe6115f6a9334e2")


def test_Network_1(page: Page):
    page.goto("https://rahulshettyacademy.com/client/")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.get_by_placeholder("email@example.com").fill("pkumarv@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@123")
    page.get_by_role("button", name="login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    order_page_content = page.locator(".blink_me").text_content()
    # sleep(30)
    print(order_page_content)


def test_session_storage(playwright: Playwright):
    apiutils = APIUtils()
    token = apiutils.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.add_init_script(f"window.localStorage.setItem('token', '{token}');")
    #sleep(30)
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()
    page.close()


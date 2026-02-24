from playwright.sync_api import Page

fakePayloadOrderResponse = {"data":[],"message":"No Orders"}
def intercept_response(route):
    route.fulfill(
        json = fakePayloadOrderResponse
    )


### when browser clicks on oder page api call is made to server to get the content -> the test code page.route intercept the call to server and provide the fake response to browser
####  -> browser uses the response to generate html page

def test_Network_1(page: Page):
    page.goto("https://rahulshettyacademy.com/client/")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("pkumarv@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@123")
    page.get_by_role("button", name="login").click()
    page.get_by_role("button", name="ORDERS").click()
    order_page_content = page.locator(".mt-4").text_content()
    print(order_page_content)




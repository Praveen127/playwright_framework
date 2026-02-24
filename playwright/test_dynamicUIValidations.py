import time

from playwright.sync_api import Page, Playwright, expect


def test_coreLocators(playwright: Playwright,):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("stud")
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    iphone = page.locator("app-card").filter(has_text="iphone X")
    iphone.get_by_role("button").click()
    nokia = page.locator("app-card").filter(has_text="Nokia Edge")
    nokia.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)


    time.sleep(10)
    page.close()

def test_childpageValidation(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    with page.expect_popup() as pageInfo:
        page.locator(".blinkingText").click()
        childpage = pageInfo.value
        text = childpage.locator(".red").text_content()
        print(text)
        list1 = text.split((" "))
        for word in list1:
            if word == 'mentor@rahulshettyacademy.com':
                assert word == "mentor@rahulshettyacademy.com"
                





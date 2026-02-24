from playwright.sync_api import Playwright


def test_firefox_browser(playwright: Playwright):
    firefoxBowser = playwright.firefox.launch(headless=True)
    # firefoxBowser = playwright.firefox.launch(headless=False)
    print("Launched")
    context = firefoxBowser.new_context()
    print("Context created")
    page = context.new_page()
    page.close()
    context.close()
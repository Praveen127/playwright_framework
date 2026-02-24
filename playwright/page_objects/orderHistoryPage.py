from playwright.sync_api import expect


class OrderHistoryPage:
    def __init__(self, page):
        self.page = page

    def selectOrder(self, orderID):
        row_Item = self.page.locator("tr").filter(has_text=orderID)
        row_Item.get_by_role("button", name="View").click()

class HomePage:
    def __init__(self, page):
        self.page = page

    def orderPageNavigation(self):
        self.page.get_by_role("button", name="ORDERS").click()




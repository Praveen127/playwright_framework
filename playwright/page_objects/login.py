class LoginPage:
    def __init__(self, page):
        self.page = page



    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client/")

    def login(self, userEmal, userPassword):
        self.page.get_by_placeholder("email@example.com").fill(userEmal)
        self.page.get_by_placeholder("enter your passsword").fill(userPassword)
        self.page.get_by_role("button", name="login").click()

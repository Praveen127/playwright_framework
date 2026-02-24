from playwright.sync_api import Playwright

oreder_palylod = {"orders": [{"country": "India", "productOrderedId": "6960eac0c941646b7a8b3e68"}]}
orderID_payload = "id=6995b0a01fe6115f6a916d82"


class APIUtils:

    def __init__(self):
        self.gplaywright = None
        self.gtoken = None
        self.order_ID = None

    def getToken(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
        response = api_request_context.post("api/ecom/auth/login",
                                            data={"userEmail": "pkumarv@gmail.com", "userPassword": "Iamking@123"}
                                            )
        assert response.ok
        #print("login :")
        #print("login :", response.json())
        responseBody = response.json()
        token = responseBody["token"]
        self.gplaywright = playwright
        self.gtoken = token
        return token

    def create_order(self, playwright: Playwright):
        token = self.getToken(playwright)
        #print(" token :")
        #print(token)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
        response = api_request_context.post("api/ecom/order/create-order",
                                            data=oreder_palylod,
                                            headers={"Authorization": token,
                                                     "Content-Type": "application/json"
                                                     }
                                            )
        assert response.ok
        #print("Create Order :", response.json())
        response_body = response.json()
        order_ID = response_body['orders'][0]
        self.order_ID = order_ID
        self.validate_orderID()
        return order_ID

    def validate_orderID(self):
        token = self.gtoken
        url = f"/api/ecom/order/get-orders-details?id={self.order_ID}"
        headers = {"Authorization": token,
                   "Accept": "application/json, text/plain, */*"
                   }
        #print(" token :")
        #print(token)
        api_request_context = self.gplaywright.request.new_context(base_url="https://rahulshettyacademy.com/client")
        response = api_request_context.get(url, headers=headers)
        #print(response.json())
        assert response.ok
        return True

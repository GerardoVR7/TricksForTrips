from fastapi import APIRouter, Request
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
import os
from paypalcheckoutsdk.orders import OrdersCreateRequest
from fastapi.responses import JSONResponse
import requests
payment_routes = APIRouter()


# Creating Access Token for Sandbox
client_id = os.environ["PAYPAL_CLIENT_ID"]
client_secret = os.environ["PAYPAL_SECRET"]

# Creating an environment
environment = SandboxEnvironment(
    client_id=client_id, client_secret=client_secret)
client = PayPalHttpClient(environment)

@payment_routes.post("/create-order", tags=["Paypal"])
async def create_order_paypal(request: Request):
    try:
        data = await request.json()
        request = OrdersCreateRequest()
        print(data)
        request.prefer('return=representation')
        request.request_body(
            {
                "intent": "CAPTURE",
                "purchase_units": [
                    {       
                        "amount": {
                            "currency_code": "USD",
                            "value": "100.00"
                        }
                    }
                ],
                "items": data
            }
        )
        response = client.execute(request)
        return JSONResponse(content={"id": response.result.id})
    except IOError:
        print(IOError)
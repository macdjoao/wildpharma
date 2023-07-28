from ninja import NinjaAPI
from customers.api import router as customers_router

api = NinjaAPI()

api.add_router('/customers/', customers_router)

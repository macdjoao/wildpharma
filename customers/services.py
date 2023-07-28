# Seguir nomenclatura CRUD

from customers.models import Customer
from django.shortcuts import get_object_or_404, get_list_or_404
from datetime import datetime


class CustomerService:

    @staticmethod
    def create(data: dict):
        customer = Customer.objects.create(**data.dict())
        return get_object_or_404(Customer, id=customer.id)

    @staticmethod
    def read_one(id: int):
        customer = get_object_or_404(Customer, id=id, active=True)
        return customer

    @staticmethod
    def read_many():
        customers = get_list_or_404(Customer, active=True)
        return customers

    # TODO
    @staticmethod
    def update(id: int, data: dict):
        customer = get_object_or_404(Customer, id=id)
        for attr, value in data.dict().items():
            setattr(customer, attr, value)
        customer.save()
        return get_object_or_404(Customer, id=id)

    # Delete lógico
    @staticmethod
    def delete(id: int):
        customer = get_object_or_404(Customer, id=id)
        customer.active = False
        customer.deleted_at = datetime.now()
        customer.save()
        return get_object_or_404(Customer, id=id)

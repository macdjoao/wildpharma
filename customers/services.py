# Seguir nomenclatura CRUD

from customers.models import Customer
from django.shortcuts import get_object_or_404, get_list_or_404


class CustomerService:

    # TODO
    @staticmethod
    def create(data: dict):
        return 'Create CustomerService'

    @staticmethod
    def read_one(id: int):
        customer = get_object_or_404(Customer, id=id)
        return customer

    # TODO
    @staticmethod
    def read_many():
        customers = get_list_or_404(Customer)
        return customers

    # TODO
    @staticmethod
    def update(id: int, data: dict):
        return 'Update CustomerService'

    # TODO
    @staticmethod
    def delete(id: int):
        return 'Delete CustomerService'

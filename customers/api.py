# Seguir nomenclatura HTTP

from ninja import Router
from customers.schemas import PostCustomer, GetOneCustomer, PatchCustomer
from customers.services import CustomerService
from typing import List

router = Router(tags=['Customers'])


@router.post('/', response=GetOneCustomer)
def post_customer(request, payload: PostCustomer):
    return CustomerService.create(data=payload)


@router.get('/', response=List[GetOneCustomer])
def get_many_customers(request):
    return CustomerService.read_many()


@router.get('/{customer_id}', response=GetOneCustomer)
def get_one_customer(request, customer_id: int):
    return CustomerService.read_one(id=customer_id)


@router.patch('/{customer_id}', response=GetOneCustomer)
def patch_customer(request, customer_id: int, payload: PatchCustomer):
    return CustomerService.update(id=customer_id, data=payload)


@router.delete('/{customer_id}', response=GetOneCustomer)
def delete_customer(request, customer_id: int):
    return CustomerService.delete(id=customer_id)

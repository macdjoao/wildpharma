# Seguir nomenclatura HTTP

from ninja import Router
from customers.schemas import PostCustomerSchema, GetCustomerSchema, PatchCustomerSchema
from customers.services import CustomerService
from typing import List
from ninja.pagination import paginate, LimitOffsetPagination

router = Router(tags=['Customers'])


@router.post('/', summary='Create customer', response={201: GetCustomerSchema})
def post_customer(request, payload: PostCustomerSchema):
    return CustomerService.create(data=payload)


@router.get('/{customer_id}/{active}', summary='Get one customer', response={200: GetCustomerSchema})
def get_one_customer(request, customer_id: int, active: bool):
    return CustomerService.read_one(id=customer_id, active=active)


@router.get('/{active}', summary='Get all customers', response={200: List[GetCustomerSchema]})
@paginate(LimitOffsetPagination)
def get_many_customers(request, active: bool):
    return CustomerService.read_many(active=active)


@router.patch('/{customer_id}', summary='Update customer', response={200: GetCustomerSchema})
def patch_customer(request, customer_id: int, payload: PatchCustomerSchema):
    return CustomerService.update(id=customer_id, data=payload)


@router.delete('/{customer_id}', summary='Delete customer', response={204: GetCustomerSchema})
def delete_customer(request, customer_id: int):
    # TODO
    return CustomerService.delete(id=customer_id)

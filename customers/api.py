# Seguir nomenclatura HTTP

from ninja import Router
from customers.schemas import PostCustomer, GetOneCustomer, GetManyCustomers, PatchCustomer
from customers.services import CustomerService

router = Router(tags=['Customers'])


@router.post('/', response=GetOneCustomer)
def post_customer(request, payload: PostCustomer):
    # TODO
    return 'Post Customer'


@router.get('/', response=GetManyCustomers)
def get_many_customers(request):
    return CustomerService.read_many()


@router.get('/{customer_id}', response=GetOneCustomer)
def get_one_customer(request, customer_id: int):
    return CustomerService.read_one(id=customer_id)


@router.patch('/{customer_id}', response=GetOneCustomer)
def patch_customer(request, customer_id: int, payload: PatchCustomer):
    # TODO
    return 'Patch Customer'


@router.delete('/{customer_id}', response=GetOneCustomer)
def delete_customer(request, customer_id: int):
    # TODO
    return 'Delete Customer'

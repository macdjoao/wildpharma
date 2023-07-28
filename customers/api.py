# Seguir nomenclatura HTTP

from ninja import Router
from customers.schemas import PostCustomerSchema, GetOneCustomerSchema, GetManyCustomersSchema, PatchCustomerSchema

router = Router(tags=['Customers'])


@router.post('/', response=GetOneCustomerSchema)
def post(request, body: PostCustomerSchema):
    # TODO
    return 'Post Customer'


@router.get('/', response=GetManyCustomersSchema)
def get_many(request):
    # TODO
    return 'Get Many Customers'


@router.get('/{customer_id}', response=GetOneCustomerSchema)
def get_one(request, customer_id):
    # TODO
    return 'Get One Customer'


@router.patch('/{customer_id}', response=GetOneCustomerSchema)
def patch(request, customer_id, body: PatchCustomerSchema):
    # TODO
    return 'Patch Customer'


@router.delete('/{customer_id}', response=GetOneCustomerSchema)
def delete(request, customer_id):
    # TODO
    return 'Delete Customer'

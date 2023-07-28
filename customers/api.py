# Seguir nomenclatura HTTP

from ninja import Router

router = Router(tags=['Customers'])


@router.post('/')
def post(request):
    # TODO
    return 'Post Customer'


@router.get('/')
def get_many(request):
    # TODO
    return 'Get Many Customers'


@router.get('/{customer_id}')
def get_one(request, customer_id):
    # TODO
    return 'Get One Customer'


@router.patch('/{customer_id}')
def patch(request, customer_id):
    # TODO
    return 'Patch Customer'


@router.delete('/{customer_id}')
def delete(request, customer_id):
    # TODO
    return 'Delete Customer'

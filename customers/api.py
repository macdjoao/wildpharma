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
def get_one(request):
    # TODO
    return 'Get One Customer'


@router.patch('/{customer_id}')
def patch(request):
    # TODO
    return 'Patch Customer'


@router.delete('/{customer_id}')
def delete(request):
    # TODO
    return 'Delete Customer'

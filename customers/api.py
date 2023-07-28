from ninja import Router

router = Router(tags=['Customers'])


@router.get('/')
def hello_world(request):
    return 'Olá mundo'

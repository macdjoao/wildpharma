# Seguir nomenclatura HTTP
# Por questões de segurança, usamos ModelSchema em vez de create_schema ( https://django-ninja.rest-framework.com/guides/response/django-pydantic-create-schema/ )

from ninja import ModelSchema
from customers.models import Customer


class PostCustomerSchema(ModelSchema):
    class Config:
        model = Customer
        model_fields = ['first_name', 'last_name', 'email', 'phone']


class GetCustomerSchema(ModelSchema):
    class Config:
        model = Customer
        model_fields = ['id', 'first_name', 'last_name',
                        'email', 'phone', 'active', 'created_at', 'updated_at', 'deleted_at']


class PatchCustomerSchema(ModelSchema):
    class Config:
        model = Customer
        model_exclude = ['id', 'active',
                         'created_at', 'updated_at', 'deleted_at']
        model_fields_optional = ['first_name', 'last_name', 'email', 'phone']

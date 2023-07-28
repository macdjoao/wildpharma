# Seguir nomenclatura HTTP
# Por questões de segurança, usarei ModelSchema e Schema em vez de create_schema ( https://django-ninja.rest-framework.com/guides/response/django-pydantic-create-schema/ )

from ninja import Schema
from datetime import datetime
from typing import List, Optional


class PostCustomerSchema(Schema):
    first_name: str
    last_name: str
    email: str
    phone: str


class GetOneCustomerSchema(Schema):
    id: int
    first_name: str
    last_name: str
    email: str
    phone: str
    active: bool
    created_at: datetime
    updated_at: datetime = None
    deleted_at: datetime = None


class GetManyCustomersSchema(Schema):
    customers: List[GetOneCustomerSchema]


class PatchCustomerSchema(Schema):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    phone: Optional[str]

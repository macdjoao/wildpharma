# Seguir nomenclatura HTTP
# Por questões de segurança, Schema em vez de create_schema ( https://django-ninja.rest-framework.com/guides/response/django-pydantic-create-schema/ )

from ninja import Schema
from datetime import datetime
from typing import List, Optional


class PostCustomer(Schema):
    first_name: str
    last_name: str
    email: str
    phone: str


class GetOneCustomer(Schema):
    id: int
    first_name: str
    last_name: str
    email: str
    phone: str
    active: bool
    created_at: datetime
    updated_at: datetime = None
    deleted_at: datetime = None


class GetManyCustomers(Schema):
    customers: List[GetOneCustomer]


class PatchCustomer(Schema):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    phone: Optional[str]

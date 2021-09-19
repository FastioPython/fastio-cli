from pydantic import BaseModel
from typing import List, Optional

RELATIONS = {
    '1-1': 'has_one',
    '1-n': 'has_many',
    'n-n': 'belongs_to_many',
    'n-1': 'belongs_to',
}


class ModelRelation(BaseModel):
    name: str = ''
    key: str = ''
    func: str = ''


class ModelField(BaseModel):
    name: str = None
    datatype: str = None
    type_hint: str = 'str'
    default: str = None
    required: bool = False
    description: str = None
    relations: List[ModelRelation]


class Model(BaseModel):
    name: str = ''
    fields: List[ModelField] = []
    filename: str = ''
    class_name: str = ''


class ApiSchemas(BaseModel):
    items: List[Model]


class ApiRequestItem(BaseModel):
    name: str = None
    query_in: str = None
    datatype: str = None
    type_hint: str = None
    default: str = None
    required: bool = False
    description: str = None


class ApiResponseItem(BaseModel):
    code: str = None
    message: str = None


class Api(BaseModel):
    url: str = None
    method: str = None
    summary: str = None
    description: str = None
    operationId: str = None
    requests: List[ApiRequestItem] = []
    responses: List[ApiResponseItem] = []


class Apis(BaseModel):
    items: List[Api]


class ProjectConfig(BaseModel):
    router_admin_dir: str
    api_admin_dir: str
    router_client_dir: str
    api_client_dir: str
    model_dir: str
    migration_dir: str
    seeder_dir: str
    repository_dir: str
    request_model_dir: str
    response_model_dir: str
    test_api_admin_dir: str
    test_api_client_dir: str


class TemplateConfig(BaseModel):
    name: str = None
    root_path: str = None

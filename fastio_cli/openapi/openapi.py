import json
from fastio_cli.github import Github
from fastio_cli.utils import camel_to_snake, dict_first_key
from fastio_cli.openapi.models import (
    Apis, Api, ApiResponseItem, ApiRequestItem, ApiSchemas,
    Model, ModelField
)
from fastio_cli.templates import StandardTemplate

PYDANTIC_DATATYPE_MAPPING = {
    'integer': 'int',
    'string': 'str',
    'boolean': 'bool',
    'object': 'dict',
    'datetime': 'datetime',
    'date-time': 'datetime',
    'date': 'date',
    'array': 'list',
    'decimal': 'Decimal',
    'float': 'Decimal',
    'uuid': 'uuid.UUID',
}

"""
Convert open api yaml or json file to python OpenApi object
"""


class OpenApi:
    _data = None

    _apis = Apis(
        items=[]
    )

    _api_schemas = ApiSchemas(
        items=[]
    )

    TEMPLATE = ''
    TEMPLATE_NAME = ''
    PROJECT_ROOT = ''

    def __init__(self, project_root: str, swagger_file: str, template: str) -> None:
        self.PROJECT_ROOT = project_root
        self.load(swagger_file)
        self.use_template(template_name=template)
        self.mapping()

    def use_template(self, template_name):
        if template_name == 'starter':
            self.TEMPLATE = StandardTemplate(project_root=self.PROJECT_ROOT)
            self.TEMPLATE.set_swagger_data(self.get_data())


    def generate(self):
        # TODO: Download standard template from github
        github = Github()
        github.download_template(template_name=self.TEMPLATE_NAME, to_path=self.PROJECT_ROOT)
        print("Downloaded standard template form github")
        # TODO: Generate files from open api
        # self.TEMPLATE.generate_base_project()

    def load(self, swagger_file):
        with open(swagger_file) as json_file:
            self._data = json.load(json_file)

    """
    Return loaded swagger data as dict 
    """

    def get_loaded_data(self) -> dict:
        return self._data

    """
    Return parsed swagger api list
    """

    def get_apis(self) -> list:
        return self._apis

    def get_apis_json(self) -> str:
        return self._apis.json()

    def get_schemas(self):
        return self._api_schemas

    def get_data(self):
        return {
            'schemas': self._api_schemas,
            'apis': self._apis
        }

    def mapping(self) -> None:
        self._map_apis()
        self._map_shemas()

    def _map_apis(self) -> None:
        api_paths = self._data['paths']

        if type(api_paths) is dict:
            for k, v in api_paths.items():
                # Extract: method
                _method = dict_first_key(v)
                # Extract: summary
                _summary = api_paths.get(k).get(_method).get('summary')
                # Extract: description
                _description = api_paths.get(k).get(_method).get('description')
                # Extract: operationId
                _operation_id = api_paths.get(k).get(_method).get('operationId')

                # TODO: Extract request params
                _requests = []
                requests_params = api_paths.get(k).get(_method).get('parameters')
                if requests_params is not None:
                    if type(requests_params) is not list:
                        raise Exception("Api - Request - Params should be a List")
                    else:
                        for param in requests_params:
                            _datatype = param.get('schema').get('type')
                            _type_hint = PYDANTIC_DATATYPE_MAPPING[
                                _datatype] if _datatype in PYDANTIC_DATATYPE_MAPPING else 'str'
                            _requests.append(
                                ApiRequestItem(
                                    name=param.get('name'),
                                    query_in=param.get('in'),
                                    datatype=_datatype,
                                    type_hint=_type_hint,
                                    default=param.get('default'),
                                    required=param.get('required'),
                                    description=param.get('description'),
                                )
                            )

                # Extract: responses
                _responses = []
                responses_data = api_paths.get(k).get(_method).get('responses')
                if responses_data is not None:
                    for response_code, response_content in responses_data.items():
                        _responses.append(
                            ApiResponseItem(
                                code=response_code,
                                message=response_content.get('description')
                            )
                        )

                api = Api(
                    url=k,
                    method=_method,
                    operationId=_operation_id,
                    summary=_summary,
                    description=_description,
                    requests=_requests,
                    responses=_responses
                )

                self._apis.items.append(api)

    def _map_shemas(self) -> None:
        _schemas = self._data['components']['schemas']

        if type(_schemas) is dict:
            for _schema_name, _schema in _schemas.items():
                model = Model(
                    name=_schema_name,
                    fields=[],
                    filename=camel_to_snake(_schema_name),
                    class_name=_schema_name,
                )

                # Extract: required fields
                required_list = _schema.get('required') if _schema.get('required') else []

                # Extract: schema properties
                fields = _schema.get('properties')
                if type(fields) is dict:
                    for field_name, field in fields.items():
                        _required = True if field_name in required_list else False
                        _datatype = field.get("type")
                        _default = field.get("default")
                        _description = field.get("description")
                        _relations = field.get("relations", [])
                        _type_hint = PYDANTIC_DATATYPE_MAPPING[
                            _datatype] if _datatype in PYDANTIC_DATATYPE_MAPPING else 'str'

                        model.fields.append(
                            ModelField(
                                name=field_name,
                                datatype=_datatype,
                                type_hint=_type_hint,
                                default=_default,
                                required=_required,
                                description=_description,
                                relations=_relations,
                            )
                        )

                self._api_schemas.items.append(model)


import os 
from fastio_cli.templates.base_tmpl import BaseTmpl
from fastio_cli.openapi.models import Model

dir_path = os.path.dirname(os.path.realpath(__file__))


class TestApiTmpl(BaseTmpl):

    tmpl_file = f'{dir_path}/test_api.jinja2'
    tmpl_data: Model
    tmpl_props: dict = {
        "props": {
            "methods": ["get", "post", "put", "delete"]
        }
    }

    def __init__(self, data: Model) -> None:
        self.tmpl_data = data.dict()

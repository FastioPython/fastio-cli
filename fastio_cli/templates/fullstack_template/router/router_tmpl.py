import os 
from fastio_cli.templates.base_tmpl import BaseTmpl
from fastio_cli.openapi.models import ApiSchemas

dir_path = os.path.dirname(os.path.realpath(__file__))


class RouterTmpl(BaseTmpl):

    tmpl_file = f'{dir_path}/router.jinja2'
    tmpl_data: ApiSchemas

    def __init__(self, data: ApiSchemas) -> None:
        self.tmpl_data = data.dict()

import os 
from fastio_cli.templates.base_tmpl import BaseTmpl
from fastio_cli.openapi.models import Model

dir_path = os.path.dirname(os.path.realpath(__file__))


class RepositoryModelTmpl(BaseTmpl):

    tmpl_file = f'{dir_path}/respository_model.jinja2'
    tmpl_data: Model
    _model_data: None


    def __init__(self, data: Model) -> None:
        self._model_data = data
        self.convert_data()

    def convert_data(self):
        self.tmpl_data = self._model_data.dict()

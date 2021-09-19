import os 
from datetime import datetime
from fastio_cli.templates.base_tmpl import BaseTmpl
from fastio_cli.openapi.models import Model

dir_path = os.path.dirname(os.path.realpath(__file__))


class MigrationTmpl(BaseTmpl):

    tmpl_file = f'{dir_path}/migration.jinja2'
    tmpl_data: Model


    def __init__(self, data: Model) -> None:
        self.tmpl_data = data.dict()

    def write(self, output_file):
        output_file = self._rename_output_file(output_file=output_file)
        super().write(output_file=output_file)

    def _rename_output_file(self, output_file):
        date_formated = datetime.today().strftime('%Y_%m_%d_%H%M%S')
        filename = str(os.path.basename(output_file)).replace('migration', 'table')
        filename = f'{os.path.dirname(output_file)}/{date_formated}_create_{filename}'
        return filename

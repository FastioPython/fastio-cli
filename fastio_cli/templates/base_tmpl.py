import os
from pathlib import Path
from jinja2 import Template


class BaseTmpl:

    tmpl_file = None
    tmpl_data = None
    tmpl_props = None

    def write(self, output_file):
        try:
            output_file_path = Path(output_file)
            output_file_dir = output_file_path.parent   
                     
            if not os.path.exists(output_file_dir):
                os.makedirs(output_file_dir, exist_ok=True)

            data = self.tmpl_data

            if self.tmpl_props is not None:
                data["props"] = self.tmpl_props
                
            self._write_from_template(self.tmpl_file, output_file, self.tmpl_data)
        except Exception as e:
            raise e

    def _write_from_template(self, template_file, output_file, data):
        # 1. Get template file
        template = None
        with open(template_file, 'r', encoding='UTF-8') as file:
            template = file.read()

        # 2. Create Template object and render data to template
        jinja2_template = Template(template)
        parsed_content = jinja2_template.render(**data)

        # 3. Write file
        with open(output_file, 'w', encoding='UTF-8') as file:
            file.write(parsed_content)
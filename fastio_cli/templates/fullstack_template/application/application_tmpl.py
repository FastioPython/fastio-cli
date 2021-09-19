import os 
from shutil import copytree, ignore_patterns, rmtree
from pathlib import Path

dir_path = os.path.dirname(os.path.realpath(__file__))


class ApplicationTmpl:

    tmpl_application_root = f'{dir_path}/application_base/'

    def __init__(self) -> None:
        pass 

    def write(self, output_dir):
        try:
            if os.path.exists(output_dir):
                rmtree(output_dir)
                
            copytree(src=self.tmpl_application_root, dst=output_dir, ignore=ignore_patterns('__pycache__'))
        except Exception as e:
            raise e
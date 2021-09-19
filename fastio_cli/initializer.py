from fastio_cli.utils import write_json, read_json
from fastio_cli import __version__


class Initializer:
    FILENAME = '.fastio-cli.json'

    def __init__(self, project_root: str) -> None:
        self.PROJECT_ROOT = project_root
        self.CONFIG_FILE = f"{project_root}/{self.FILENAME}"
        self.write_config()

    def write_config(self) -> None:
        write_json(file_path=self.CONFIG_FILE, data=self.config_data())
        
    def read_config(self) -> object:
        return read_json(self.CONFIG_FILE)

    def config_data(self) -> object:
        return {
            "name": "Fastio CLI",
            "version": __version__,
            "project_root": self.PROJECT_ROOT
        }

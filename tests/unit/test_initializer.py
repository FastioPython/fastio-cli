import os

from tests.base import BaseTestCase
from fastio_cli.initializer import Initializer


class TestInitializer(BaseTestCase):

    def test_init_as_fastio_project(self):
        project_root = os.getcwd()
        initializer = Initializer(project_root=project_root)
        initializer.write_config()
        assert f"{project_root}/.fastio-cli.json" == initializer.CONFIG_FILE
        assert os.path.isfile(initializer.CONFIG_FILE)
        assert initializer.read_config() == initializer.config_data()

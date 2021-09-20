import pathlib
from shutil import rmtree
from tests.base import BaseTestCase
from fastio_cli.github import Github


class TestGithub(BaseTestCase):

    def setup_method(self, test_method):
        self.project_root = f"{self.examples_dir()}/myproject"

    def teardown_method(self, method):
        if self.path_exist(self.project_root):
            rmtree(self.project_root)

    def test_clone_template_from_github(self):
        template_name = 'standard'
        github = Github()
        github.download_template(template_name=template_name, to_path=self.project_root)
        assert True == self.path_exist(self.project_root)

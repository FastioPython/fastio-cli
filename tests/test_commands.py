import json
import subprocess

from fastio_cli.initializer import Initializer
from .base import BaseTestCase


class TestCommonCommands(BaseTestCase):

    def test_command_root(self):
        cmd = ['fastio']
        result = self.call_command(cmd)
        assert result.returncode == 0

    def test_command_init(self):
        cmd = ['fastio', 'init']
        result = self.call_command(cmd)
        assert result.returncode == 0
        assert result.stdout == 'Initialized as fastio project\n'

    def test_command_initdb(self):
        cmd = ['fastio', 'initdb']
        result = self.call_command(cmd)
        assert result.returncode == 0
        assert result.stdout == 'Initialized the database\n'

    def test_command_dropdb(self):
        cmd = ['fastio', 'dropdb']
        result = self.call_command(cmd)
        assert result.returncode == 0
        assert result.stdout == 'Dropped the database\n'

    def test_command_read_config(self):
        # Prepare: config file
        project_root = self.current_dir()
        initializer = Initializer(project_root=project_root)
        initializer.write_config()

        # Run command: fastio config --show
        cmd = ['fastio', 'config', '--show']
        result = self.call_command(cmd)
        assert result.returncode == 0
        assert json.loads(result.stdout) == initializer.read_config()


class TestOpenapiCommands(BaseTestCase):

    def test_command_openapi_help(self):
        cmd = ['fastio', 'openapi', '--help']
        result = self.call_command(cmd)
        assert result.returncode == 0

    def test_command_openapi_from_file(self):
        filename = 'academic.openapi3.json'
        filepath = f"{self.examples_dir()}/{filename}"
        assert self.path_exist(filepath)

        cmd = ['fastio', 'openapi', f'--file={filepath}']
        result = self.call_command(cmd)
        assert result.returncode == 0
        assert 'Downloaded standard template form github\n' in result.stdout
        assert 'Generated project from openapi file\n' in result.stdout


class TestGeneratorCommands(BaseTestCase):

    def test_command_generate_model(self):
        cmd = ['fastio', 'generate', 'model', 'User']
        result = self.call_command(cmd)
        assert result.returncode == 0

    def test_command_generate_request(self):
        cmd = ['fastio', 'generate', 'request', 'UserCreateRequest']
        result = self.call_command(cmd)
        assert result.returncode == 0

    def test_command_generate_resource(self):
        cmd = ['fastio', 'generate', 'resource', 'UserResource']
        result = self.call_command(cmd)
        assert result.returncode == 0

    def test_command_generate_repository(self):
        cmd = ['fastio', 'generate', 'repository', 'UserRepository']
        result = self.call_command(cmd)
        assert result.returncode == 0

    def test_command_generate_service(self):
        cmd = ['fastio', 'generate', 'service', 'UserService']
        result = self.call_command(cmd)
        assert result.returncode == 0

    def test_command_generate_test_without_type(self):
        cmd = ['fastio', 'generate', 'test', 'UserRepositoryTest']
        result = self.call_command(cmd)
        assert result.returncode == 0
        assert result.stdout == 'The flag --unit or --feature is required\n'

    def test_command_generate_test_unit(self):
        cmd = ['fastio', 'generate', 'test', 'UserRepositoryTest', '--unit']
        result = self.call_command(cmd)
        assert result.returncode == 0

    def test_command_generate_test_feature(self):
        cmd = ['fastio', 'generate', 'test', 'UserControllerTest', '--feature']
        result = self.call_command(cmd)
        assert result.returncode == 0

    def test_command_generate_event(self):
        cmd = ['fastio', 'generate', 'event', 'UserCreatedEvent']
        result = self.call_command(cmd)
        assert result.returncode == 0

import os
import subprocess

uppath = lambda _path, n: os.sep.join(_path.split(os.sep)[:-n])

class BaseTestCase:

    def call_command(self, cmd: list = []):
        # subprocess.Popen(cwd=self.examples_dir())
        subprocess.call("ls", cwd=self.examples_dir())

        result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
        return result

    def current_dir(self):
        return os.path.abspath(os.path.dirname(__file__))

    def examples_dir(self):
        path = f"{uppath(__file__, 2)}/examples"
        return path
        # raise Exception(path)

    def path_exist(self, path: str):
        return os.path.exists(path)

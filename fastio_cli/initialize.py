from fastio_cli.utils import write_json


class Initialize:

    CONF_FILE = '.fastio.json'

    def __init__(self, path: str):
        filename = f"{path}/{self.CONF_FILE}"
        write_json(file_path=filename, data=self.getConfigutation())

    def getConfigutation(self):
        return {
            "version": "0.1.0"  
        }
"""
Get template information from github
"""
import subprocess

import git


class Github:

    TEMPLATES: dict = {}

    def __init__(self):
        self.get_templates()

    def download_template(self, template_name: str, to_path: str) -> bool:
        if template_name not in self.TEMPLATES:
            return False
        else:
            template = self.TEMPLATES[template_name]
            repo = git.Repo.clone_from(url='https://github.com/FastioPython/standard',
                    to_path=to_path,
                    # 'Cookbook-https'
            )
            return True

    def find_template(self, template_name: str) -> None:
        if template_name in self.TEMPLATES:
            return self.TEMPLATES[template_name]
        return None

    def get_templates(self):
        self.TEMPLATES = {
            "standard": {
                "url": "https://github.com/FastioPython/standard",
                "latest_version": "v1.0-alpha.1",
                "versions": [
                    "v1.0-alpha.1",
                ]
            }
        }
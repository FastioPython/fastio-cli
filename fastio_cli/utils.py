import os
import json
import shutil
from pathlib import Path
import re
from jinja2 import Template


def read_json(file_path):
	with open(file_path, 'r') as file:
		return json.load(file)
	return None

def write_file(file_path, data):
	with open(file_path, 'w', encoding='UTF-8') as file:
		file.write(data)

def write_json(file_path: str, data: dict):
	with open(file_path, 'w') as outfile:
		json.dump(data, outfile)

def copy_file(source_file, dest_file):
	try:
		newPath = shutil.copy(source_file, dest_file)
	except:
		raise Exception(f"Error copy from {source_file} to {dest_file}")
	return newPath

def copy_dirs(source_dir, dest_dir):
	try:
		destination = shutil.copytree(source_dir, dest_dir)
	except Exception as e:
		raise Exception(f"Error copy from {source_dir} to {dest_dir}")

def make_dirs(folderPath):
	os.makedirs(folderPath, exist_ok=True)

def camel_to_snake(str):
	s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', str)
	return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def write_from_template(template_file, output_file, data):
	# Get template file
	template = None
	with open(template_file, 'r', encoding='UTF-8') as file:
		template = file.read()

	# Create Template object and render data to template
	jinja2_template = Template(template)
	parsed_content = jinja2_template.render(**data)

	# write file
	with open(output_file, 'w', encoding='UTF-8') as file:
		file.write(parsed_content)

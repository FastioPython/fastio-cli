app_dir=$(CURDIR)/App
db_dir=App/Database
model_dir=App/Models
env_path=App/.env

## Help
help:
	@cat makefile | grep ##. | sed '2d;s/##//;s/://'

exec:
	@docker-compose $(project) exec $(optionT) backend $$cmd


## Setup, start, stop ->
venv:
	@rm -rf ./venv-py3.7
	@virtualenv -p python3.7 venv-py3.7

install:
	@pip install -r requirements.txt

require:
	@pip install $$name

start:
	uvicorn App.app:app --reload --port 8009


## Database: migrations
model:
	orator make:model $$name -p $(model_dir)

migrate:
	orator migrate -p $(db_dir)/Migrations -c $(db_dir)/db.py

migration:
	orator make:migration $$name -p $(db_dir)/Migrations

rollback:
	orator migrate:rollback -p $(db_dir)/Migrations  -c $(db_dir)/db.py

refresh:
	orator migrate:refresh -p $(db_dir)/Migrations --seed --seed-path $(db_dir)/seeds -c $(db_dir)/db.py

# Database: seeding
seed:
	orator db:seed -p $(db_dir)/Seeds -c $(db_dir)/db.py

seed-fresh:
	orator migrate:refresh --seed 

seed-one:
	orator db:seed --seeder $$name -p $(db_dir)/Seeds



## Testing -->
test:
	python -m pytest -vv

# test-cov:
# 	python -m pytest -vv
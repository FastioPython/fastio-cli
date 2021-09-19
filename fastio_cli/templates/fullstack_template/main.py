from fastio_cli.openapi.models import Model, ApiRequestItem, TemplateConfig, ProjectConfig
from fastio_cli.templates.fullstack_template.application.application_tmpl import ApplicationTmpl
from fastio_cli.templates.fullstack_template.api.api_tmpl import ApiTmpl
from fastio_cli.templates.fullstack_template.test.test_api_tmpl import TestApiTmpl
from fastio_cli.templates.fullstack_template.router.router_tmpl import RouterTmpl
from fastio_cli.templates.fullstack_template.model.model_tmpl import ModelTmpl
from fastio_cli.templates.fullstack_template.migration.migration_tmpl import MigrationTmpl
from fastio_cli.templates.fullstack_template.seeder.seeder_tmpl import SeederTmpl
from fastio_cli.templates.fullstack_template.seeder.database_seeder_tmpl import DatabaseSeederTmpl
from fastio_cli.templates.fullstack_template.request_model.request_model_tmpl import RequestModelTmpl
from fastio_cli.templates.fullstack_template.response_model.response_model_tmpl import ResponseModelTmpl
from fastio_cli.templates.fullstack_template.repository.respository_model_tmpl import RepositoryModelTmpl


class StandardTemplate:

    TEMPLATE = 'StandardTemplate'
    TEMPLATE_PATH = '/home/quanvu/Projects/pyworks-pypi/starter/generator/generator/templates/StandardTemplate'
    CONFIG = TemplateConfig(
        name='Restful API Project'
    )

    SWAGGER_DATA = None

    PROJECT_ROOT = ''
    PROJECT_CONFIG: ProjectConfig

    def __init__(self, project_root: str):
        self.PROJECT_ROOT = project_root
        self.set_project_config()

    def set_project_config(self):
        self.PROJECT_CONFIG = ProjectConfig(
            project_name='Fastapp',
            project_root_dir=self.PROJECT_ROOT,
            router_admin_dir='App/Api/admin',
            api_admin_dir='App/Api/admin/endpoints',
            router_client_dir='App/Api/v1',
            api_client_dir='App/Api/v1/endpoints',
            model_dir='App/Models',
            migration_dir='App/Database/Migrations',
            seeder_dir='App/Database/Seeds',
            repository_dir='App/Repositories',
            request_model_dir='App/Http/Requests',
            response_model_dir='App/Http/Responses',
            test_api_admin_dir='App/Tests/Feature/Admin',
            test_api_client_dir='App/Tests/Feature/Api',
        )

    def set_swagger_data(self, swagger_data):
        self.SWAGGER_DATA = swagger_data
        
    def generate_base_project(self):
        self.generate_project_struct()
        self.generate_schemas()

    def generate_project_struct(self):
        applicationTmpl = ApplicationTmpl()
        applicationTmpl.write(output_dir=self.PROJECT_CONFIG.project_root_dir)

    def generate_schemas(self):
        schemas = self.SWAGGER_DATA['schemas']
        for schema in schemas.items:
            if type(schema) is Model :
                # Generate Model 
                output_file = f'{self.PROJECT_CONFIG.project_root_dir}/{self.PROJECT_CONFIG.model_dir}/{schema.filename}.py'
                modelTmpl = ModelTmpl(data=schema)
                modelTmpl.write(
                    output_file=output_file
                )

                # Generate Repository 
                output_file = f'{self.PROJECT_CONFIG.project_root_dir}/{self.PROJECT_CONFIG.repository_dir}/{schema.filename}_repository.py'
                repositoryModelTmpl = RepositoryModelTmpl(data=schema)
                repositoryModelTmpl.write(
                    output_file=output_file
                )

                # Generate Request 
                output_file = f'{self.PROJECT_CONFIG.project_root_dir}/{self.PROJECT_CONFIG.request_model_dir}/{schema.filename}_request.py'
                requestModelTmpl = RequestModelTmpl(data=schema)
                requestModelTmpl.write(
                    output_file=output_file
                )

                # Generate Response 
                output_file = f'{self.PROJECT_CONFIG.project_root_dir}/{self.PROJECT_CONFIG.response_model_dir}/{schema.filename}_response.py'
                responseModelTmpl = ResponseModelTmpl(data=schema)
                responseModelTmpl.write(
                    output_file=output_file
                )

                # Generate Migration 
                output_file = f'{self.PROJECT_CONFIG.project_root_dir}/{self.PROJECT_CONFIG.migration_dir}/{schema.filename}_migration.py'
                migrationTmpl = MigrationTmpl(data=schema)
                migrationTmpl.write(
                    output_file=output_file
                )

                # Generate Seeder
                output_file = f'{self.PROJECT_CONFIG.project_root_dir}/{self.PROJECT_CONFIG.seeder_dir}/{schema.filename}_table_seeder.py'
                seederTmpl = SeederTmpl(data=schema)
                seederTmpl.write(
                    output_file=output_file
                )

                # Generate Api: admin 
                output_file = f'{self.PROJECT_CONFIG.project_root_dir}/{self.PROJECT_CONFIG.api_admin_dir}/{schema.filename}_admin_api.py'
                apiTmpl = ApiTmpl(data=schema)
                apiTmpl.write(
                    output_file=output_file
                )

                # Generate Api: client - v1 
                output_file = f'{self.PROJECT_CONFIG.project_root_dir}/{self.PROJECT_CONFIG.api_client_dir}/{schema.filename}_api.py'
                apiTmpl = ApiTmpl(data=schema)
                apiTmpl.write(
                    output_file=output_file
                )

                # Generate Tests - Api: admin
                output_file = f'{self.PROJECT_CONFIG.project_root_dir}/{self.PROJECT_CONFIG.test_api_admin_dir}/test_{schema.filename}_api.py'
                testApiTmpl = TestApiTmpl(data=schema)
                testApiTmpl.write(
                    output_file=output_file
                )

                # Generate Tests - Api: client
                output_file = f'{self.PROJECT_CONFIG.project_root_dir}/{self.PROJECT_CONFIG.test_api_client_dir}/test_{schema.filename}_api.py'
                testApiTmpl = TestApiTmpl(data=schema)
                testApiTmpl.write(
                    output_file=output_file
                )


        # Generate Database Seeder 
        output_file = f'{self.PROJECT_CONFIG.project_root_dir}/{self.PROJECT_CONFIG.seeder_dir}/database_seeder.py'
        databaseSeederTmpl = DatabaseSeederTmpl(data=schemas)
        databaseSeederTmpl.write(
            output_file=output_file
        )

        # Generate Api - Router admin
        output_file = f'{self.PROJECT_CONFIG.project_root_dir}/{self.PROJECT_CONFIG.router_admin_dir}/routers.py'
        routerTmpl = RouterTmpl(data=schemas)
        routerTmpl.write(
            output_file=output_file
        )

        # Generate Api - Router client: v1 
        output_file = f'{self.PROJECT_CONFIG.project_root_dir}/{self.PROJECT_CONFIG.router_client_dir}/routers.py'
        routerTmpl = RouterTmpl(data=schemas)
        routerTmpl.write(
            output_file=output_file
        )
            
                
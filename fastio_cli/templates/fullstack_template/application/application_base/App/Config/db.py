from App.Config.app import settings

DATABASES = {
    'default': 'mysql',
    'mysql': {
        'driver': 'mysql',
        'host': settings.DB_HOST,
        'port': settings.DB_PORT,
        'database': settings.DB_DATABASE,
        'user': settings.DB_USER,
        'password': settings.DB_PASSWORD,
        'prefix': settings.DB_PREFIX,
        'log_queries': True
    },
    'postgres': {
        'driver': 'postgres',
        'host': settings.DB_HOST,
        'database': settings.DB_DATABASE,
        'user': settings.DB_USER,
        'password': settings.DB_PASSWORD,
        'prefix': settings.DB_PREFIX,
        'port': settings.DB_PORT,
    }
}
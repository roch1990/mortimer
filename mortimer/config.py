from os import getenv as env


class Config:
    app_address = env('APP_ADDR', '0.0.0.0')
    app_port = env('APP_PORT', '8080')
    app_name = env('APP_NAME', 'mortimer')
    llevel = env('LLEVEL', 'DEBUG')
    app_salt = env('APP_SALT', 'MXhZifmhG7Zzegk2')

    # cache settings
    redis_enabled = bool(env('REDIS_ENABLED', False))

    # persistent backend settings
    db_host = env('DB_HOST', '0.0.0.0')
    db_port = env('DB_PORT', '5432')
    db_name = env('DB_NAME', 'test')
    db_user = env('DB_USER', 'test')
    db_pass = env('DB_PASS', 'test')
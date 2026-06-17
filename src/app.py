from decouple import config, UndefinedValueError

def get_db_config():
    return {
        "host":     config('MYSQL_HOST'),
        "user":     config('MYSQL_USER'),
        "password": config('MYSQL_PASSWORD'),
        "db":       config('MYSQL_DB'),
        "port":     config('MYSQL_PORT', default=3306, cast=int),
    }

if __name__ == "__main__":
    try:
        cfg = get_db_config()
        print(f"host: {cfg['host']}")
        print(f"user: {cfg['user']}")
        print(f"password: {'*' * len(cfg['password'])}")
        print(f"db:   {cfg['db']}")
        print(f"port: {cfg['port']}")
    except UndefinedValueError as e:
        print(f"Error: falta variable de entorno -> {e}")
        raise SystemExit(1)

import pymysql
import os


def check_mysql_connect():
    import re
    timeout = os.environ.get('DATABASE_TIMEOUT', 10)
    retry = os.environ.get('DATABASE_RETRY', 2)
    connection_params = re.split(':|@|/', os.environ.get('SQLALCHEMY_DATABASE_URI'))
    for i in range(retry + 1):
        print(f'TRY CONNECT {i+1}')
        try:
            connection = pymysql.connect(host=connection_params[5],
                                         port=int(connection_params[6]),
                                         user=connection_params[3],
                                         password=connection_params[4],
                                         database=connection_params[7],
                                         connect_timeout=timeout,
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT 1"
                cursor.execute(sql)
                result = cursor.fetchone()
                print('DB CONNECTED', result)
                return True
        except pymysql.DatabaseError:
            pass
    print('NO DATABASE CONNECTION')
    return False


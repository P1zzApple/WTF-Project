import psycopg2
from config import host, user, password, db_name
print('main is working')


def present():
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    with connection.cursor() as cursor:
        cursor.execute(
            f"""
            select * from fake_origami
            """  # replace fake with real when finished testing
        )
        res = cursor.fetchall()
        connection.close()
    return res

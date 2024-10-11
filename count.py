import psycopg2
from config import host, user, password, db_name
print('count is working')


def count():
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    with connection.cursor() as cursor:
        cursor.execute(
            f"""
                SELECT COUNT(id) FROM ORIGAMI
            """
        )
        this = cursor.fetchall()
        ans = this[0][0]
        connection.close()
    return ans

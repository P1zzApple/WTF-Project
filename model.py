import psycopg2
from config import host, user, password, db_name
print('model is working')


def process(data):
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    with connection.cursor() as cursor:
        cursor.execute(
            """
            select * from fake_origami 
            where id = %s
            """,  # replace fake with real when finished testing
            (data,)
        )
        mres = cursor.fetchall()  # make it fetchone maybe
        connection.close()
    return mres


''' # idk to leave it or not
try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            """
            select * from ori_test
            where id = %s
            """,
            (session['id'],)
        )
        #print('[INFO] great success')
        #mres = cursor.fetchone()
        #print(mres)
    

except Exception as _ex:
    print("Msg:Error while working with PostgreSQL", _ex)

finally:
    if connection:
        connection.close()
        print("Msg: PostgreSQL connection closed")
'''

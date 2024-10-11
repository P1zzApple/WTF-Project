import psycopg2
from config import host, user, password, db_name
from count import count
print('add is working')


def add(adding):
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    ans = count() + 1
    with connection.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO origami(id, name, image, author, color, size, difficulty, video_link, diagram, comment)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """, (ans, adding[0], adding[1], adding[2], adding[3], adding[4], adding[5], adding[6], adding[7], adding[8])
        )
    connection.commit()
    connection.close()
    print("Data added successfully")

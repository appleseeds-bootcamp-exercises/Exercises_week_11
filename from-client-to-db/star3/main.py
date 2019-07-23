import pymysql


# The SQl command to create the column:
# ALTER TABLE actors
# ADD num_of_movies int;

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='imdb',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor,
                             )


try:
    with connection.cursor() as c:
        c.execute(f'SELECT * FROM actors')
        actors = c.fetchall()
        for actor in c.fetchall():
            c.execute(
                f'SELECT COUNT(*) FROM cast WHERE actor_id = {actor["id"]}')
            actor_num_of_movies = c.fetchone()['COUNT(*)']
            c.execute(
                f'UPDATE actors SET num_of_movies = {actor_num_of_movies} WHERE id = {actor["id"]}')

except:
    print('Error with the db')
finally:
    connection.close()

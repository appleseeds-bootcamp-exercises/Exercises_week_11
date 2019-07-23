import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='imdb',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor,
                             )


actors_list = [
    {'Name': 'Jason Stathams', 'ID': 452342, 'Gender': 'M'},
    {'Name': 'David Schwimmer', 'ID': 530090, 'Gender': 'F'},
    {'Name': 'Jennifer Aniston', 'ID': 414244, 'Gender': 'M'},
    {'Name': 'Shlomo Abergel', 'ID': 542986, 'Gender': 'F'},
    {'Name': 'David Proval', 'ID': 383529, 'Gender': 'M'}
]


def check_if_id_exist(id):
    sql = f'SELECT * FROM actors WHERE id= "{id}"'
    c.execute(sql)
    return c.fetchone() is not None


def add_actor_to_db(actor):
    sql = f'INSERT INTO actors VALUES ({actor["ID"]}, "{actor["Name"]}", "{actor["Gender"]}")'
    c.execute(sql)


try:
    with connection.cursor() as c:
        for actor in actors_list:
            sql = f'SELECT * FROM actors WHERE full_name="{actor["Name"]}"'
            c.execute(sql)
            actor_in_db = c.fetchone()
            if actor_in_db is not None:
                print(actor['Name'] + ' already exists in the database')
            else:
                if check_if_id_exist(actor['ID']):
                    print(f'Could not add {actor["Name"]}to the database')
                else:
                    add_actor_to_db(actor)
                    print(
                        f'Actor {actor["Name"]} was not found and was added to the database')

        connection.commit()

except:
    print('Error with the db')
finally:
    connection.close()

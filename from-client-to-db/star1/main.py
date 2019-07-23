import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='imdb',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor,
                             )


actors_list = ['Jason statham', 'David Schwimmer', 'Jennifer Aniston']
print(actors_list)
try:
    with connection.cursor() as c:
        for actor in actors_list:
            sql = 'Select full_name from actors where full_name= ' + '"' + actor + '"'
            c.execute(sql)
            result = c.fetchone()
            print(actor + ' exists in the database' if result is not None else actor +
                  ' does not exists in the database')

finally:
    connection.close()

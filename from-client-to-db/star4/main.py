from bottle import get, run, static_file
import json
import pymysql



connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='imdb',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor,
                             )
                             

@get('/')
def index():
    return static_file('index.html', root='static')

@get('/get_actors')
def statics():
    try:
        with connection.cursor() as c:
            c.execute(f'SELECT * FROM actors')
            actors = c.fetchall()
            print(actors)
            return json.dumps(actors)
    except:
        return json.dumps({'error': 'Error with the db'})
    finally:
        connection.close()


@get('/<path:path>')
def statics(path):
    return static_file(path, root='static')

run(host='localhost', port=7000, reloader=True, Debug=True)

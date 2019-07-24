from bottle import run, route, get, post, delete, put, request
import pymysql
import json

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='imdb',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor,
                             )
try:
    with connection.cursor() as c:
        c.execute('USE bootcamp')
except:
    pass


@get('/student')
def get_student():
    name = request.json.get('name')
    try:
        with connection.cursor() as c:
            c.execute(
                f'SELECT * FROM students where full_name="{name}"; ')
            students = c.fetchone()
            return json.dumps(students)
    except:
        return json.dumps({'error': 'Error with the db/ no such student exists'})


@post('/student')
def add_student():
    full_name = request.json.get('name')
    is_cute = request.json.get('is_cute')
    try:
        with connection.cursor() as c:
            query = """
            INSERT INTO `students`
            VALUES (%s, %s, %s)
            """
            c.execute(query, (None, full_name,
                              True if is_cute == 'True' else False))
            connection.commit()
        return 'Student added'
    except:
        return 'Sadly could not add student'


@put('/student')
def update_student():
    id = request.json.get('id')
    full_name = request.json.get('name')
    is_cute = request.json.get('is_cute')
    try:
        with connection.cursor() as c:
            query = """
            UPDATE students
            SET full_name = %s, is_cute = %s
            WHERE id=%s;
            """
            c.execute(
                query, (full_name, 1 if is_cute.lower() == 'true' else 0, id))
            connection.commit()
        return 'Student updated'
    except:
        return 'Sadly could not update student'


@delete('/student')
def delete_student():
    id = request.json.get('id')
    try:
        with connection.cursor() as c:
            query = """
            DELETE FROM students
            WHERE id=%s;
            """
            c.execute(query, (id))
            connection.commit()
        return 'Student deleted'
    except:
        return 'Sadly could not delete student'


@get('/all_students')
def get_all_students():
    try:
        with connection.cursor() as c:
            c.execute('SELECT * FROM students')
            students = c.fetchall()
            return json.dumps(students)
    except:
        return json.dumps({'error': 'Error with the db'})


@get('/cohort')
def get_cohort():
    name = request.json.get('name')
    try:
        with connection.cursor() as c:
            c.execute(
                f'SELECT * FROM cohorts where cohort_name="{name}"; ')
            students = c.fetchone()
            return json.dumps(students)
    except:
        return json.dumps({'error': 'Error with the db/ no such cohort exists'})


@post('/cohort')
def add_cohort():
    name = request.json.get('name')
    try:
        with connection.cursor() as c:
            query = """
            INSERT INTO `cohorts`
            VALUES (%s, %s)
            """
            c.execute(query, (None, name))
            connection.commit()
            return 'Cohort added'
    except:
        return 'Sadly could not add cohort'


@delete('/cohort')
def delete_cohort():
    id = request.json.get('id')
    try:
        with connection.cursor() as c:
            query = """
            DELETE FROM cohorts
            WHERE id=%s;
            """
            c.execute(query, (id))
            connection.commit()
        return 'Cohort deleted'
    except:
        return 'Sadly could not delete cohort'


@get('/all_cohorts')
def get_all_cohorts():
    try:
        with connection.cursor() as c:
            c.execute('SELECT * FROM cohorts')
            students = c.fetchall()
            return json.dumps(students)
    except:
        return json.dumps({'error': 'Error with the db'})


@route('/')
def index():
    return 'Welcome to the Bootcamp API index page'


run(host='localhost', port=6500, reloader=True, debug=True)

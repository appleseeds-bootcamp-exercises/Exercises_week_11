from bottle import run, get, post, delete, put, request
import pymysql
import json

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='bootcamp',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor,
                             )

dict_unpack = lambda d, *k: [d[i] for i in k]


def get_student_by_identifier(c, identifier, value):
    c.execute(
        'SELECT * FROM students where '+identifier+'=%s', (value))
    return c.fetchone()


@get('/student/<name>')
def get_student(name):
    # try:
    with connection.cursor() as c:
        student = get_student_by_identifier(c, 'name', name)
        if student is None:
            return 'Error: no such student exists'
        return json.dumps(student)
    # except:
    #     return 'Error: with the db'


@post('/student')
def add_student():
    name, is_cute = dict_unpack(request.json, 'name', 'is_cute')
    try:
        with connection.cursor() as c:
            if get_student_by_identifier(c, "name", name) is not None:
                return 'Error: Student with this name already exist'
            query = """
            INSERT INTO `students`
            VALUES (%s, %s, %s)
            """
            c.execute(query, (None, name,
                              1 if is_cute == 'True' else 0))
            connection.commit()
        return 'Student added'
    except:
        return 'Error: Sadly could not add student'


@put('/student')
def update_student():
    name, is_cute, id = dict_unpack(
        request.json, 'name', 'is_cute', 'id')
    try:
        with connection.cursor() as c:
            if get_student_by_identifier(c, 'id', id) is None:
                return 'Error: no student with this id exists'
            query = """
            UPDATE students
            SET name = %s, is_cute = %s
            WHERE id=%s;
            """
            c.execute(
                query, (name, 1 if is_cute == 'True' else 0, id))
            connection.commit()
        return 'Student updated'
    except:
        return 'Sadly could not update student'


@delete('/student/<id>')
def delete_student(id):
    try:
        with connection.cursor() as c:
            if get_student_by_identifier(c, 'id', id) is None:
                return 'No student with this id exist!'
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
            if len(students)==0 :
                return 'No students on the database'
            return json.dumps(students)
    except:
        return json.dumps('Error: error with the database')


@get('/cohort/<name>')
def get_cohort(name):
    try:
        with connection.cursor() as c:
            c.execute(
                f'SELECT * FROM cohorts where cohort_name="{name}"; ')
            cohort = c.fetchone()
            if cohort is None:
                return 'Error: no such cohort exists'
            return json.dumps(cohort)
    except:
        return json.dumps('Error: error with the database')


@post('/cohort')
def add_cohort():
    name = request.json.get('name')
    try:
        with connection.cursor() as c:
            c.execute(
                'SELECT * FROM cohorts where name=%s', (name))
            if c.fetchone() is not None:
                return 'Error: cohort name already exist'
            query = """
            INSERT INTO `cohorts`
            VALUES (%s, %s)
            """
            c.execute(query, (None, name))
            connection.commit()
            return 'Cohort added'
    except:
        return 'Sadly could not add cohort'


@delete('/cohort/<id>')
def delete_cohort(id):
    try:
        with connection.cursor() as c:
            c.execute(
                'SELECT * FROM cohorts where id=%s', (id))
            if c.fetchone() is None:
                return 'Error: No cohort with this id exist'
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
            cohorts = c.fetchall()
            if len(cohorts) == 0:
                return 'no cohorts to show'
            return json.dumps(cohorts)
    except:
        return json.dumps({'error': 'Error with the db'})


@get('/')
def index():
    return 'Welcome to the Bootcamp API index page'


run(host='localhost', port=6500, reloader=True, debug=True)

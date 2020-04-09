import MySQLdb
import MySQLdb.cursors

def connection():
    cnx= MySQLdb.connect(host='localhost', user='root', passwd='', db='prueba', cursorclass=MySQLdb.cursors.DictCursor)
    cursor = cnx.cursor()

    return cnx, cursor

cnx, cursor = connection()

def get_users():
    query = cursor.execute('SELECT * FROM usuarios')
    results = cursor.fetchall()
    return results

def get_user_by_name(user):
    query = cursor.execute('SELECT user_id, user, passwrd FROM usuarios WHERE user=\''+user+'\';')
    results = cursor.fetchall()
    return results

def get_user_by_id(user_id):
    query = cursor.execute('SELECT user_id, user, passwrd FROM usuarios WHERE user_id=\''+str(user_id)+'\';')
    results = cursor.fetchall()
    return results

def get_todos(user_id):
    query = cursor.execute('SELECT todo FROM to_dos WHERE user_id='+ str(user_id)+';')
    results = cursor.fetchall()
    return results

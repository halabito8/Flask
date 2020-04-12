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
    if query > 0:
        flag = True
    else:
        flag = False
    return results, flag

def get_user_by_id(user_id):
    query = cursor.execute('SELECT user_id, user, passwrd FROM usuarios WHERE user_id=\''+str(user_id)+'\';')
    results = cursor.fetchall()
    return results

def new_user(username, password):
    query = cursor.execute('INSERT INTO usuarios(user, passwrd) VALUES(\''+username+'\',\''+password+'\');')
    cnx.commit()

def new_todo(user_id, description):
    query = cursor.execute('INSERT INTO to_dos(todo,user_id) VALUES(\''+description+'\',\''+ str(user_id)+'\');')
    cnx.commit()

def get_todos(user_id):
    query = cursor.execute('SELECT todo FROM to_dos WHERE user_id='+ str(user_id)+' AND done=0;')
    results = cursor.fetchall()
    if query > 0:
        flag = True
    else:
        flag = False
    return results, flag

def del_todo(description, user_id):
    query = cursor.execute('UPDATE to_dos SET done = 1 WHERE todo=\''+description+'\' And user_id='+str(user_id)+';')
    cnx.commit()
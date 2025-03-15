import pymysql

def connect_db():
    Connection = pymysql.Connect(host = 'localhost',user = 'root', password ='root', database = 'dhanush_tb',charset = 'utf8', port = 3306)
    print('DB connected')
    return Connection

def disconnect_db(connection):
    connection.close()
    print('DB dis-connected')


def create_db():
    query = 'create dataabse IF NOT EXSISTS dhanush_tb'
    connection  = connect_db()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    disconnect_db(connection)

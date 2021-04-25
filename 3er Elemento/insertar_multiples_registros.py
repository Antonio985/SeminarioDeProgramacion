# Realizar la importacion del modulo postgres sql
import psycopg2

# Realizar conexion a base de datos
conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='127.0.0.1',
                            port='5432',
                            database='testg02_db')

# utilizar el metodo cursor
cursor = conexion.cursor()
# creamos la setencia sql
sql = 'INSERT INTO persona(nombre, apellido, mail) VALUES(%s,%s,%s)'

# Creamos una varieble y asignacion de tuplas
valores = (('guillermo', 'MARTINEZ', 'eduardo.martinez@ues.mx'),
           ('joaquin', 'TORRES', 'enrrique.torre@ues.mx'),
           ('Maria', 'MONTAÑO', 'jesus.montalo@ues.mx'),
           ('Pedro', 'MURRIETA', 'alonso.murrieta@ues.mx'),
           ('Marco', 'NAVARRO', 'luis.navarro@ues.mx') )

# invocar la variable utilizando el metodo execute()
cursor.executemany(sql, valores)

# Guardaremos la informacion en la base de datos
# Utilizaremos el objeto de de conexio, invocando el metodo commit()
conexion.commit()

# Recuperaremos los registros que se han sido insertados
registros_insertados = cursor.rowcount
print(f'Registro insertado: {registros_insertados}')

# cerrar la conexion y cursor
cursor.close()
conexion.close()

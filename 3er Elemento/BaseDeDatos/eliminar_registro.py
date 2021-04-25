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
sql = 'DELETE FROM persona WHERE id_persona=%s'
# Crearemos una variable y haremos uso de la funcion INPUT}
entrada = input("Ingresar el indice que desea eliminar:")
# Creamos una varieble y asignacion de tuplas
valores = (entrada,)
# invocar la variable utilizando el metodo execute()
cursor.execute(sql, valores)
# Guardaremos la informacion en la base de datos
# Utilizaremos el objeto de de conexio, invocando el metodo commit()
conexion.commit()
# Recuperaremos los registros que se han sido eliminados
registros_eliminados = cursor.rowcount
print(f'Registro eliminado: {registros_eliminados}')

# cerrar la conexion y cursor
cursor.close()
conexion.close()

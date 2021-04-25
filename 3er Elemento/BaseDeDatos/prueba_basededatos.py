#Realizar la importacion del modulo postgres sql
import psycopg2
    
#Realizar conexion a base de datos
conexion = psycopg2.connect(user = 'postgres',
                            password= 'admin',
                            host= '127.0.0.1',
                            port= '5432',
                            database= 'testg02_db')
    
#utilizar el metodo cursor
cursor = conexion.cursor()
#creamos la setencia sql
sql = 'SELECT * FROM persona'
#invocar la variable utilizando el metodo execute()
cursor.execute(sql)

#enviar a impresion
registros = cursor.fetchall()
print(registros)

#cerrar la conexion y cursor
cursor.close()
conexion.close()



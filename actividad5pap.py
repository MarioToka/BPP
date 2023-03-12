'''
Este programa servirá para crear dos tablas, de 2 y 4 campos e implementar llas funciones insertar, actualizar, listar y borrar sobre cada una de las tablas
'''

#Primero importamos el paquete sqlite3 para porde trabajar en lenguaje sql

import sqlite3

#Ahora vamos a crear la base de datos

def crear_conexion():
    '''
    Crea la conexión
    '''
    try:
        con = sqlite3.connect("./mibase.db")
        print("Se ha creado una BDD")
        return con
    #except Exception as e:
    except sqlite3.Error as e:
        print("Ha habido un error",e)

#creamos la función que genera las dos tablas que queremos

def crear_tabla(con):
    '''
    Crea una tabla
    '''
    try:
        my_cursor = con.cursor()
        my_cursor.execute("CREATE TABLE IF NOT EXISTS tabla1 (t1c1 varchar(100), t1c2 varchar(100), t1c3 varchar(100), t1c4 varchar(100));")
        my_cursor.execute("CREATE TABLE IF NOT EXISTS tabla2 (t2c1 varchar(100), t2c2 varchar(100))")
        con.commit()
        print("Las tablas han sido creadas")
    except Exception as e:
        print("Error creando la tabla: ",e)

#Definamos las distintas funciones que queremos usar

def insertar_registro(con):
    '''
    Crea un nuevo registro en la tabla indicada
    '''
    try:
        my_cursor = con.cursor()
        r1 = input("¿Quieres hacer un nuevo registro en la tabla 1? (Pulsa s si sí y n si no) ")
        if r1 == 's':
            t1c1input = input("Introduce lo que quieras poner en la primera columna de este registro en la tabla 1 ")
            t1c2input = input("Introduce lo que quieras poner en la segunda columna de este registro en la tabla 1 ")
            t1c3input = input("Introduce lo que quieras poner en la tercera columna de este registro en la tabla 1 ")
            t1c4input = input("Introduce lo que quieras poner en la cuarta columna de este registro en la tabla 1 ")
            intro1 = '''
            insert into tabla1(t1c1,t1c2,t1c3,t1c4) 
            values(?,?,?,?)
            '''
            parametro = (t1c1input,t1c2input,t1c3input,t1c4input)
            my_cursor.execute(intro1,parametro)
            print("El registro ha sido creado en la tabla 1")

        r2 = input("¿Quieres hacer un nuevo registro en la tabla 2? (Pulsa s si sí y n si no) ")
        if r2 == 's':
            t2c1input = input("Introduce lo que quieras poner en la primera columna de este registro en la tabla 2")
            t2c2input = input("Introduce lo que quieras poner en la segunda columna de este registro en la tabla 2")
            intro2 = '''
            insert into tabla2(t2c1,t2c2) 
            values(?,?)
            '''
            parametro = (t2c1input,t2c2input)
            my_cursor.execute(intro2,parametro)
            print("El registro ha sido creado en la tabla 2")

        con.commit()
        
    except Exception as e:
        print("Error creando el registro: ",e)

def actualizar_base(con):
    '''
    actualiza las entradas de la base
    '''
    try:
        my_cursor = con.cursor()
        a1 = input("¿Quieres actualizar la algún registro de la tabla 1? (s o n) ")
        if a1 == 's':
            print("Dame los nombres de los elementos de cada columna de la tabla (y de la misma fila) que quieras modificar. Si algún elemento de la fila lo quieres mantener, introdúcelo y cuando te pida el modificado, vuelve a ponerlo.")
            t1c1oinput = input("¿Qué elemento de la primera columna quieres modificar?")
            t1c1ninput = input("¿Por qué nuevo elemento lo quieres cambiar?")
            t1c2oinput = input("¿Qué elemento de la segunda columna quieres modificar?")
            t1c2ninput = input("¿Por qué nuevo elemento lo quieres cambiar?")
            t1c3oinput = input("¿Qué elemento de la tercera columna quieres modificar?")
            t1c3ninput = input("¿Por qué nuevo elemento lo quieres cambiar?")
            t1c4oinput = input("¿Qué elemento de la cuarta columna quieres modificar?")
            t1c4ninput = input("¿Por qué nuevo elemento lo quieres cambiar?")
            update1 = '''update tabla1 set t1c1 = ?, t1c2 = ?, t1c3 = ?, t1c4 = ? 
            where t1c1 = ? and t1c2 = ? and t1c3 = ? and t1c4 = ?'''
            parametro1 = (t1c1ninput,t1c2ninput,t1c3ninput,t1c4ninput,t1c1oinput,t1c2oinput,t1c3oinput,t1c4oinput)
            my_cursor.execute(update1,parametro1)
        a2 = input("¿Quieres actualizar la algún registro de la tabla 2? (s o n)")
        if a2 == 's':
            print("Dame los nombres de los elementos de cada columna de la tabla (y de la misma fila) que quieras modificar. Si algún elemento de la fila lo quieres mantener, introdúcelo y cuando te pida el modificado, vuelve a ponerlo.")
            t2c1oinput = input("¿Qué elemento de la primera columna quieres modificar?")
            t2c1ninput = input("¿Por qué nuevo elemento lo quieres cambiar?")
            t2c2oinput = input("¿Qué elemento de la segunda columna quieres modificar?")
            t2c2ninput = input("¿Por qué nuevo elemento lo quieres cambiar?")
            update2 = '''update tabla2 set t2c1 = ?, t2c2 = ? 
            where t1c1 = ? and t1c2 = ?'''
            parametro2 = (t2c1ninput,t2c2ninput,t2c1oinput,t2c2oinput)
            my_cursor.execute(update2,parametro2)
    except Exception as e: 
        print("Error actualizando la base",e)

#Definamos la función de lisrado de elementos

def select_rows(con):
    '''
    Sirve kpara seleccionar una determinada fila
    '''
    try:
        my_cursor = con.cursor()
        my_cursor.execute("select * from tabla1") 
        rows1 = my_cursor.fetchall()
        print("Los elementos de la tabla 1 son:")
        print(rows1)
        my_cursor.execute("select * from tabla2")
        rows2 = my_cursor.fetchall()
        print("Los elementos de la tabla 2 son:")
        print(rows2)
    except Exception as e:
        print("Error seleccionando elementos: ",e)

def delete_rows(con):
    '''
    Elimina una de las filas de la tabla
    '''
    try:
        my_cursor = con.cursor()
        r1 = input("¿Quieres eliminar algún registro de la tabla 1? (s o n) ")
        if r1 == 's':
            t1c1rinput = input("¿Cuál es el primer elemento de la fila que quieres eliminar?")
            t1c2rinput = input("¿Cuál es el segundo elemento de la fila que quieres eliminar?")
            t1c3rinput = input("¿Cuál es el tercer elemento de la fila que quieres eliminar?")
            t1c4rinput = input("¿Cuál es el cuarto elemento de la fila que quieres eliminar?")
            delete1 = '''delete from tabla1 where t1c1 = ? and t1c2 = ? and t1c3 = ? and t1c4 = ?'''
            parametro = (t1c1rinput,t1c2rinput,t1c3rinput,t1c4rinput)
            my_cursor.execute(delete1,parametro)
        
        r2 = input("¿Quieres eliminar algún registro de la tabla 2? (s o n) ")
        if r2 == 's':
            t2c1rinput = input("¿Cuál es el primer elemento de la fila que quieres eliminar?")
            t2c2rinput = input("¿Cuál es el segundo elemento de la fila que quieres eliminar?")
            delete2 = '''delete from tabla1 where t1c1 = ? and t1c2 = ?'''
            parametro = (t1c1rinput,t1c2rinput)
            my_cursor.execute(delete2,parametro)
    except Exception as e:
        print("Error eliminando elementos",e)

con = crear_conexion()
crear_tabla(con)
insertar_registro(con)
actualizar_base(con)
select_rows(con)
delete_rows(con)
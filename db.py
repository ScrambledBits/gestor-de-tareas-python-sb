import sqlite3
import os

archivo_bd = os.path.join(os.getcwd(), "tareas.db")
con = sqlite3.connect(archivo_bd)
cursor = con.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS tareas(
        id integer primary key autoincrement,
        nombre text,
        descripcion text,
        completada
    )
    """
)

con.close()


def obtener_todas_las_tareas() -> list:
    try:
        con = sqlite3.connect(archivo_bd)
        cursor = con.cursor()
        cursor.execute("SELECT * FROM tareas")
        tareas = cursor.fetchall()
        return tareas
    except Exception as error:
        print(f"Hubo un error al mostrar las tarea:\n{error}")
        return False
    finally:
        con.close()


def agregar_tarea(nombre: str, descripcion: str) -> bool:
    completada = False
    try:
        con = sqlite3.connect(archivo_bd)
        cursor = con.cursor()
        cursor.execute(
            f"INSERT INTO tareas (nombre, descripcion, completada) VALUES ('{nombre}', '{descripcion}', '{completada}')"
        )
        con.close()
        return True
    except Exception as error:
        print(f"Hubo un error al agregar la tarea:\n{error}")
        return False
    finally:
        con.commit()


def actualizar_tarea(id):
    try:
        con = sqlite3.connect(archivo_bd)
        cursor = con.cursor()
        cursor.execute(
            f"""
                UPDATE tareas
                SET completada = True
                WHERE tareas.id = {id};
            """
        )
        con.commit()
        return True
    except Exception as error:
        print(f"Hubo un error al actualizar la tarea:\n{error}")
        return False
    finally:
        con.close()


def borrar_tarea(id):
    try:
        con = sqlite3.connect(archivo_bd)
        cursor = con.cursor()
        cursor.execute(f"DELETE FROM tareas WHERE id = {id}")
        con.commit()
        return True
    except Exception as error:
        print(f"Hubo un error al eliminar la tarea:\n{error}")
        return False
    finally:
        con.close()


if __name__ == "__main__":
    print("este es el archivo de base de datos")
    print(f"El contexto es: {__name__}")
    print(archivo_bd)
    print(f"Tareas: {obtener_todas_las_tareas()}")

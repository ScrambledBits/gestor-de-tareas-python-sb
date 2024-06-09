import os
import db


# tareas = []
def clear_screen():
    os.system(command="cls")


def agregar_tarea(nombre: str, descripcion: str) -> str:
    resultado = db.agregar_tarea(nombre=nombre, descripcion=descripcion)
    if resultado:
        print(f"La tarea {nombre} fue agregada exitosamente\n\n")
    else:
        print(f"La tarea {nombre} no se pudo agregar\n\n")


def mostrar_todas_las_tareas():
    tareas = db.obtener_todas_las_tareas()
    print("\n\nTus tareas pendientes son:")
    for tarea in tareas:
        id, nombre, descripcion, completada = tarea
        print(
            f"ID: {id}, Nombre: {nombre}, Desc: {descripcion}, Completada: {completada}\n{'-'*45}"
        )


def marcar_completada(id):
    if db.actualizar_tarea(id=id):
        print(f"La tarea con ID = {id} fue actualizada existosamente")
    else:
        print("La tarea no se pudo actualizar")


def eliminar_tarea(id):
    if db.borrar_tarea(id=id):
        print(f"La tarea con ID = {id} fue borrada existosamente")
    else:
        print("La tarea no se pudo borrar")


if __name__ == "__main__":
    print("este es el archivo de funciones")
    print(f"El contexto es: {__name__}")

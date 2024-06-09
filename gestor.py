import funciones as f


def menu():
    while True:
        # f.clear_screen()
        print(
            """
=== Mis tareas ===
1) Agregar una tarea
2) Mostrar todas las tareas
3) Marcar como completada
4) Eliminar tarea
5) Salir del programa
              """
        )
        try:
            opcion = int(input("¿Qué quieres hacer? "))
            if opcion == 1:
                f.clear_screen()
                nombre = input("¿Cuál es el nombre de la tarea que quieres agregar? ")
                descripcion = input(
                    "Dame una descripcion para la tarea anterior, pofabó: "
                )
                f.agregar_tarea(nombre=nombre, descripcion=descripcion)
            elif opcion == 2:
                f.clear_screen()
                f.mostrar_todas_las_tareas()
                input("Presiona cualquier tecla para continuar")
            elif opcion == 3:
                f.clear_screen()
                f.mostrar_todas_las_tareas()
                tarea = int(input("Escribe el número de tarea a modificar: "))
                f.marcar_completada(id=tarea)
            elif opcion == 4:
                f.clear_screen()
                f.mostrar_todas_las_tareas()
                id = int(input("Escribe el ID de tarea a eliminar: "))
                f.eliminar_tarea(id=id)
                input("Presiona cualquier tecla para continuar")
            else:
                break
        except Exception as error:
            print(error)


if __name__ == "__main__":
    menu()

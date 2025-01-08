import pandas as pd

agenda=[]
while True:
    print("\n Bienvenidos a la agenda, tenemos las siguientes opciones: ")
    print(" 1. Agregar contacto")
    print(" 2. Mostrar contacto")
    print(" 3. Actualizar teléfono")
    print(" 4. Actualizar correo")
    print(" 5. eliminar contacto")
    print(" 6. Exportar a excel")
    print(" 7. Salir")

    try:
        opcion = input("Seleccione la opción que desea: ")
        if not opcion.isdigit() or not (1 <= int(opcion) <= 7):
            raise ValueError("Por favor, ingrese un número entre 1 y 7.")
    except ValueError as e:
        print(f"Error: {e}")
        continue

    if opcion == "1":
      print("Seleccionaste Agregar contacto: ", opcion)
      try:
          nombre = input("Ingrese el nombre del contacto: ")
          if not nombre:
              raise ValueError("El nombre no puede estar vacío.")

          correo = input("Ingrese la dirección de correo del contacto: ")
          if not correo:
              raise ValueError("El correo no puede estar vacío.")

          telefono = input("Ingrese el número de teléfono del contacto: ")
          if not telefono:
              raise ValueError("El teléfono no puede estar vacío.")

          contacto = {"nombre": nombre, "correo": correo, "telefono": telefono}
          agenda.append(contacto)
          print(agenda)
      except ValueError as e:
          print(f"Error: {e}")

    elif opcion=="2":
          print("Seleccionaste Mostrar contacto: ",opcion)
          if not agenda:
              print("La agenda se encuentra vacía ")
          else:
              lenght=len(agenda)
              for id in range(lenght):
                  contacto=agenda[id]
                  print("\n Contacto ",id+1)
                  print("Nombre: ",contacto["nombre"])
                  print("Teléfono: ",contacto["telefono"])
                  print("Correo electrónico: ",contacto["correo"])



    elif opcion == "3":
        print("Seleccionaste Actualizar teléfono: ", opcion)
        if not agenda:
            print("La agenda se encuentra vacía.")
        else:
            lenght = len(agenda)
            for id in range(lenght):
                contacto = agenda[id]
                print("\n Contacto ", id+1)
                print("Nombre: ", contacto["nombre"])
            try:
                contacto_id = int(input("Selecciona el contacto a modificar: ")) - 1
                if contacto_id < 0 or contacto_id >= lenght:
                    raise IndexError("El contacto seleccionado no existe.")

                nuevo_telefono = input("Ingresa el nuevo teléfono: ")
                agenda[contacto_id]["telefono"] = nuevo_telefono
                print("Teléfono actualizado exitósamente.")
            except ValueError:
                print("Error: Debe ingresar un número válido.")
            except IndexError as e:
                print(f"Error: {e}")


    elif opcion=="4":
        print("Seleccionaste Actualizar correo: ",opcion)
        if not agenda:
            print("La agenda se encuentra vacía.")
        else:
            lenght = len(agenda)
            for id in range(lenght):
                contacto = agenda[id]
                print("\n Contacto ", id+1)
                print("Nombre: ", contacto["nombre"])
            try:
                contacto_id = int(input("Selecciona el contacto a modificar: ")) - 1
                if contacto_id < 0 or contacto_id >= lenght:
                    raise IndexError("El contacto seleccionado no existe.")

                nuevo_correo = input("Ingresa el nuevo correo: ")
                agenda[contacto_id]["correo"] = nuevo_correo
                print("Correo actualizado exitósamente.")
            except ValueError:
                print("Error: Debe ingresar un número válido.")
            except IndexError as e:
                print(f"Error: {e}")


    elif opcion=="5":
          print("Seleccionaste Eliminar contacto: ",opcion)
          if not agenda:
            print("La agenda se encuentra vacía.")
          else:
            lenght = len(agenda)
            for id in range(lenght):
                contacto = agenda[id]
                print("\n Contacto ", id+1)
                print("Nombre: ", contacto["nombre"])
            try:
                contacto_id = int(input("Selecciona el contacto a modificar: ")) - 1
                if contacto_id < 0 or contacto_id >= lenght:
                    raise IndexError("El contacto seleccionado no existe.")

                eliminado = agenda.pop(contacto_id)
                print(f"Contacto eliminado: {eliminado['nombre']}")

            except ValueError:
                print("Error: Debe ingresar un número válido.")
            except IndexError as e:
                print(f"Error: {e}")

    elif opcion=="6":
          print("Seleccionaste Exportar a Excel: ",opcion)
          if not agenda:
            print("La agenda se encuentra vacía.")
          else:
            df = pd.DataFrame(agenda)
            df.to_excel("agenda.xlsx", index=False)
            print("Agenda exportada a Excel exitosamente.")
    elif opcion=="7":
          print("Seleccionaste Salir: ",opcion)
          break
    else:
          print("Opción no válida")
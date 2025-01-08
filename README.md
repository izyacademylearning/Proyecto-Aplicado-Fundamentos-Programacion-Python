# Proyecto-Aplicado-Fundamentos-Programacion-Python
# Agenda de Contactos

Este proyecto es un programa interactivo para gestionar una agenda de contactos. Permite agregar, mostrar, actualizar, eliminar contactos y exportar los datos a un archivo Excel.

## Características

1. **Agregar Contacto**: Permite añadir un nuevo contacto con nombre, correo y teléfono.
2. **Mostrar Contactos**: Muestra todos los contactos almacenados en la agenda.
3. **Actualizar Teléfono**: Actualiza el número de teléfono de un contacto seleccionado.
4. **Actualizar Correo**: Actualiza la dirección de correo electrónico de un contacto seleccionado.
5. **Eliminar Contacto**: Elimina un contacto de la agenda.
6. **Exportar a Excel**: Exporta todos los contactos almacenados en un archivo Excel.
7. **Salir**: Finaliza la ejecución del programa.

## Requisitos

- Python 3.6 o superior
- Biblioteca `pandas` instalada

Para instalar `pandas`, utiliza el siguiente comando:

```bash
pip install pandas
```

## Uso

1. Clona este repositorio o copia el archivo a tu máquina local.
2. Ejecuta el programa en la terminal:

   ```bash
   python nombre_del_archivo.py
   ```

3. Utiliza el menú interactivo para gestionar los contactos:
   - Opción 1: Agregar un nuevo contacto.
   - Opción 2: Mostrar la lista de contactos.
   - Opción 3: Actualizar el número de teléfono de un contacto.
   - Opción 4: Actualizar el correo electrónico de un contacto.
   - Opción 5: Eliminar un contacto de la lista.
   - Opción 6: Exportar los contactos a un archivo Excel.
   - Opción 7: Salir del programa.

## Estructura del Código

### Funcionalidades Principales

- **Agregar Contacto**: Solicita al usuario el nombre, correo y teléfono del contacto, y lo guarda en la agenda.
- **Mostrar Contactos**: Itera sobre la lista de contactos y muestra la información de cada uno.
- **Actualizar Teléfono/Correo**: Permite modificar el número de teléfono o correo de un contacto seleccionado.
- **Eliminar Contacto**: Permite eliminar un contacto seleccionado por su índice en la lista.
- **Exportar a Excel**: Usa la biblioteca `pandas` para exportar la agenda a un archivo `agenda.xlsx`.

### Control de Errores

El programa incluye validaciones para manejar errores como:
- Selecciones inválidas del menú.
- Campos vacíos al agregar contactos.
- Índices fuera de rango al actualizar o eliminar contactos.

## Ejemplo de Ejecución

```text
Bienvenidos a la agenda, tenemos las siguientes opciones:
 1. Agregar contacto
 2. Mostrar contacto
 3. Actualizar teléfono
 4. Actualizar correo
 5. Eliminar contacto
 6. Exportar a excel
 7. Salir
Seleccione la opción que desea: 1
Ingrese el nombre del contacto: Juan Pérez
Ingrese la dirección de correo del contacto: juan.perez@gmail.com
Ingrese el número de teléfono del contacto: 123456789
[{'nombre': 'Juan Pérez', 'correo': 'juan.perez@gmail.com', 'telefono': '123456789'}]
```

## Mejoras Futuras

- Agregar la funcionalidad para buscar contactos por nombre o correo.
- Guardar los contactos en un archivo para persistencia de datos.
- Implementar una interfaz gráfica de usuario.

## Contribuciones

¡Las contribuciones son bienvenidas! Si tienes sugerencias o mejoras, crea un issue o un pull request.

## Licencia

Este proyecto fue desarrollado como parte de un curso en IzyAcademy.

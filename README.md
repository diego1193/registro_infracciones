# Sistema de Registro de Infracciones de Tránsito 📖

## Descripción

Este proyecto es un sistema de registro de infracciones de tránsito desarrollado en Python. Incluye una interfaz administrativa, API para cargar infracciones, y generación de informes de infracciones.

## Características Principales

- **Interfaz Administrativa**: Gestión de registros de personas, vehículos y oficiales.
- **API de Infracciones**: Permite a los oficiales cargar infracciones a través de una App.
- **Generación de Informes**: Método API para obtener informes de infracciones por correo electrónico.

## Uso y Documentación 📋

### Desarrollo y Tecnologías Implementadas

Este proyecto ha sido desarrollado utilizando el framework Django junto con Django REST Framework, siguiendo el patrón de arquitectura Modelo-Vista-Controlador (MVC). Se han implementado diversos endpoints para manejar las operaciones requeridas, proporcionando una API robusta y segura. 

Para la autenticación y seguridad, se ha integrado JSON Web Token (JWT) asegurando así la protección de los endpoints. La elección de SQLite como sistema de gestión de base de datos ofrece una solución ligera y eficiente para el almacenamiento de datos.

En cuanto al despliegue, se ha optado por Docker, facilitando la contenerización y la gestión de la aplicación y sus dependencias de manera eficiente y escalable.

### Librerías y Herramientas Utilizadas

- **Django**: Un framework web de alto nivel para el desarrollo rápido y limpio del backend, fomentando un diseño pragmático y limpio.
- **Django REST Framework**: Potente y flexible framework para construir APIs RESTful, mejorando la funcionalidad de Django con un conjunto de herramientas adicionales para la creación de APIs.
- **SQLite**: Sistema de gestión de bases de datos relacional ligero, que ofrece un almacenamiento de datos sencillo y efectivo para aplicaciones de menor escala.
- **Docker**: Plataforma de contenerización que permite empaquetar y ejecutar aplicaciones en un entorno aislado llamado contenedor, facilitando el despliegue y la escalabilidad.
  
## Arquitectura AWS para Producción 🚀

Para la arquitectura de servicios AWS de la aplicación, recomiendo un enfoque de Infraestructura como Servicio (IaaS) y Plataforma como Servicio (PaaS). Esto proporciona flexibilidad y control sobre los recursos informáticos, al tiempo que aprovecha la administración y la automatización que ofrece AWS.

### Bases de Datos Híbridas
Para manejar información delicada como la de personas y agentes, sugiero una base de datos híbrida que combine tanto SQL como NoSQL.

### Servicios: 

1. #### Amazon RDS (SQL):
   - **Uso**: Almacenar datos estructurados como información de personas y agentes.
   - **Justificación**: RDS proporciona capacidades de gestión y escalabilidad para bases de datos relacionales, facilitando el manejo de datos sensibles con seguridad y eficiencia.
     
2. #### Amazon DynamoDB (NoSQL):
   - **Uso**: Almacenar datos no estructurados o semi-estructurados, como logs, datos de transacciones, o información de sesiones.
   - **Justificación**: DynamoDB es ideal para manejar grandes volúmenes de datos con requisitos de baja latencia y alto rendimiento, complementando las capacidades de RDS.
     
3. #### Amazon EC2:
   - **Uso**: Hospedaje del servidor de la aplicación Django.
   - **Justificación**: Ofrece control sobre el entorno del servidor, permitiendo una configuración personalizada.
     
4. #### Amazon S3:
   - **Uso**: Almacenamiento de archivos estáticos y multimedia.
   - **Justificación**: Escalabilidad y alta disponibilidad para almacenar archivos.
     
5. #### AWS Elastic Load Balancer (ELB):
   - **Uso**: Distribuir el tráfico entrante entre múltiples instancias EC2.
   - **Justificación**: Asegura la alta disponibilidad y la distribución equitativa de las cargas de trabajo.
     
6. #### AWS Identity and Access Management (IAM):
   - **Uso**: Gestión de permisos y acceso seguro a los recursos de AWS.
   - **Justificación**: Permite un control detallado sobre quién puede acceder a qué recursos, crucial para la seguridad.
     
7. #### Amazon CloudWatch:
   - **Uso**: Monitoreo y alertas.
   - **Justificación**: Proporciona información valiosa sobre el rendimiento de la aplicación, uso de recursos y patrones de tráfico.
     
8. #### AWS Auto Scaling:
   - **Uso**: Escalar recursos automáticamente.
   - **Justificación**: Asegura que la aplicación tenga los recursos necesarios durante picos de demanda.
     
9. #### AWS Route 53:
   - **Uso**: Sistema de nombres de dominio (DNS).
   - **Justificación**: Gestiona el DNS de la aplicación, incluyendo el balanceo de carga y la salud del enrutamiento.


## Desarrollo del sistema. 💻

### Requisitos Previos 🛠️

Antes de comenzar, asegúrate de tener instalados **Python 3.10** y **Docker** en tu sistema. Estas herramientas son esenciales para construir y ejecutar el entorno contenerizado del proyecto.

### Clonar el Repositorio

Para obtener una copia del proyecto, clónalo en la carpeta de tu elección utilizando el siguiente comando:

```bash
git clone https://github.com/diego1193/registro_infracciones.git
```

### Ejecución del Programa

- Mediante **Docker Hub**:
  Puedes usar la imagen del repositorio [infracciones_gestion](https://hub.docker.com/r/diego1193/infracciones_gestion), siguiendo estos pasos:
  
  **descargar imagen**:
  Ejecuta el siguiente comando para obtener la imagen de Docker:
  ```bash
  docker pull diego1193/infracciones_gestion
  ```
  **Lanzar imagen**:
  Para iniciar la imagen descargada, utiliza:
  ```bash
  docker run -p 8000:8000 diego1193/infracciones_gestion
  ```
  
- Desde local:
  Si prefieres ejecutar el proyecto localmente, sigue estos pasos después de clonar el repositorio:
  
  **Configurar el entorno virtual**:
  Para preparar el entorno de ejecución, ejecuta:
  ```bash
  python -m venv entorno
  source entorno/bin/activate 
  pip install -r requirements.txt
  ```

  **Iniciar el proyecto**:
  Para lanzar el proyecto, utiliza:
  ```bash
  python manage.py runserver
  ```
  
## Iterfaz administrativa

Una vez levantado el proyecto podemos ingresar al admin de django con la siguiente url:

```
http://localhost:8000/admin/
``` 

El usuario y contrasena son los siguientes

```
Usuario: root
Password: root
``` 

En esta sección, podrás gestionar registros para varios modelos, incluyendo Oficiales, Personas, Vehículos e Infracciones. Cada categoría ofrece opciones para crear, visualizar, modificar y eliminar registros.

### Personas:
Aquí encontrarás opciones para buscar personas por nombre o correo electrónico. Utiliza el botón `ADD PERSONA` para agregar nuevas entradas o la opción `Action` para eliminar registros existentes. Al crear un registro, deberás proporcionar el nombre y el correo electrónico de la persona.

### Vehiculos
Esta sección permite buscar vehículos por placa o propietario. Para agregar un vehículo, selecciona `ADD VEHÍCULO` y utiliza `Action` para eliminarlos. Al registrar un vehículo, es necesario completar varios campos obligatorios, incluyendo la relación con el propietario, que debe estar vinculado a un registro de persona previamente creado.

### Users
Encontrarás opciones para buscar usuarios por nombre de usuario o dirección de correo electrónico. Usa `ADD USUARIO` para añadir nuevos usuarios o `Action` para eliminarlos. Al crear un usuario, debes proporcionar información requerida como el nombre de usuario y la contraseña, asegurándote de no activar la opción de superusuario.

### Oficiales
Aquí puedes buscar oficiales por nombre o número de identificación. Para agregar un oficial, utiliza `ADD OFICIAL` y `Action` para su eliminación. Al crear un registro de oficial, se requieren ciertos campos, incluyendo una relación con un registro de usuario previo. Es importante crear primero el usuario y luego asignarlo al oficial, lo que facilitará posteriormente el uso de la API para agregar infracciones, realizar login, crear token y efectuar peticiones POST.

## APIs
He desarrollado las APIs **generar_informe** y **crear_infraccion** de dos maneras distintas. A continuación, explico el funcionamiento de ambas:

### Generacion Token
La autenticación se realiza mediante un Bearer token, obtenido tras iniciar sesión con el usuario y contraseña de un oficial. Este proceso es esencial para acceder a las funcionalidades de las APIs.

Es importante utilizar las credenciales correctas, que deben estar registradas en el apartado de Usuario en el admin y asignadas a un oficial específico.

### Login para pruebas
Para las pruebas, se puede utilizar el siguiente usuario de prueba, ya incluido en la base de datos:

```json
{
  "username": "ramirez",
  "password": "juan1234"
}
``` 
### Login mediante banner:  
Al ingresar a http://localhost:8000/login_user/ y proporcionar las credenciales correctas, serás redirigido a la página **crear_infraccion**

![Img 1](/imagenes/img_1.png)

### Login demostrado en Postman
Peticion HTTP POST 
```
http://localhost:8000/login/
``` 
Mediante una petición HTTP POST a http://localhost:8000/login/, recibirás, si es exitoso, un código de estado HTTP 200 junto con un JSON que contiene dos tokens: refresh y access. El token de acceso se utiliza para autenticar solicitudes a endpoints protegidos, mientras que el token de actualización sirve para obtener un nuevo token de acceso cuando sea necesario.

ejemplo:
![Img 2](/imagenes/img_2.png)

## Agregando JWT a los Endpoints

Para probar los endpoints protegidos en Postman, necesitarás incluir el JSON Web Token (JWT) obtenido después del inicio de sesión. Si estás utilizando el [Workspace de Postman](https://www.postman.com/red-sunset-571136/workspace/infracciones/overview), puedes configurar el token como una variable global de entorno.

#### Configuración del Token:

1. **Obtener el Token**: Inicia sesión mediante el endpoint de login para obtener el `access token`.


2. **Agregar el Token al Entorno Global**:
   
    En Postman, ve a la sección de "Environments" y configura una nueva variable global llamada `accaessToken` con el valor del JWT.

#### Uso del Token en las Solicitudes:

- Al realizar solicitudes a endpoints protegidos, asegúrate de incluir el token JWT en la cabecera `Authorization` con el prefijo `Bearer`.
- Puedes hacerlo automáticamente en Postman seleccionando `Bearer Token` en el tipo de autorización y utilizando la variable global previamente configurada.

Siguiendo estos pasos, podrás probar fácilmente los endpoints protegidos de tu API en Postman.


## API Crear Infracción

### Creación de Infracción Mediante Banner:
Tras iniciar sesión, serás redirigido a http://localhost:8000/cargar_infraccion/ . Aquí, un formulario te permitirá completar tres campos. Al seleccionar el ícono del calendario, podrás elegir fácilmente la fecha y hora del incidente.

![Img 3](/imagenes/img_3.png)

### Creación de Infracción en Postman:

Para realizar esta acción, es crucial incluir el token JWT en la cabecera `Authorization`. Al enviar una petición HTTP POST a http://localhost:8000/carga_infraccion/, recibirás una respuesta con un código de estado HTTP 200 y un JSON confirmando el proceso completado.

```json
{
    "placa_patente": "JCD099",
    "timestamp": "2024-01-25T00:00:00Z",
    "comentarios": "paso semaforo en rojo"
}
``` 
ejemplo:

![Img 4](/imagenes/img_4.png)

****

## API Generar Informe

### Generar Informe Mediante Banner:
En http://localhost:8000/informe/, un formulario te permitirá ingresar el correo electrónico del dueño del vehículo (Registro Persona) registrado. Al hacer clic en buscar, se mostrarán las infracciones asociadas a ese vehículo.

ejemplo:
![Img 5](/imagenes/img_5.png)

### Generar Informe en Postman:

Realizando una petición HTTP GET a http://127.0.0.1:8000/generar_informe/[email de la persona]/, recibirás como respuesta un código de estado HTTP 200 y un JSON con un listado detallado de las infracciones del vehículo.

ejemplo:

![Img 6](/imagenes/img_6.png)

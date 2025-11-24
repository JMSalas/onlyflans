# ONLYFLANS

## Plataforma Web de Venta y Catálogo de Postres Flan

[![Framework](https://img.shields.io/badge/Framework-Django-092E20?style=flat-square&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Lenguaje](https://img.shields.io/badge/Lenguaje-Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Database](https://img.shields.io/badge/Database-SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)](https://www.sqlite.org/index.html)

> **OnlyFlans** es una aplicación web dinámica construida con el framework **Django (Python)**. Funciona como un catálogo digital que permite a los usuarios explorar diferentes tipos de postres flan, proporcionando una base para un sistema de e-commerce o una simple galería con formularios de contacto y gestión de contenido.

---

## ✨ Características Principales (Features)

El proyecto implementa la arquitectura Modelo-Vista-Template (MVT) de Django para ofrecer las siguientes funcionalidades:

* **Gestión de Modelos:** Integración con la base de datos (SQLite por defecto) para la gestión persistente de productos (Flanes), órdenes de compra y mensajes de contacto.
* **Catálogo de Flanes:** Muestra los productos de forma dinámica, cargando la información (nombre, descripción, imagen, precio) directamente desde la base de datos.
* **Formulario de Contacto:** Permite a los visitantes enviar mensajes directamente al administrador, demostrando la capacidad de manejar y procesar datos ingresados por el usuario.
* **Panel de Administración (Admin Site):** Utiliza el *Django Admin Site* para que el administrador pueda crear, leer, actualizar y eliminar (CRUD) fácilmente los registros del catálogo y revisar los mensajes de contacto.
* **Sistema de Enrutamiento:** Manejo de múltiples rutas URL a través de la configuración de `urls.py` a nivel de proyecto y aplicación.
* **Componentes Front-end:** Uso de HTML, CSS y minimalista JavaScript para una interfaz de usuario limpia y funcional.

---

## Tecnologías Utilizadas

El corazón de **OnlyFlans** es el stack de desarrollo basado en Python y Django:

| Categoría | Tecnología | Versión | Rol en el Proyecto |
| :--- | :--- | :--- | :--- |
| **Backend** | Python | 3.x | Lenguaje principal del servidor. |
| **Framework** | Django | 4.x / 5.x | Estructura MVT para desarrollo web. |
| **Base de Datos**| SQLite | - | Base de datos por defecto para el desarrollo. |
| **Front-end** | HTML, CSS, JS | - | Creación de las plantillas (Templates) y estilos. |

---

## Inicio Rápido (Setup e Instalación)

Para clonar y ejecutar este proyecto de Django en tu entorno local, sigue los siguientes pasos.

### Requisitos

* Python 3.x instalado.
* Git.

### 1. Clonar el Repositorio

Abre tu terminal y ejecuta el siguiente comando:

```bash
git clone [https://github.com/JMSalas/onlyflans.git](https://github.com/JMSalas/onlyflans.git)
cd onlyflans
````

### 2\. Configurar el Entorno Virtual

Es altamente recomendable usar un entorno virtual para aislar las dependencias del proyecto:

```bash
# Crear el entorno virtual (venv)
python -m venv venv

# Activar el entorno virtual
# En Windows:
.\venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```

### 3\. Instalar Dependencias

Instala todas las librerías de Python necesarias (incluyendo Django):

```bash
# Asume la existencia de un archivo requirements.txt con la dependencia de Django
pip install -r requirements.txt 
# O, si no existe el archivo:
pip install django
```

### 4\. Ejecutar Migraciones y Crear Superusuario

Aplica las migraciones para configurar la base de datos y crea un superusuario para acceder al panel de administración:

```bash
# Aplicar migraciones
python manage.py migrate

# Crear superusuario (sigue las instrucciones en pantalla)
python manage.py createsuperuser
```

### 5\. Iniciar el Servidor de Desarrollo

Una vez configurado, puedes iniciar la aplicación localmente:

```bash
python manage.py runserver
```

La aplicación estará accesible en tu navegador en: `http://127.0.0.1:8000/`.

-----

## 📂 Estructura del Proyecto

El proyecto sigue la estructura estándar de Django, con un proyecto principal y una aplicación web dedicada:

```
onlyflans/
├── onlyflans/              # Directorio del Proyecto Principal (Configuración global)
│   ├── settings.py         # Configuración del proyecto.
│   ├── urls.py             # Enrutamiento de URLs a nivel de proyecto.
│   └── wsgi.py
├── web/                    # Directorio de la Aplicación Principal
│   ├── migrations/
│   ├── models.py           # Definición de las tablas de la base de datos (Flanes, Contacto).
│   ├── views.py            # Lógica de las vistas.
│   ├── templates/          # Archivos HTML (plantillas).
│   └── urls.py             # Enrutamiento de URLs a nivel de aplicación.
├── manage.py               # Utilidad de línea de comandos de Django.
└── db.sqlite3              # Base de datos de desarrollo.
```

-----

## 👤 Autor

Desarrollado por: **José Miguel Salas Markov**

| Plataforma | Enlace |
| :--- | :--- |
| **GitHub** | [@JMSalas](https://www.google.com/search?q=https://github.com/JMSalas) |

```
```
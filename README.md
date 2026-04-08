# Sistema de Gestión de Compras - Taller 2

## Integrantes del Grupo
 * **Duvan Paternina**
 * **Juan Moreno**

## Descripción del Sistema
 Este sistema es una herramienta de consola desarrollada en **Python** que aplica los principios de POO, Permite a los usuarios administrar un inventario dinámico de productos, facilitando tareas de registro, visualización y análisis de costos.

### Características Principales
 * **Clase Producto:** Estructura base para definir objetos con atributos de nombre y precio.
 * **Clase ListaProductos:** Actúa como un contenedor inteligente que encapsula la lógica de:
 * Registro sin duplicados.
 * Sumatoria automática de precios (Punto 3).
 * Filtrado dinámico por umbral de precio (Punto 4).
 * **Interfaz de Usuario:** Menú interactivo con validaciones básicas.

##  Arquitectura del Software
El sistema está diseñado bajo un modelo de capas lógicas para facilitar el mantenimiento y la escalabilidad:

### 1. Clase `Producto` (Entidad)
Representa la unidad básica de información. 
* **Atributos:** `nombre` (string) y `precio` (float).
* **Métodos:** Implementa `__str__` para garantizar una representación legible de los datos al usuario final.

### 2. Clase `ListaProductos` (Gestor de Datos)
Funciona como el controlador central del inventario. Sus métodos principales incluyen:
* **`agregar_producto`**: Valida que no existan registros nulos o duplicados antes de la inserción.
* **`sumar_precios`**: Realiza una operación de agregación sobre el arreglo de productos para devolver el valor total de la inversión.
* **`productos_mayores_a_precio`**: Implementa una estructura de filtrado (List Comprehension) para segmentar el inventario según criterios económicos.

---

##  Especificaciones Técnicas
* **Lenguaje:** Python 3.10 o superior.
* **Entorno:** Consola / Terminal.
* **Control de Versiones:** Git con flujo de trabajo basado en **Feature Branches** (`rama-juan-moreno-taller`).
* **Editor:** Visual Studio Code.

---

##  Guía de Instalación y Despliegue

### Requisitos Mínimos
* Tener instalado el intérprete de PPython
* Git configurado en el sistema local.

### Paso 1: Clonación del Repositorio
Obtenga una copia local del proyecto utilizando:
```bash
git clone [https://github.com/DuvanPaternina/taller-2.git](https://github.com/DuvanPaternina/taller-2.git)

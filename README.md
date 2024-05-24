Descripción
Este programa es una aplicación de interfaz gráfica de usuario (GUI) desarrollada en Tkinter que permite a los usuarios gestionar la ejecución de trabajos asignándolos a máquinas basadas en sus tiempos de ejecución. El software simula el proceso y genera un diagrama de Gantt para visualizar la planificación de las tareas.

Funcionalidad
Ingreso de Datos: Permite introducir el número de máquinas y trabajos, así como los detalles específicos de cada trabajo.
Simulación: Ejecuta una simulación de la planificación de tareas basada en los datos ingresados.
Visualización: Muestra un diagrama de Gantt que representa la planificación de las tareas.
Instrucciones de Uso
Iniciar la Aplicación: Al abrir el programa, se te solicitará ingresar el número de máquinas. Introduce un número y haz clic en "OK".
Ingreso de Trabajos: Después se te pedirá el número de trabajos. Introduce el número correspondiente y presiona "OK".
Detalles de los Trabajos: Se abrirán ventanas emergentes para ingresar los detalles de cada trabajo, como se describe a continuación:
Trabajo 1:
Nombre del trabajo: EjemploA
Operaciones: O1, O2, O3
Tiempos de ejecución en cada máquina (se introducen en una nueva ventana emergente para cada operación).
Repetir para cada trabajo según el número introducido en el paso 2.
Iniciar Simulación: Una vez completados todos los detalles, haz clic en "Iniciar Simulación" para generar el diagrama de Gantt.
Estructura del Código
Clases Principales:
Operation: Representa una operación individual en un trabajo.
Job: Agrupa múltiples operaciones.
Machine: Gestiona la cola de operaciones y el tiempo de finalización de las tareas en una máquina específica.
Funciones Importantes:
schedule_operation(): Planifica una operación en una máquina.
process_queue(): Procesa la cola de tareas en una máquina.
start_simulation(): Inicia la simulación y crea el diagrama de Gantt.
Requisitos
Python 3.x
Tkinter
Matplotlib

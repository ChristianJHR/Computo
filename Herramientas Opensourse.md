# Herramientas Opensourse

**Alumno:** Christian de Jesus Hernandez Ruiz

**Matricula:** 210300546

## Introduccion

El cómputo de alto desempeño (HPC) permite resolver problemas complejos mediante el uso de múltiples procesadores trabajando 
en paralelo. Para aprovechar esta capacidad, existen herramientas open source que facilitan la gestión de recursos, la 
programación distribuida y el análisis de grandes volúmenes de datos. Estas soluciones son fundamentales en 
áreas como la ciencia, la ingeniería y la inteligencia artificial.

### SLURM (Simple Linux Utility for Resource Management)
SLURM es una de las herramientas de gestión de recursos y planificación de tareas más utilizadas en entornos de 
cómputo de alto desempeño. Es un software de código abierto que permite asignar recursos del clúster como CPU, 
memoria y GPU a distintos trabajos, controlar su ejecución y programar tareas en cola. Es muy escalable y utilizado 
en centros de supercómputo a nivel mundial. Además, ofrece flexibilidad para definir políticas de uso y cuenta con una 
amplia comunidad de soporte.

### OpenPBS (Portable Batch System)
OpenPBS es un sistema de planificación de tareas por lotes que permite a los usuarios enviar trabajos a un clúster de 
computadoras. A través de una interfaz de línea de comandos, los usuarios pueden definir qué recursos necesitan y cuánto 
tiempo estiman que tomará su ejecución. Esta herramienta es ampliamente conocida por su estabilidad y facilidad de 
integración con otros sistemas, lo que la hace ideal para instituciones educativas y centros de investigación.

### HTCondor
HTCondor es una herramienta especializada en la ejecución de trabajos distribuidos que requieren una planificación 
compleja o que necesitan ejecutarse durante largos períodos de tiempo. Está diseñado para aprovechar recursos ociosos en 
clústeres heterogéneos, lo cual lo hace muy eficiente en ambientes donde se combinan diferentes tipos de máquinas. 
HTCondor también facilita la ejecución de trabajos de tipo “high-throughput”, donde se procesan grandes volúmenes de 
datos en paralelo.

### MPI (Message Passing Interface)
MPI es el estándar principal para la programación paralela en sistemas distribuidos. Permite que múltiples procesos 
trabajen conjuntamente en un mismo problema, compartiendo información a través del envío y recepción de mensajes. 
Existen varias implementaciones open source de MPI, como OpenMPI y MPICH, las cuales son altamente compatibles con 
lenguajes como C, C++ y Fortran. MPI es fundamental en muchas aplicaciones científicas que requieren sincronización 
precisa entre procesos.

### OpenMP
OpenMP es una interfaz que permite programar aplicaciones paralelas en arquitecturas de memoria compartida, como 
computadoras multinúcleo. Su principal ventaja es la simplicidad de uso, ya que basta con agregar directivas al 
código fuente en C, C++ o Fortran para habilitar la ejecución en paralelo. OpenMP es ideal para algoritmos que pueden 
dividirse en tareas independientes que se ejecutan simultáneamente en diferentes núcleos de un mismo equipo.

### CUDA y alternativas (OpenCL, HIP)
CUDA es una plataforma de computación paralela desarrollada por NVIDIA que permite aprovechar el poder de procesamiento 
de las tarjetas gráficas (GPUs). Aunque no es completamente open source, es ampliamente utilizada por su eficiencia. 
Como alternativas libres se encuentran OpenCL, que es una plataforma abierta para cómputo en CPU y GPU, y HIP 
(Heterogeneous-computing Interface for Portability), desarrollada por AMD, que permite programar aplicaciones 
paralelas portables entre arquitecturas.

### Lustre
Lustre es un sistema de archivos distribuidos diseñado específicamente para entornos HPC. Es capaz de manejar 
petabytes de datos y soportar miles de clientes accediendo simultáneamente a archivos. Su diseño distribuido 
permite un rendimiento extremo, lo que lo convierte en una opción ideal para supercomputadoras y clústeres científicos 
donde el acceso eficiente a grandes volúmenes de información es crítico.

### BeeGFS (The Fraunhofer Parallel File System)
BeeGFS es otro sistema de archivos distribuido optimizado para entornos HPC, que ofrece un balance ideal entre facilidad
de uso y rendimiento. Permite una instalación modular y escalable, lo que significa que puede adaptarse tanto a pequeños 
clústeres como a grandes instalaciones de investigación. BeeGFS destaca por su rendimiento consistente en lectura y 
escritura, y por su facilidad de integración con herramientas de monitoreo.

### Ganglia
Ganglia es una herramienta ligera y escalable para la monitorización en tiempo real de clústeres y sistemas distribuidos. 
Permite recopilar métricas sobre uso de CPU, memoria, red y otros parámetros de desempeño, lo que ayuda a los 
administradores a identificar cuellos de botella o fallas. Su arquitectura distribuida le permite escalar a miles 
de nodos sin pérdida significativa de rendimiento.

### Prometheus + Grafana
Prometheus es un sistema de recopilación de métricas que, junto con Grafana, permite crear dashboards visuales 
interactivos para monitorear el estado del clúster. Es ideal para visualizar el uso de recursos, el comportamiento 
de aplicaciones y detectar fallos. Su enfoque moderno y flexible ha llevado a su adopción en muchos entornos HPC, 
especialmente donde se requiere una presentación visual clara del estado de los sistemas.

### GROMACS
GROMACS es una herramienta de simulación de dinámica molecular, utilizada principalmente en el campo de la 
bioquímica para estudiar el comportamiento de moléculas como proteínas o lípidos. Es altamente optimizada para 
correr en paralelo tanto en CPU como en GPU, y se ejecuta eficientemente en clústeres HPC. Su comunidad activa y 
constante desarrollo la han posicionado como una de las herramientas más confiables en su campo.

### LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator)
LAMMPS es una herramienta open source para simulaciones de materiales a nivel atómico. Es ampliamente utilizada 
en la ciencia de materiales, química y física. Al estar diseñada para ser ejecutada en paralelo, puede escalar 
a miles de núcleos de procesamiento, lo cual la hace ideal para simulaciones complejas en supercomputadoras.

### OpenFOAM (Open Field Operation and Manipulation)
OpenFOAM es un paquete de software especializado en dinámica de fluidos computacional (CFD), utilizado en ingeniería, 
aeronáutica y automotriz. Permite simular flujos de fluidos, transferencia de calor y otros fenómenos físicos. 
Su diseño modular y extensible lo hace adaptable a distintas necesidades, y es capaz de ejecutarse eficientemente en 
entornos paralelos gracias a su integración con MPI.

### Singularity / Apptainer
Singularity (ahora conocido como Apptainer) es una herramienta de contenedores especialmente diseñada para entornos HPC. 
A diferencia de Docker, Singularity está orientado a sistemas multiusuario y permite a los científicos empaquetar sus 
entornos de ejecución sin comprometer la seguridad del sistema. Esto facilita la portabilidad de aplicaciones complejas 
entre diferentes sistemas y asegura que los experimentos sean reproducibles.

## CONCLUSION

El cómputo de alto desempeño (HPC) es clave para la ciencia y la tecnología moderna. Gracias a herramientas open source 
como SLURM, MPI, OpenFOAM y Singularity, es posible gestionar recursos, programar en paralelo, simular fenómenos 
complejos y asegurar la portabilidad del software, todo sin costos de licencia. Estas soluciones permiten a universidades, 
centros de investigación y empresas acceder a tecnologías avanzadas de manera eficiente y escalable.

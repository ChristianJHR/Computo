# Reporte de la Implementacion y Pruebas de Carga en un Entorno de Dacker con HAProxy y Wordpress

## Introduccion

En este reporte se documenta la implementacion, configuracion y pruebas de cargas realizadas en un entorno de docker que 
utiliza HAProxy como balanceador de carga y multiples instancias de Wordpress con una base de MariaDb Galera Cluster,
todo ejeccutado dentro de una maquina virtual con el sistema operativo de Ubuntu Desktop 24.04.

## Configuracion del Entorno

El entorno de la maquina virtual utilizadsa esta compeusta por los siguientes seervicioos:

- HAProxy ( **master** ): Es el balanceador de carga para distribuir el trafico entre los servidores web.

- Servidores Web ( **webnode1, webnode2, webnode3** ): Instancias de Wordpress corrinedo en contenedores Docker.

- Base de Datos ( **dbnode1, dbnode2, dbnode3** ): Cluster de bases de datos MariaDB Galera para peplicacion y alta disponibilidad.

    ### Archivos de Configuracion ###

  El despliege del entonrno se realiza mediante **docker-compose.yml**, que contiene lass definiciones de los servicios. S e han realizado modificaciones en los archivos de configuracion para garantizar la conectividad y balanceo de carga.

## Despliege del Entorno con Docker Compose

  ### Ejecucion de Comandos

  Para iniciar los contenedores, se ejecuto el siguiente comando en la terminal de Ubuntu:

  ```
  cd haproxylb
  cd containerized
  ```

  Estos comnados fueron utilizados para ingresar a las carpetas necesarias.

  ```
  docker-compose up -d
  ```

  Comando utilizado para lebantar los contenedores.

  ### Errores encontrados y Soluciones aplicadas.

  - **Descripcion**: Algunos ccontnedores no iniciaban devidamente a problemas con los bolumenes y las ip.
  - **Solucion**: Se detuvieron los volumenes y se reinicio el cluster.

  ```
  docker-compose down -v
  ```

  Comando utilizado para detener y elimiar los clusters

  ```
  docker-compose up -d
  ```

  Comando utilizado para levantar nuevamnete los clusters.

  

![Levantaminedo de docker compose](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2021-28-34.png)

![Visualizacion del volumen y los contenedores creados](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2021-32-30.png?raw=true)


![Entrada al dbnode1](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2021-28-56.png?raw=true)

![Visualizacion de las bases de datos](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2021-28-56.png?raw=true)
![Creacionde base de dato prueba](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2021-30-21.png?raw=true)

![Entrada y visualizacion de la base de datos desde dbnode2](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2021-30-36.png?raw=true)
![Entrada y visualizacion de la base de datos desde dbnode3](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2021-30-45.png?raw=true)

![Entrada a Wordpress](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2022-12-43.png?raw=true)

![Pruba de estres con siage con 100 usuarios en 5 minutos](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2021-32-56.png?raw=true)

![Evidencia de la prueba de estres de siage](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2021-33-10.png?raw=true)

![Resultado de la prueba de estres de siage](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2021-46-38.png?raw=true)

![Prueba de estres con ab con 100 usuarios en 6 minutos](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2021-46-56.png?raw=true)

![Evidencia de la prueba de estres de ab](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2021-47-10.png?raw=true)

![Resultado de la prueba de estres de ab](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2021-57-00.png?raw=true)

![Resultado de la prueba de estres de ab](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2021-57-14.png?raw=true)

![Grafica del resultado del siage con 33785 transacciones y transacciones exitosas](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20de%20pantalla%202025-04-02%20231923.png?raw=true)

![Grafica de datos del resultado de ab con 7908 peticiones completas](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20de%20pantalla%202025-04-02%20233532.png?raw=true)

![Gracfica de tiempos de conexion ab](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20de%20pantalla%202025-04-02%20234255.png?raw=true)

![Grafica de tiempos de distribucion de ab](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20de%20pantalla%202025-04-02%20234559.png?raw=true)

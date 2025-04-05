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
  docker images
  ```

  Comando utilizado para ver las imagenes creadas.

  ### Visualizacion de las iamgenes creadas.
  
  ![Imagen creada](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-04%2017-26-29.png?raw=true)

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

  - **Descripcion**: HAProxy no distribuia el trafico entre los nodos web.
  - **Solucion**: Se reviso el archivo de configuracion HAProxy y se corrigieron las direcciones ip.

### Evidencia de Levantamiento de los nodos con docker-compose.

Se aprecia la eliminacion y el levantamiendo de los nodos con docker-compose.

![Levantaminedo de docker compose](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2021-28-34.png)

### Visualizacion del volumen y los contenedores creados.

En esta imagen se aprecia la creacion de los dbnodes y los webnodes. 

![Visualizacion del volumen y los contenedores creados](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2021-32-30.png?raw=true)

## Configuracion de la conexion entre los nodos de la Base de Datos.

El cluster de MariaDB Galera esta conformado por dbnode1, dbnode2 y dbnode3.

```
docker exec -it dbnode1 bash
```

Comando utilizado para ingresar a los dbnodes respectivamente.

```
mysql -u root -p
```

Comando utilizado pra entrar en modo root dentro del node y posteriormmente ccolocar la contraseña configurada para acceder.

![Entrada al dbnode1](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2021-28-56.png?raw=true)

Para vizualizar la base de datos dentro del node, se utiliza el siguiente comando.

```
show databases:
```

![Visualizacion de las bases de datos](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2021-28-56.png?raw=true)

El siguiente comando es utilizado para la creacion de la base de datos para comprobar la conexion entre los nodes.

```
create database markdown;
```

![Creacionde base de dato prueba](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2021-30-21.png?raw=true)

## Evidencia de la conexion entre los nodes.

![Entrada y visualizacion de la base de datos desde dbnode2](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2021-30-36.png?raw=true)
![Entrada y visualizacion de la base de datos desde dbnode3](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2021-30-45.png?raw=true)

## Entrada a Wordpress

![Entrada a Wordpress](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2022-12-43.png?raw=true)

## Pruebas de Carga

### Pruebas con **Siege**

Se realizaron las pruebas de carga en el balanceador de carga HAProxy, distribuyendo las peticiones a los tres nodos web.
Estas prueba se realizo con 100 usuarios en 5 minutos, utilizando el siguiente ccomando.

```
siege -c 100 -i -b -v -t 5m http://localhost:8083
```

![Pruba de estres con siage con 100 usuarios en 5 minutos](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2021-32-56.png?raw=true)

### Evidencia del rendimeindo al ejecutar la prueba.

![Evidencia de la prueba de estres de siage](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2021-33-10.png?raw=true)

### Resultados de la prueba de carga.

![Resultado de la prueba de estres de siage](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2021-46-38.png?raw=true)

### Pruebas con **ab**

Para evaluar el reendimiendo con ab, se ejecuto la siguiente prueba.

```
ab -n 3000 -c 100 -t 300 http://localhost:8083/
```

![Prueba de estres con ab con 100 usuarios en 6 minutos](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2021-46-56.png?raw=true)

### Evidencia deñ rendimeinto al ejecutar la prueba.

![Evidencia de la prueba de estres de ab](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2021-47-10.png?raw=true)

### Resultado de la prueba de carga.

![Resultado de la prueba de estres de ab](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2021-57-00.png?raw=true)

![Resultado de la prueba de estres de ab](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2021-57-14.png?raw=true)

## Graficas de los resultados de las pruebas realizadas.

### Grafica de resultado de **Siage** con 33785 transacciones y transaccciones exitosas.

![Grafica del resultado del siage con 33785 transacciones y transacciones exitosas](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20de%20pantalla%202025-04-02%20231923.png?raw=true)

### Grafica de resultado de **ab** con 7908 peticioness completaadas. 

![Grafica de datos del resultado de ab con 7908 peticiones completas](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20de%20pantalla%202025-04-02%20233532.png?raw=true)

### Grafica de tiempos de conexion ab.

![Gracfica de tiempos de conexion ab](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20de%20pantalla%202025-04-02%20234255.png?raw=true)

### Grafica de tiempos de distribucion ab.

![Grafica de tiempos de distribucion de ab](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20de%20pantalla%202025-04-02%20234559.png?raw=true)

## Diagrama de Arquitectura

![Diagrama de arquitectura](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20de%20pantalla%202025-04-04%20200112.png?raw=true)

## Conclusion

La implementacion de HAProxy y MariaDB Galera en Docker demostro ser efectiva para balancear carga  y garantizar alta disponibilidad, Se resolvieron problemas de configuracion y conectividad, las prubas de carga validaron la capacidad del sistemaa para manejar multiples usuarios concurrentes.

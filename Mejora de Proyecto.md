# Reporte de la Mejora de la Implementacion y Pruebas de Carga en un Entorno de Docker con HAProxy y Wordpress

## Introduccion

Este reporte detalla la mejora arquitectonica realizada a un entorno Dockerizado que inicialmente implementaba un cluster de base de datos MariaDB Galera y multiples instancias de WordPress. La mejora principal consistio en la implementacion de 
balanceadores HAProxy dedicados: uno para la capa web (**haproxy-web**) y otro para la base de datos (**haproxy-bd**). Ambos balanceadores fueron añadidos al archivo **docker-compose.yml**, junto con las configuraciones necesarias para permitir alta disponibilidad, distribucion de carga y tolerancia a fallos.

## Configuracion del Entorno

La arquitectura original del entorno estaba compuesto por:

- 3 nodos de base de datos Galera: dbnode1, dbnode2, dbnode3.

- 3 nodos de WordPress: webnode1, webnode2, webnode3.

- 1 balanceador HAProxy llamado master: manejaba únicamente el tráfico HTTP hacia los nodos web.

    ### Separación del Balanceo Web y de Base de Datos

    Para lograr una arquitectura más robusta, se decidió:

     - Reemplazar el nodo master por dos nuevos balanceadores:

	- haproxy-web: balancea el tráfico HTTP (puerto 80) entre los servidores WordPress.

	- haproxy-db: balancea las conexiones entrantes hacia el clúster MariaDB Galera.

## Funcionalidad de los Nuevos Servicios

🟢 **haproxy-web**
- Redirige el tráfico HTTP entrante hacia los tres nodos WordPress disponibles.
- Proporciona **alta disponibilidad y distribución equitativa de carga**.
- En caso de caída de uno o más servidores, el balanceador mantiene el servicio activo.

🔵 **haproxy-db**
- Balancea las conexiones hacia los nodos **dbnode1, dbnode2, y dbnode3** del clúster Galera.
- Se encarga de distribuir conexiones de lectura y/o escritura según la configuración.
- Mejora el rendimiento y confiabilidad de las conexiones a la base de datos.

## Cambios Aplicados en **docker-compose.yml**

  ```
    haproxy-web:
    container_name: haproxy-web
    image: haproxy
    networks:
      network_galera:
        ipv4_address: 172.19.0.111
    ports:
      - "80:80"
    volumes:
      - ./haproxy-web.cfg:/usr/local/etc/haproxy/haproxy.cfg
    depends_on:
      - webnode1
      - webnode2
      - webnode3

  haproxy-db:
    container_name: haproxy-db
    image: haproxy
    networks:
      network_galera:
        ipv4_address: 172.19.0.112
    ports:
      - "3310:3306"  # Puerto cambiado para evitar conflicto con dbnode1
    volumes:
      - ./haproxy-db.cfg:/usr/local/etc/haproxy/haproxy.cfg
    depends_on:
      - dbnode1
      - dbnode2
      - dbnode3

  ```
## Configuración de Archivos HAProxy

  haproxy-web.cfg.

  ```
  frontend http_front
   bind *:80
   default_backend web_servers

backend web_servers
   balance roundrobin
   server web1 172.19.0.107:80 check
   server web2 172.19.0.108:80 check
   server web3 172.19.0.109:80 check

  ```

  haproxy-db.cfg.

  ```
  frontend mysql_front
   bind *:3306
   default_backend galera_cluster

backend galera_cluster
   balance roundrobin
   mode tcp
   option mysql-check user root
   server db1 172.19.0.104:3306 check
   server db2 172.19.0.105:3306 check
   server db3 172.19.0.106:3306 check


  ```

  Detenemos los Contenedores para que los cambios sean aplicados.

  ```
  docker-compose down -v
  ```

  Comando utilizado para detener y elimiar los clusters

  ```
  docker-compose up -d
  ```

  Comando utilizado para levantar nuevamnete los clusters.

### Evidencia de Levantamiento de los nodos con docker-compose.

Se aprecia la eliminacion y el levantamiendo de los nodos con docker-compose.

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

![Entrada al dbnode1](https://github.com/user-attachments/assets/86aab82a-680c-429d-a5d7-68198c882e5d)

## Entrada a Wordpress

![Entrada a Wordpress](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-04-02%2022-12-43.png?raw=true)

## Pruebas de Carga

### Pruebas con **Siege**

Se realizaron las pruebas de carga en el balanceador de carga HAProxy, distribuyendo las peticiones a los tres nodos web.
Estas prueba se realizo con 100 usuarios en 5 minutos, utilizando el siguiente ccomando.

```
siege -c 100 -i -b -v -t 5m http://localhost:8083
```

![Pruba de estres con siage con 100 usuarios en 5 minutos](https://github.com/user-attachments/assets/b8893584-444c-49e7-860b-8bd906829e53)

### Evidencia del rendimeindo al ejecutar la prueba.

![Evidencia de la prueba de estres de siage](https://github.com/user-attachments/assets/31206489-8c49-4797-ac70-0ac613841289)

### Resultados de la prueba de carga.

![Resultado de la prueba de estres de siage](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20desde%202025-05-06%2000-10-44.png?raw=true)

### Pruebas con **ab**

Para evaluar el reendimiendo con ab, se ejecuto la siguiente prueba.

```
ab -n 3000 -c 100 -t 300 http://localhost:8083/
```

![Prueba de estres con ab con 100 usuarios en 6 minutos](https://github.com/user-attachments/assets/604aa6fc-c2f0-40b1-8beb-f5f9cffb41af)

### Evidencia deñ rendimeinto al ejecutar la prueba.

![Evidencia de la prueba de estres de ab](https://github.com/user-attachments/assets/d3fd57f2-70e7-4a94-859c-70f15de06045)


### Resultado de la prueba de carga.

![Resultado de la prueba de estres de ab](https://github.com/user-attachments/assets/36459621-45b0-4698-9c1d-1e88dccaf6cc)

![Resultado de la prueba de estres de ab](https://github.com/user-attachments/assets/183dc633-c569-48f0-b7f8-e4494071db78)

## Graficas de los resultados de las pruebas realizadas.

### Grafica de resultado de **Siage** con 874784 transacciones y transaccciones exitosas.

![Grafica del resultado del siage con 33785 transacciones y transacciones exitosas](https://github.com/user-attachments/assets/afe075f2-cad8-484e-8641-982c4c54151b)

### Grafica de resultado de **ab** con 50000 peticioness completaadas. 

![Grafica de datos del resultado de ab con 7908 peticiones completas](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20de%20pantalla%202025-05-07%20122411.png?raw=true)

### Grafica de tiempos de conexion ab.

![Gracfica de tiempos de conexion ab](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20de%20pantalla%202025-05-07%20123004.png?raw=true)

### Grafica de tiempos de distribucion ab.

![Grafica de tiempos de distribucion de ab](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20de%20pantalla%202025-05-07%20124007.png?raw=true)

## Diagrama de Arquitectura

![Diagrama de arquitectura](https://github.com/ChristianJHR/Computo/blob/main/Capturas%20de%20pantalla/Captura%20de%20pantalla%202025-04-04%20200112.png?raw=true)

## Conclusion

La refactorización de la arquitectura con la integración de dos balanceadores HAProxy ofrece una solución robusta, altamente disponible y escalable para entornos de producción o pruebas avanzadas. Al utilizar HAProxy tanto en la capa web como en la base de datos, se logra una distribución eficiente del tráfico, mejorando el rendimiento general del sistema y asegurando su continuidad incluso ante fallas parciales o caídas de nodos.

Además de mejorar la tolerancia a fallos, esta configuración permite una gestión más flexible y facilita futuras mejoras como la implementación de certificados SSL para comunicaciones seguras, autenticación de usuarios, monitoreo en tiempo real y mecanismos automáticos de failover. En conjunto, esta arquitectura mejora tanto la estabilidad como la capacidad de crecimiento del sistema.

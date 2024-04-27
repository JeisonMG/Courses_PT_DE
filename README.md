# Diagrama de la arquitectura

![image](https://github.com/JeisonMG/Courses_PT_DE/assets/89539582/435c34c5-9033-4f08-b9fa-6f4d251380f0)

# Desafío Global - Prueba Técnica

Este repositorio contiene todos los archivos necesarios para cumplir con el desafío propuesto en la prueba técnica de Global.

## Nota

- Los siguientes scripts fueron desarrollados en Azure Databricks. Por lo tanto, si se abren desde otro IDE, es posible que se encuentren con algunos códigos o mensajes que no sean muy agradables a la vista.

- Cada script cuenta con una configuración de conexión pensada para entornos separados. Además, utiliza un SAS token para conectarse al Azure Data Lake, el cual caduca el próximo 03/05/2024.

- Se han dejado quemados/seteados varios datos "sensibles". En un escenario óptimo, se utilizaría Azure Key Vault para la encriptación y el consumo de estos.

## Contenido

- En la carpeta `scripts` encuentra los siguientes dos archivos .ipynb:

  - El script `src_generate_course_data` se encarga de ejecutar lo solicitado en el primer y segundo desafío. Opté por guardar las tablas/dataframes "categories" y "levels" en formato CSV, ya que contienen datos simples y su volumetría es pequeña, aprovechando así un formato plano para una mayor eficiencia en su consumo. En el caso de la tabla/dataframe "courses", opté por guardarlo en formato Parquet debido a su eficiencia en el almacenamiento y la lectura de datos estructurados, especialmente cuando hay una gran cantidad de registros.
  
  - Las tablas mencionadas representan lo que en un escenario más grande conocemos como datamart con un modelo tipo estrella.

  - El script `write_course_data_into_sql` se encarga de ejecutar lo solicitado en el tercer desafío. El cual realiza la lectura de la data guardada en el azure datalake, genera los dataframes correspondientes, filtra la tabla/dataframe "courses" para implementar un carga en bacth o lotes a la tabla final que se encuentra en una azure SQL. 

- Las siguientes credenciales proporcionan acceso de lectura y escritura al SQL Server:
  - Servidor: srvsql-pt-de.database.windows.net
  - Usuario: read_write_user
  - Contraseña: -C2:!*Hcl4O&4e7
  
- En la carpeta `API_Courses` se encuentra el código fuente, de la API desarrollada para consumir la vista generada en la Azure SQL (DTU). La API se encuentra desarrollada en Python 3.9.13 y desplegada en una Azure Function.

## Endpoint de Consumo

El endpoint de consumo es el siguiente:

```
https://func-pt-de.azurewebsites.net/api/GetRecentCourses?code=9h_QaDXpwkdJFXKa8aiTaooJjLjslQIs0yWrKfXi_6yiAzFuIS7LnA==
```

## Escalabilidad y Costo

La solución es altamente escalable a nivel de infraestructura, puesto que, se encuentra implementada en la nube de Azure. Las funcionalidades se han dejado parametrizadas para ser aprovechadas en futuras caracteristicas.

Actualmente (26/04/2024 07:30 PM), el costo es mínimo. Dos días de consumo (aproximadamente 9 horas) me han facturado $1.03.

Los servicios/recursos desplegados son: 
- Azure SQL (DTU).
- Databricks Premium con un clúster single node Standard_DS3_V2.
- Azure Data Lake Gen2.
- Azure Function tipo serverless (consumo).

# Usar la imagen base de Python
FROM python:3.9-slim

# Crear un directorio temporal en el contenedor para almacenar los archivos del sitio web
WORKDIR /usr/src/app

# Copiar los archivos del sitio web y el script Python al contenedor
COPY temp_site/ /usr/src/app/temp_site/
COPY servidor.py /usr/src/app/

# Exponer el puerto 7529 en el contenedor
EXPOSE 7529

# Ejecutar el script Python para servir el sitio web
CMD ["python", "servidor.py"]

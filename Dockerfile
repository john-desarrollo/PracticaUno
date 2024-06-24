# Configuracion del archivo docker

# Dockerfile

# Utilizar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el script Python desde el host al contenedor
COPY palindromo.py .

# Comando para ejecutar el script cuando se inicie el contenedor
ENTRYPOINT ["python", "palindromo.py"]
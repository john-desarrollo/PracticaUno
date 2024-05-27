# Usa una imagen ligera de servidor web como base
FROM nginx:alpine

# Copia los archivos HTML, CSS y JavaScript al directorio de trabajo del contenedor
COPY . /usr/share/nginx/html